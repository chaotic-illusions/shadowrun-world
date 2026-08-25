from PIL import Image, ImageFilter
import numpy as np
from scipy import ndimage

src = Image.open("docs/Monofilament_Sword.png").convert("RGB")
arr = np.array(src).astype(np.float32)
gray = arr.mean(axis=2)

x0, x1 = 0, 614
y0, y1 = 16, 554
gray_c = gray[y0:y1, x0:x1]
h, w = gray_c.shape

hx0, hx1, hy0, hy1 = 24 - x0, 600 - x0, 52 - y0, 102 - y0
bx0, bx1, by0, by1 = 11 - x0, 604 - x0, 135 - y0, 544 - y0

yy, xx = np.mgrid[0:h, 0:w]
in_header = (xx >= hx0) & (xx <= hx1) & (yy >= hy0) & (yy <= hy1)
in_box = (xx >= bx0) & (xx <= bx1) & (yy >= by0) & (yy <= by1)

dist_edge = np.minimum.reduce([np.abs(xx - bx0), np.abs(xx - bx1), np.abs(yy - by0), np.abs(yy - by1)])
BORDER_MARGIN = 26

dark_ink = gray_c < 150
box_sword = in_box & dark_ink & (dist_edge > BORDER_MARGIN)
# solid fill: any non-dark pixel inside the header block is glyph (interior + AA edge)
header_text = in_header & (gray_c >= 150)
# despeckle: drop tiny connected components (scan dust/registration marks), keep real letters
labels, n = ndimage.label(header_text)
if n:
    sizes = ndimage.sum(header_text, labels, range(1, n + 1))
    keep = np.zeros(n + 1, dtype=bool)
    keep[1:] = sizes >= 20
    header_text = keep[labels]

NEON = np.array([63, 216, 255], dtype=np.uint8)
STEEL_GRID = np.array([60, 82, 100], dtype=np.uint8)
PAGE_BG = np.array([9, 13, 22], dtype=np.uint8)
GRID_SPACING = 27.5  # measured from source scan

# Silhouette of the sword so the grid can be masked out from "inside" it
# rather than showing through the empty interior of the traced outline.
closed_for_fill = ndimage.binary_closing(box_sword, structure=np.ones((3, 3)), iterations=2)
sword_fill = ndimage.binary_fill_holes(closed_for_fill)
near_ink = ndimage.distance_transform_edt(~box_sword) <= 6
sword_fill = ndimage.binary_fill_holes(sword_fill | near_ink)

# --- procedural square grid, full-bleed, no frame ---
grid_alpha = np.zeros((h, w), dtype=np.float32)
ox, oy = bx0 % GRID_SPACING, by0 % GRID_SPACING  # keep phase continuity with the sword's original position
xs = np.arange(ox, w, GRID_SPACING)
ys = np.arange(oy, h, GRID_SPACING)
LINE_W = 1.1
for gx in xs:
    d = np.abs(xx - gx)
    grid_alpha = np.maximum(grid_alpha, np.clip(1 - d / LINE_W, 0, 1))
for gy in ys:
    d = np.abs(yy - gy)
    grid_alpha = np.maximum(grid_alpha, np.clip(1 - d / LINE_W, 0, 1))
grid_alpha = np.where(sword_fill, 0, grid_alpha)
grid_alpha *= 95  # subdued

grid_layer = np.zeros((h, w, 4), dtype=np.uint8)
grid_layer[..., 0:3] = STEEL_GRID
grid_layer[..., 3] = grid_alpha.astype(np.uint8)
grid_img = Image.fromarray(grid_layer, "RGBA")

# --- neon layer: sword ink (glow) + solid glowing header text ---
neon_alpha = np.zeros((h, w), dtype=np.float32)
neon_alpha[box_sword] = np.clip((255 - gray_c[box_sword]) / 255.0, 0, 1) * 255
neon_alpha[header_text] = gray_c[header_text]  # brightness-as-alpha -> solid glyph fill

neon_layer = np.zeros((h, w, 4), dtype=np.uint8)
neon_layer[..., 0:3] = NEON
neon_layer[..., 3] = neon_alpha.astype(np.uint8)
neon_img = Image.fromarray(neon_layer, "RGBA")

GLOW_STRENGTH = 0.5  # matches --glow 0.5 used across the other traced pieces

glow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
for radius, boost in [(16, 0.55), (8, 0.7), (3, 0.9)]:
    radius *= GLOW_STRENGTH
    boost *= GLOW_STRENGTH
    blurred = neon_img.filter(ImageFilter.GaussianBlur(radius))
    a = np.array(blurred).astype(np.float32)
    a[..., 3] *= boost
    glow = Image.alpha_composite(glow, Image.fromarray(a.astype(np.uint8), "RGBA"))
glow = Image.alpha_composite(glow, neon_img)

base_arr = np.zeros((h, w, 4), dtype=np.uint8)
base_arr[..., 0:3] = PAGE_BG
base_arr[..., 3] = 255
base_img = Image.fromarray(base_arr, "RGBA")

final = Image.alpha_composite(base_img, grid_img)
final = Image.alpha_composite(final, glow)
final.convert("RGB").save("docs/Monofilament_Sword_neon_v2.png")

transparent_base = Image.new("RGBA", (w, h), (0, 0, 0, 0))
final_t = Image.alpha_composite(transparent_base, grid_img)
final_t = Image.alpha_composite(final_t, glow)
final_t.save("docs/Monofilament_Sword_neon_v2_transparent.png")

print("done", final.size, "grid spacing", GRID_SPACING)
