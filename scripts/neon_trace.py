"""
Trace a scanned gear-catalog illustration (title bar + line art, optionally
a bordered graph-paper grid box) into a neon-blue schematic on a dark ground.

Usage:
    python neon_trace.py path/to/scan.png [-o output.png]
    python neon_trace.py path/to/scan.png --neon 3fd8ff --steel 3c525f --bg 090d16
    python neon_trace.py path/to/scan.png --no-grid       # force no grid
    python neon_trace.py path/to/scan.png --debug         # dump intermediate masks

Everything (content crop, title-bar box, border-frame box, grid spacing,
grid presence) is auto-detected per image, so input images do not need to
share dimensions, DPI, or layout proportions.
"""
import argparse
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage
from scipy.signal import find_peaks
from skimage.filters import threshold_otsu


def hex_to_rgb(s):
    s = s.lstrip("#")
    return np.array([int(s[i:i + 2], 16) for i in (0, 2, 4)], dtype=np.uint8)


def despeckle(mask, min_size):
    labels, n = ndimage.label(mask)
    if n == 0:
        return mask
    sizes = ndimage.sum(mask, labels, range(1, n + 1))
    keep = np.zeros(n + 1, dtype=bool)
    keep[1:] = sizes >= min_size
    return keep[labels]


def strip_corner_marks(mask, region_bbox, corner_frac=0.2, max_area_frac=0.05):
    """Drop small components that sit entirely in a corner of region_bbox
    and are tiny relative to the main subject -- a publisher's stamp or
    watermark, not part of the drawing.
    """
    rx0, ry0, rx1, ry1 = region_bbox
    rw, rh = rx1 - rx0, ry1 - ry0
    lbl, n = ndimage.label(mask)
    if n == 0:
        return mask
    sizes = ndimage.sum(mask, lbl, range(1, n + 1))
    main_size = sizes.max()
    objs = ndimage.find_objects(lbl)
    keep = np.ones(n + 1, dtype=bool)
    for i, sl in enumerate(objs):
        if sl is None:
            continue
        ys0, ys1 = sl[0].start, sl[0].stop
        xs0, xs1 = sl[1].start, sl[1].stop
        near_left = xs1 <= rx0 + corner_frac * rw
        near_right = xs0 >= rx1 - corner_frac * rw
        near_top = ys1 <= ry0 + corner_frac * rh
        near_bottom = ys0 >= ry1 - corner_frac * rh
        in_corner = (near_left or near_right) and (near_top or near_bottom)
        if in_corner and sizes[i] < max_area_frac * main_size:
            keep[i + 1] = False
    keep[0] = False
    return keep[lbl]


def to_outline(mask, iterations=2):
    """Reduce a mask of filled ink regions to just their boundary. Some
    source art shades with solid black (highlights, shadows, tire fills)
    rather than pure line work; gluing a full neon glow onto that reads as
    a solid glowing blob, not a traced outline. Eroding and taking the
    difference converts a fill into a thin ring at its edge. Genuinely thin
    strokes are unaffected: eroding a 1-2px line already empties it, so the
    "boundary" (original minus nothing) is just the original line back.
    """
    eroded = ndimage.binary_erosion(mask, structure=np.ones((3, 3)), iterations=iterations)
    return mask & ~eroded


def negative_fill(mask, iterations=2):
    """Keep filled ink regions solid (preserving the shading/depth read the
    source used solid black for) and add a neon rim around whatever white
    shapes are enclosed *inside* them -- highlight streaks, a headlight dot,
    reflections -- so that fine detail isn't lost inside a flat glowing
    silhouette. Background that isn't enclosed (the general page/canvas
    area) is left alone; binary_fill_holes only catches topologically
    enclosed holes, not anything touching the array edge.
    """
    holes = ndimage.binary_fill_holes(mask) & ~mask
    hole_rim = to_outline(holes, iterations=iterations)
    return mask | hole_rim


