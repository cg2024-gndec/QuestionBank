"""
=============================================================================
Script: ocr_book_pdf.py
Description: Automated Windows Media OCR script to extract text and
             exercises from COMPREHENSION BOOK 1 PDF into chapter markdown files.
Environment: Requires .venv with pymupdf, winrt-Windows.Media.Ocr,
             winrt-Windows.Graphics.Imaging, winrt-Windows.Storage.Streams,
             winrt-Windows.Foundation, and winrt-Windows.Globalization.
Usage: ..\..\..\.venv\Scripts\python.exe scripts\ocr_book_pdf.py
=============================================================================
"""

import fitz
import asyncio
import os
import sys

try:
    import winrt.windows.media.ocr as ocr
    import winrt.windows.globalization as glob
    import winrt.windows.graphics.imaging as imaging
    import winrt.windows.storage.streams as streams
    HAS_WINRT = True
except ImportError:
    HAS_WINRT = False
    print("WARNING: winrt not available. OCR will be skipped.")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(os.path.dirname(BASE_DIR))
PDF_DIR = os.path.join(ROOT_DIR, "COMPREHENSION BOOK")
# Find COMPREHENSION BOOK—1.pdf dynamically
pdf_files = [f for f in os.listdir(PDF_DIR) if f.startswith("COMPREHENSION BOOK") and "1.pdf" in f]
if pdf_files:
    PDF_PATH = os.path.join(PDF_DIR, pdf_files[0])
else:
    PDF_PATH = os.path.join(PDF_DIR, "COMPREHENSION BOOK—1.pdf")
OUTPUT_DIR = os.path.join(BASE_DIR, "chapters")

# ===================================================================
# CHAPTER_MAP — Update this after first OCR run to map pages to chapters.
# Format: {"num": "01", "title": "Chapter Title", "pages": (start, end)}
# ===================================================================
CHAPTER_MAP = [
    # TODO: Populate after reviewing the book PDF (page numbers & chapter titles)
    # Example:
    # {"num": "01", "title": "First Chapter Title", "pages": (5, 9)},
    # {"num": "02", "title": "Second Chapter Title", "pages": (10, 14)},
]

async def ocr_page(engine, page, dpi=220):
    pix = page.get_pixmap(dpi=dpi)
    img_bytes = pix.tobytes("png")

    stream = streams.InMemoryRandomAccessStream()
    writer = streams.DataWriter(stream)
    writer.write_bytes(img_bytes)
    await writer.store_async()
    writer.detach_stream()
    stream.seek(0)

    decoder = await imaging.BitmapDecoder.create_async(stream)
    software_bitmap = await decoder.get_software_bitmap_async()

    result = await engine.recognize_async(software_bitmap)
    text = "\n".join([line.text for line in result.lines])
    return text

async def run_ocr():
    if not os.path.exists(PDF_PATH):
        print(f"Error: Source PDF not found at {PDF_PATH}")
        print(f"Expected: {PDF_PATH}")
        sys.exit(1)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    doc = fitz.open(PDF_PATH)
    print(f"Opened: {PDF_PATH} ({len(doc)} pages)")

    if not HAS_WINRT:
        print("Error: winrt not available. Cannot run OCR.")
        sys.exit(1)

    lang = glob.Language("en-US")
    engine = ocr.OcrEngine.try_create_from_language(lang)

    if not engine:
        print("Error: Could not initialize Windows OCR engine for language 'en-US'.")
        sys.exit(1)

    print(f"Starting OCR on all {len(doc)} pages...")
    ocr_results = {}
    for p in range(1, len(doc) + 1):
        text = await ocr_page(engine, doc[p-1])
        ocr_results[p] = text
        if p % 10 == 0 or p == len(doc):
            print(f"  Processed page {p}/{len(doc)}")

    if not CHAPTER_MAP:
        # Dump all pages to a single raw file for manual review
        raw_path = os.path.join(OUTPUT_DIR, "raw_ocr_all_pages.md")
        with open(raw_path, "w", encoding="utf-8") as f:
            for p in sorted(ocr_results.keys()):
                f.write(f"### Page {p}\n\n{ocr_results[p]}\n\n---\n\n")
        print(f"\nCHAPTER_MAP is empty. Raw OCR saved to: {raw_path}")
        print("Review the raw file, identify chapter page ranges, then update CHAPTER_MAP and re-run.")
        return

    print("\nGenerating chapter markdown files under 'chapters/'...")
    for ch in CHAPTER_MAP:
        start_p, end_p = ch["pages"]
        ch_text = []
        for p in range(start_p, end_p + 1):
            page_content = ocr_results.get(p, "").strip()
            ch_text.append(f"### Page {p}\n\n{page_content}")

        full_content = f"# Chapter {ch['num']}: {ch['title']}\n\n"
        full_content += f"**Source**: *My Book of English COMPREHENSION & COMPOSITION 1* (Pages {start_p}-{end_p})\n\n"
        full_content += "---\n\n"
        full_content += "## Complete Textbook Content & Exercises (OCR Extracted)\n\n"
        full_content += "\n\n---\n\n".join(ch_text)

        file_path = os.path.join(OUTPUT_DIR, f"chapter_{ch['num']}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(full_content)
        print(f"  Saved chapter_{ch['num']}.md")

    print("\nSUCCESS: All chapter source files created with OCR text & exercises.")

if __name__ == "__main__":
    asyncio.run(run_ocr())
