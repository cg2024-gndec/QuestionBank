"""
=============================================================================
Script: ocr_book_pdf.py
Description: Automated Windows Media OCR script to extract text and
             exercises from COMPREHENSION BOOK 3 PDF into chapter markdown files.
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
WORKSPACE_ROOT = os.path.dirname(os.path.dirname(BASE_DIR))
PDF_PATH = os.path.join(
    WORKSPACE_ROOT,
    "COMPREHENSION BOOK",
    "COMPREHENSION BOOK\u20143.pdf"
)
OUTPUT_DIR = os.path.join(BASE_DIR, "chapters")

CHAPTER_MAP = [
    {"num": "01", "title": "The Foolish Pandit", "pages": (5, 8)},
    {"num": "02", "title": "The Jackal and the Dhol", "pages": (9, 12)},
    {"num": "03", "title": "Two Cats and the Monkey", "pages": (13, 16)},
    {"num": "04", "title": "Fountain Pen", "pages": (17, 19)},
    {"num": "05", "title": "Invention of Steam Engine", "pages": (20, 23)},
    {"num": "06", "title": "Flying Sikh - Milkha Singh", "pages": (24, 27)},
    {"num": "07", "title": "Ustad Zakir Hussain: The Tabla Maestro", "pages": (28, 31)},
    {"num": "08", "title": "Chandrashekhar Azad", "pages": (32, 35)},
    {"num": "09", "title": "Harvest Festival of India", "pages": (36, 39)},
    {"num": "10", "title": "The Indian Deserts", "pages": (40, 43)},
    {"num": "11", "title": "The Brahmaputra River: A Lifeline of South Asia", "pages": (44, 47)},
    {"num": "12", "title": "The Magic of Rain", "pages": (48, 51)},
    {"num": "13", "title": "The Brave Little Kite", "pages": (52, 55)},
    {"num": "14", "title": "The Talking Tree", "pages": (56, 59)},
    {"num": "15", "title": "Composition Modules", "pages": (60, 68)},
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
        full_content += f"**Source**: *My Book of English COMPREHENSION & COMPOSITION 3* (Pages {start_p}-{end_p})\n\n"
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