def content_bbox(mask, pad=14):
    ys, xs = np.where(mask)
    if len(xs) == 0:
        raise ValueError("no ink found in image")
    h, w = mask.shape
    x0, x1 = max(xs.min() - pad, 0), min(xs.max() + pad, w)
    y0, y1 = max(ys.min() - pad, 0), min(ys.max() + pad, h)
    return x0, y0, x1, y1


def find_title_bar(dark_mask, w, h):
    """Locate the title bar by its row-wise dark-pixel fraction rather than
    connected components: a solid filled bar (even with letter-shaped holes)
    reads as a sustained run of high-fraction rows near the top. Component
    labeling is fragile here because the bar sometimes touches the border
    frame below it through a single stray pixel, fusing them into one blob.
    """
    row_frac = dark_mask.mean(axis=1)
    top_limit = int(0.35 * h)
    HI, LO = 0.15, 0.04

    start = None
    for y in range(top_limit):
        if row_frac[y] > HI:
            start = y
            break
    if start is None:
        return None

    end = start
    low_run = 0
    for y in range(start, h):
        if row_frac[y] > LO:
            end = y + 1
            low_run = 0
        else:
            low_run += 1
            if low_run > 3:
                break

    bh = end - start
    if bh < 10 or bh > 0.4 * h:
        return None

    band = dark_mask[start:end, :]
    cols = np.where(band.any(axis=0))[0]
    if len(cols) == 0:
        return None
    x0, x1 = int(cols.min()), int(cols.max()) + 1
    if (x1 - x0) < 0.45 * w:
        return None
    return (x0, start, x1, end)


