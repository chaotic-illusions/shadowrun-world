"""OCR / text-extract every adventure PDF in docs/Adventures/Digital into docs/Adventures/text/<name>.txt.

Pages are written with '=== PAGE n ===' markers (1-based viewer page). Files that already have a
text layer are extracted directly; scanned files go through Tesseract. Restricted page ranges
(sourcebooks that merely contain an adventure) come from PAGE_RANGES. Duplicates are skipped.
Idempotent: an existing complete .txt is not redone.
"""
import io, os, sys, glob, time
from concurrent.futures import ProcessPoolExecutor
import pymupdf

ROOT = os.path.join(os.path.dirname(__file__), "..", "docs", "Adventures")
SRC = os.path.join(ROOT, "Digital")
OUT = os.path.join(ROOT, "text")
TESS = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

PAGE_RANGES = {
    "Shadowrun 1st - Corebook.pdf": (220, 226),
    "Shadowrun 1e - Native American Nations Volume One {FASA7202}.pdf": (6, 70),
    "Shadowrun 1e - Native American Nations Volume Two {FASA7207}.pdf": (6, 55),
    "Shadowrun 1e - Universal Brotherhood - Missing Blood {FASA7205}.pdf": (92, 146),
}
SKIP = {
    "Shadowrun 2e - Adventure - Universal Brotherhood - Missing Blood {FASA7205}.pdf",  # same as 1e file
    "Shadowrun 3e - Corporate Punishment 2060 [FASA 7330].pdf",  # B&W copy is used
}


def ocr_page(pdf, pno):
    import pytesseract
    from PIL import Image
    pytesseract.pytesseract.tesseract_cmd = TESS
    d = pymupdf.open(pdf)
    p = d[pno]
    txt = p.get_text()
    if len(txt.strip()) < 200:
        try:
            img = None
            # Prefer the raw embedded scan: MuPDF mis-renders some grayscale JPEG scans (e.g. the
            # Mercurial copies) into stripes, while PIL decodes the same bytes cleanly.
            imgs = sorted(p.get_images(), key=lambda im: im[2] * im[3], reverse=True)
            if imgs and imgs[0][2] >= 600:
                try:
                    raw = d.extract_image(imgs[0][0])
                    img = Image.open(io.BytesIO(raw["image"]))
                    img.load()
                except Exception:  # noqa: BLE001 -- fall back to rendering
                    img = None
            if img is None:
                pix = p.get_pixmap(dpi=200)
                img = Image.open(io.BytesIO(pix.tobytes("png")))
            txt = pytesseract.image_to_string(img, timeout=90)
            if len(txt.strip()) < 100 and imgs:  # raw image unreadable? try the render too
                pix = p.get_pixmap(dpi=200)
                alt = pytesseract.image_to_string(Image.open(io.BytesIO(pix.tobytes("png"))), timeout=90)
                if len(alt.strip()) > len(txt.strip()):
                    txt = alt
        except Exception as e:  # noqa: BLE001 -- one bad page must not sink the file
            txt = f"[OCR FAILED: {e!r}]"
    return pno, txt


def main():
    files = sorted(f for f in glob.glob(os.path.join(SRC, "*.pdf")) if os.path.basename(f) not in SKIP)
    if len(sys.argv) > 1:  # optional: restrict to the named PDFs (basenames)
        files = [f for f in files if os.path.basename(f) in set(sys.argv[1:])]
    jobs = []
    for f in files:
        base = os.path.basename(f)
        out = os.path.join(OUT, os.path.splitext(base)[0] + ".txt")
        if os.path.exists(out) and os.path.getsize(out) > 0:
            continue
        n = len(pymupdf.open(f))
        lo, hi = PAGE_RANGES.get(base, (1, n))
        jobs.append((f, out, lo, hi))
    print(f"{len(jobs)} files to process", flush=True)
    with ProcessPoolExecutor(max_workers=6) as ex:
        for f, out, lo, hi in jobs:
            t0 = time.time()
            pages = dict(ex.map(ocr_page, [f] * (hi - lo + 1), range(lo - 1, hi)))
            with open(out + ".part", "w", encoding="utf-8") as fh:
                for pno in range(lo - 1, hi):
                    fh.write(f"\n=== PAGE {pno + 1} ===\n{pages[pno]}")
            os.replace(out + ".part", out)
            print(f"{time.time()-t0:6.0f}s  p{lo}-{hi}  {os.path.basename(out)}", flush=True)


if __name__ == "__main__":
    main()