def find_border_frame(dark_mask, search_bbox):
    """Detect a thin rectangular border ring by shape: a component whose bbox
    spans most of the search region but whose fill ratio is low (a ring
    occupies little of its own bounding box, unlike a solid blob).

    Returns the border's *own pixel mask* (dilated by a couple pixels to
    cover anti-aliasing), not a geometric band between outer/inner bboxes.
    A band sized to safely clear the ring's rounded corners has to be much
    thicker than the actual stroke, and blindly excluding that whole band
    swallows any real subject linework that happens to pass through it
    (e.g. a front sight sitting close to the top edge) even though it has
    nothing to do with the border itself.
    """
    x0, y0, x1, y1 = search_bbox
    region = dark_mask[y0:y1, x0:x1]
    rh, rw = region.shape
    if rh == 0 or rw == 0:
        return None
    lbl, n = ndimage.label(region)
    if n == 0:
        return None
    objs = ndimage.find_objects(lbl)
    best = None
    for i, sl in enumerate(objs):
        if sl is None:
            continue
        ys0, ys1 = sl[0].start, sl[0].stop
        xs0, xs1 = sl[1].start, sl[1].stop
        bw, bh = xs1 - xs0, ys1 - ys0
        if bw < 0.7 * rw or bh < 0.7 * rh:
            continue
        comp_mask = lbl[sl] == (i + 1)
        area = comp_mask.sum()
        fill = area / (bw * bh)
        if fill > 0.15:
            continue  # far too solid to be a border, alone or fused to content
        if fill > 0.06:
            # Ambiguous band: a genuine border ring measures 0.036-0.047 fill
            # clean, but if subject linework happens to touch it (an armor
            # figure's line brushing the frame), the fused component's fill
            # can climb into the low 0.1s -- the same range sprawling subject
            # art with no border at all can also land in (a car drawn
            # corner-to-corner measured 0.113 once and erased the whole
            # drawing). Fill ratio alone can't tell these apart; whether the
            # component encloses one big dominant background region can: a
            # border (fused or not) still encloses the interior as one large
            # hole, while sprawling art fragments into many small gaps
            # (windows, panel seams) with no single dominant one.
            holes = ndimage.binary_fill_holes(comp_mask) & ~comp_mask
            hlbl, hn = ndimage.label(holes)
            biggest_frac = 0.0
            if hn > 0:
                hole_sizes = ndimage.sum(holes, hlbl, range(1, hn + 1))
                biggest_frac = hole_sizes.max() / (bw * bh)
            if biggest_frac < 0.45:
                continue

        score = bw * bh
        if best is None or score > best[0]:
            perim = 2 * (bw + bh)
            # Estimating stroke from the *whole* component's area/perimeter
            # is fine for a clean ring but badly inflates once fused content
            # is mixed in (a touching figure once pushed a ~4px stroke's
            # estimate up to 13px, ballooning the exclusion margin to 82px
            # and eating the figure's head along with the border). Probe a
            # small fixed band first -- mostly just the ring itself, rarely
            # enough fused content to skew it much -- and estimate stroke
            # from that instead.
            yy_p, xx_p = np.mgrid[0:bh, 0:bw]
            probe_edge = np.minimum.reduce([xx_p, bw - 1 - xx_p, yy_p, bh - 1 - yy_p])
            probe = comp_mask & (probe_edge <= 15)
            stroke = max(probe.sum() / perim, 1.0)
            margin = stroke * 6 + 4  # still used to size the *interior* bbox
            best = (score, (xs0 + x0, ys0 + y0, xs1 + x0, ys1 + y0), margin, comp_mask, stroke)
    if best is None:
        return None
    _, outer, margin, comp_mask, stroke = best
    ox0, oy0, ox1, oy1 = outer
    m = int(round(margin))
    inner = (ox0 + m, oy0 + m, ox1 - m, oy1 - m)

    # The winning component can be the border ring fused to subject content
    # that happens to touch it (a figure's helmet brushing the frame) -- the
    # fill/hole tests above correctly still recognize that blob as
    # border-shaped overall, but excluding it wholesale would erase whatever
    # touched it too. Re-derive just the near-edge portion of the component
    # (real border stroke, generously margined for corners) rather than
    # trusting the full blob as the exclusion mask.
    bh_c, bw_c = comp_mask.shape
    yy_c, xx_c = np.mgrid[0:bh_c, 0:bw_c]
    dist_edge_c = np.minimum.reduce([xx_c, bw_c - 1 - xx_c, yy_c, bh_c - 1 - yy_c])
    comp_mask = comp_mask & (dist_edge_c <= m)

    full_h, full_w = dark_mask.shape
    border_mask = np.zeros((full_h, full_w), dtype=bool)
    dilate_px = max(2, int(round(stroke)) + 1)
    dilated = ndimage.binary_dilation(comp_mask, iterations=dilate_px)
    border_mask[oy0:oy0 + bh_c, ox0:ox0 + bw_c] = dilated

    return outer, inner, border_mask


def profile_spacing(profile, min_lines=5, min_span_frac=0.55):
    """Find evenly-spaced line positions in a 1-D density profile (sum of a
    thin-line mask along one axis) via prominent local maxima, and return
    the median spacing if enough consistently-spaced lines are found.

    A real background grid has lines running the full extent of the box;
    a localized repeating texture (e.g. slide serrations, grip checkering)
    produces the same kind of evenly-spaced peaks but only across a small
    slice of the profile. min_span_frac rejects the latter.
    """
    profile = profile.astype(np.float64)
    if profile.max() <= 0:
        return None
    peaks, _ = find_peaks(profile, prominence=max(profile.max() * 0.12, 1.0), distance=6)
    if len(peaks) < min_lines:
        return None
    if (peaks.max() - peaks.min()) < min_span_frac * len(profile):
        return None
    diffs = np.diff(peaks)
    med = np.median(diffs)
    if med <= 0:
        return None
    consistent = diffs[np.abs(diffs - med) < 0.35 * med]
    if len(consistent) < min_lines - 1:
        return None
    return float(np.median(consistent))


def detect_grid(light_ink_mask, region_bbox, min_lines=5):
    x0, y0, x1, y1 = region_bbox
    sub = light_ink_mask[y0:y1, x0:x1]
    if sub.size == 0:
        return None
    # A real grid covers a meaningful fraction of the interior with lines
    # (~10-11% measured across every confirmed grid so far). When there's no
    # grid at all, the two-tier Otsu split still finds *some* "light ink"
    # tier out of scan noise / print dither, and it can occasionally show
    # weak, coincidentally-consistent spacing -- but only ever covering a
    # tiny fraction of the area (<1%), nowhere near a real grid's coverage.
    if sub.mean() < 0.03:
        return None
    row_profile = sub.sum(axis=1)
    col_profile = sub.sum(axis=0)
    sx = profile_spacing(col_profile, min_lines)
    sy = profile_spacing(row_profile, min_lines)
    # a real grid is periodic on BOTH axes at roughly the same pitch; a
    # one-axis-only hit is almost always a repeating texture (serrations,
    # checkering) rather than a background grid, so require agreement.
    if sx is None or sy is None:
        return None
    if abs(sx - sy) > 0.3 * max(sx, sy):
        return None
    return float((sx + sy) / 2)


def make_glow(neon_img, layers=((16, 0.55), (8, 0.7), (3, 0.9)), strength=1.0):
    """strength scales both the blur radius and its opacity boost for every
    layer, so 1.0 is the full designed glow, 0.0 is the crisp line with no
    halo at all, and anything between gives a proportionally smaller one.
    """
    w, h = neon_img.size
    glow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    if strength > 0:
        for radius, boost in layers:
            r = radius * strength
            if r < 0.5:
                continue
            blurred = neon_img.filter(ImageFilter.GaussianBlur(r))
            a = np.array(blurred).astype(np.float32)
            a[..., 3] *= boost * strength
            glow = Image.alpha_composite(glow, Image.fromarray(a.astype(np.uint8), "RGBA"))
    return Image.alpha_composite(glow, neon_img)


def trace(path, out_path, neon_rgb, steel_rgb, bg_rgb, force_grid=None, debug=False,
          outline_fills=False, negative_fill_mode=False, glow_strength=1.0):
    src = Image.open(path).convert("RGB")
    arr = np.array(src).astype(np.float32)
    gray_full = arr.mean(axis=2)

    # Some source scans crop their ink almost flush with the file's own
    # edge (no margin to spare). A flat black line survives that fine, but
    # a glow needs room to fade -- without real margin to crop into, it
    # gets hard-clipped by the canvas boundary instead of tapering off like
    # it does on every other side. Pad with synthetic "paper" margin up
    # front so there's always room, regardless of what the source has.
    MARGIN = 40
    gray_full = np.pad(gray_full, MARGIN, mode="constant", constant_values=255)

    non_white = gray_full[gray_full < 250]
    if non_white.size < 50:
        raise ValueError("image appears blank")
    # global Otsu on the raw image separates *bold* ink (title bar fill,
    # border, subject linework) from everything lighter (grid lines + paper)
    # in one shot -- a full-image histogram is dominated by two clusters
    # (bold ink vs. "everything light"), so this reliably becomes t_dark,
    # not a paper/ink split.
    t_dark = threshold_otsu(gray_full)
    dark_mask = gray_full < t_dark

    x0, y0, x1, y1 = content_bbox(dark_mask)
    W, H = x1 - x0, y1 - y0

    dark_c = dark_mask[y0:y1, x0:x1]
    gray_c = gray_full[y0:y1, x0:x1]

    # grid lines (if any) are only distinguishable from paper *within the
    # crop*, once the huge blank page margin is gone -- a fresh local Otsu
    # over just the non-dark pixels here can actually separate "light gray
    # line" from "white paper", which a whole-image Otsu cannot (2-class
    # Otsu can't find both splits at once against a 3-cluster histogram).
    non_dark = gray_c[~dark_c]
    midtone = non_dark[non_dark < 245]
    if midtone.size > max(200, 0.003 * W * H) and midtone.std() > 3:
        t_light = threshold_otsu(non_dark)
        light_c = ~dark_c & (gray_c < t_light)
    else:
        light_c = np.zeros_like(dark_c)

    title_box = find_title_bar(dark_c, W, H)

    search_region = (0, title_box[3] if title_box else 0, W, H)
    frame = find_border_frame(dark_c, search_region)

    yy, xx = np.mgrid[0:H, 0:W]
    in_title_full = np.zeros((H, W), dtype=bool)
    in_title_text_zone = np.zeros((H, W), dtype=bool)
    if title_box:
        tx0, ty0, tx1, ty1 = title_box
        in_title_full = (xx >= tx0) & (xx <= tx1) & (yy >= ty0) & (yy <= ty1)
        # Just enough margin to stay off the box's own boundary pixels --
        # letterforms in bold/rounded display fonts routinely overshoot right
        # up to the bar's edge (a round letter like "C" needs to sit a hair
        # taller/wider than a flat one to look optically even), and a
        # fraction-of-bar-size pad was clipping that overshoot on tightly-set
        # titles. The solid-row filter below (not this pad) is what actually
        # guards against a decorative bevel/highlight line near the edge.
        pad_x = pad_y = 2
        in_title_text_zone = (xx >= tx0 + pad_x) & (xx <= tx1 - pad_x) & (yy >= ty0 + pad_y) & (yy <= ty1 - pad_y)

    header_text = in_title_text_zone & ~dark_c
    if title_box:
        # letterforms have gaps (moderate per-row light fraction); a decorative
        # bevel/highlight line across the bar is ~solid across its full width.
        # Drop any such near-solid rows before they get treated as glyphs.
        bar_not_dark = ~dark_c[ty0:ty1, tx0:tx1]
        row_frac = bar_not_dark.mean(axis=1)
        solid_rows = np.where(row_frac > 0.82)[0] + ty0
        if len(solid_rows):
            header_text[solid_rows, :] = False
    # decorative serif fonts often threshold into disconnected fragments --
    # a curved letter's spur or terminal pinches down to a gap the ink
    # doesn't survive thresholding across. A soft glow blur alone only
    # papers over this (the pieces still read as separate blobs up close);
    # physically closing small gaps first makes the glyph actually solid.
    header_text = ndimage.binary_dilation(header_text, iterations=2)
    # a stray scan-dust speck is a handful of pixels; even a thin/round
    # glyph fragment (a serif "G" or "U") is easily 15-30px, so a small
    # fixed floor removes noise without eating letterforms.
    header_text = despeckle(header_text, min_size=14)

    in_border = np.zeros((H, W), dtype=bool)
    interior_bbox = (0, title_box[3] if title_box else 0, W, H)
    if frame:
        outer, inner, border_mask = frame
        in_border = border_mask
        interior_bbox = inner

    subject_ink = dark_c & ~in_title_full & ~in_border
    subject_ink = despeckle(subject_ink, min_size=3)  # drop scan-dust flecks, keep real strokes
    subject_ink = strip_corner_marks(subject_ink, interior_bbox)  # drop publisher stamps/watermarks

    # Silhouette used later to keep the background grid out from "inside"
    # the subject. subject_ink itself is just line art -- flood-filling its
    # enclosed regions turns a closed outline (a gun body, a car) into a
    # solid shape. A light closing first bridges the small gaps thresholding
    # leaves where a traced line's antialiasing thins to nothing for a
    # pixel or two, without fusing separate nearby strokes (checkering,
    # parallel detail lines) into one blob.
    closed_for_fill = ndimage.binary_closing(subject_ink, structure=np.ones((3, 3)), iterations=2)
    subject_fill = ndimage.binary_fill_holes(closed_for_fill)
    # Some enclosed pockets never become topologically "enclosed" at all --
    # a dashed decorative line (a stitching groove, a selector diamond) has
    # gaps too wide for the closing above but is still clearly meant to read
    # as solid once traced, and small print gaps between converging lines
    # (a stock meeting a receiver) can leave a sliver that fill_holes can't
    # see as a hole because it never fully closes. Anything within a few
    # pixels of *any* ink is background too fine to matter for grid-hiding
    # purposes, so fold it in directly rather than fighting each case with
    # more closing (which would risk fusing unrelated nearby strokes).
    near_ink = ndimage.distance_transform_edt(~subject_ink) <= 6
    subject_fill = ndimage.binary_fill_holes(subject_fill | near_ink)

    if outline_fills:
        subject_ink = to_outline(subject_ink)
    elif negative_fill_mode:
        subject_ink = negative_fill(subject_ink)

    # Draw the grid across the whole remaining canvas below the title, not
    # just the frame's measured interior. A small bbox-based pad isn't
    # enough: the neon *glow* halo bleeds well past the actual ink (up to
    # its blur radius), so anything less than full-bleed leaves a visible
    # seam between "glow with grid behind it" and "glow with no grid" right
    # where a sight or barrel tip pokes near the interior's edge.
    grid_region = (0, title_box[3] if title_box else 0, W, H)

    grid_spacing = None
    if force_grid is not False:
        grid_spacing = detect_grid(light_c, interior_bbox)
        if force_grid is True and grid_spacing is None:
            grid_spacing = 28.0

    # --- compose layers ---
    base_arr = np.zeros((H, W, 4), dtype=np.uint8)
    base_arr[..., 0:3] = bg_rgb
    base_arr[..., 3] = 255
    base_img = Image.fromarray(base_arr, "RGBA")

    layer = base_img
    if grid_spacing:
        grid_alpha = np.zeros((H, W), dtype=np.float32)
        gx0, gy0, gx1, gy1 = grid_region
        line_w = 1.1
        for gx in np.arange(gx0, gx1, grid_spacing):
            d = np.abs(xx - gx)
            grid_alpha = np.maximum(grid_alpha, np.clip(1 - d / line_w, 0, 1))
        for gy in np.arange(gy0, gy1, grid_spacing):
            d = np.abs(yy - gy)
            grid_alpha = np.maximum(grid_alpha, np.clip(1 - d / line_w, 0, 1))
        region_mask = (xx >= gx0) & (xx <= gx1) & (yy >= gy0) & (yy <= gy1)
        grid_alpha = np.where(region_mask & ~subject_fill, grid_alpha, 0) * 95
        grid_layer = np.zeros((H, W, 4), dtype=np.uint8)
        grid_layer[..., 0:3] = steel_rgb
        grid_layer[..., 3] = grid_alpha.astype(np.uint8)
        layer = Image.alpha_composite(layer, Image.fromarray(grid_layer, "RGBA"))

    subject_alpha = np.zeros((H, W), dtype=np.float32)
    subject_alpha[subject_ink] = np.clip((255 - gray_c[subject_ink]) / 255.0, 0, 1) * 255
    subject_layer = np.zeros((H, W, 4), dtype=np.uint8)
    subject_layer[..., 0:3] = neon_rgb
    subject_layer[..., 3] = subject_alpha.astype(np.uint8)
    subject_glow = make_glow(Image.fromarray(subject_layer, "RGBA"), strength=glow_strength)

    text_alpha = np.zeros((H, W), dtype=np.float32)
    text_alpha[header_text] = gray_c[header_text]
    text_layer = np.zeros((H, W, 4), dtype=np.uint8)
    text_layer[..., 0:3] = neon_rgb
    text_layer[..., 3] = text_alpha.astype(np.uint8)
    # a wider bridging pass than the subject glow: scanned display fonts
    # often break into disconnected serif fragments once thresholded, and
    # a soft wide halo reads them back as one contiguous glowing word.
    text_glow = make_glow(
        Image.fromarray(text_layer, "RGBA"),
        layers=((26, 0.42), (14, 0.55), (7, 0.75), (3, 0.95)),
        strength=glow_strength,
    )

    glow = Image.alpha_composite(subject_glow, text_glow)

    final = Image.alpha_composite(layer, glow)
    final.convert("RGB").save(out_path)

    transparent = Image.alpha_composite(Image.new("RGBA", (W, H), (0, 0, 0, 0)), layer if grid_spacing else Image.new("RGBA", (W, H), (0, 0, 0, 0)))
    if grid_spacing:
        # rebuild grid-only layer over transparency (layer above included bg fill)
        transparent = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        transparent = Image.alpha_composite(transparent, Image.fromarray(grid_layer, "RGBA"))
    transparent = Image.alpha_composite(transparent, glow)
    t_path = str(Path(out_path).with_name(Path(out_path).stem + "_transparent.png"))
    transparent.save(t_path)

    if debug:
        dbg = Path(out_path).with_name(Path(out_path).stem + "_debug.txt")
        dbg.write_text(
            f"t_dark={t_dark:.1f}\n"
            f"content_bbox=({x0},{y0},{x1},{y1}) size={W}x{H}\n"
            f"title_box={title_box}\n"
            f"frame={(frame[0], frame[1]) if frame else None}\n"
            f"grid_spacing={grid_spacing}\n"
        )

    return out_path, t_path, (W, H), title_box, frame, grid_spacing


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("input")
    p.add_argument("-o", "--output")
    p.add_argument("--neon", default="3fd8ff")
    p.add_argument("--steel", default="3c525f")
    p.add_argument("--bg", default="090d16")
    grid_group = p.add_mutually_exclusive_group()
    grid_group.add_argument("--no-grid", action="store_true")
    grid_group.add_argument("--force-grid", action="store_true")
    p.add_argument("--debug", action="store_true")
    fill_group = p.add_mutually_exclusive_group()
    fill_group.add_argument("--outline-fills", action="store_true",
                             help="reduce solid-filled shading (shadows, highlights, tire fills) to a "
                                  "thin boundary outline instead of glowing it as a solid shape; use "
                                  "for art with heavy shading rather than pure line work")
    fill_group.add_argument("--negative-fill", action="store_true",
                             help="keep solid-filled shading as solid glowing fill (preserving the "
                                  "depth/shading read), and instead outline whatever white shapes are "
                                  "enclosed inside it (highlight streaks, a headlight dot, reflections)")
    p.add_argument("--glow", type=float, default=1.0,
                    help="glow intensity from 0.0 (crisp line, no halo) to 1.0 (full designed glow, "
                         "the default). Scales both blur radius and opacity.")
    args = p.parse_args()

    in_path = Path(args.input)
    out_path = Path(args.output) if args.output else in_path.with_name(in_path.stem + "_neon.png")

    force = None
    if args.no_grid:
        force = False
    elif args.force_grid:
        force = True

    result = trace(
        in_path, out_path,
        hex_to_rgb(args.neon), hex_to_rgb(args.steel), hex_to_rgb(args.bg),
        force_grid=force, debug=args.debug, outline_fills=args.outline_fills,
        negative_fill_mode=args.negative_fill, glow_strength=args.glow,
    )
    out_png, t_png, size, title_box, frame, spacing = result
    print(f"saved {out_png}  ({size[0]}x{size[1]})")
    print(f"saved {t_png}")
    print(f"title bar: {'found' if title_box else 'not found'}")
    print(f"border frame: {'found' if frame else 'not found'}")
    print(f"grid: {'spacing=%.1f' % spacing if spacing else 'none'}")


if __name__ == "__main__":
    sys.exit(main())
