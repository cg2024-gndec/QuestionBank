r"""
=============================================================================
Script: ocr_book_pdf.py
Description: Automated 80-page Windows Media OCR script to extract text and 
             exercises from scanned textbook PDFs into chapter markdown files.
Environment: Requires .venv with pymupdf, winrt-Windows.Media.Ocr, 
             winrt-Windows.Graphics.Imaging, winrt-Windows.Storage.Streams, 
             winrt-Windows.Foundation, and winrt-Windows.Globalization.
Usage: .\.venv\Scripts\python.exe QuestionBank\scripts\ocr_book_pdf.py
=============================================================================
"""

import fitz
import asyncio
import os
import sys
import winrt.windows.media.ocr as ocr
import winrt.windows.globalization as glob
import winrt.windows.graphics.imaging as imaging
import winrt.windows.storage.streams as streams

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_PATH = os.path.join(BASE_DIR, "COMPREHENSION_BOOK_4.pdf")
OUTPUT_DIR = os.path.join(BASE_DIR, "chapters")

CHAPTER_MAP = [
    {"num": "01", "title": "Empty Pot", "pages": (5, 9)},
    {"num": "02", "title": "The Cave that Talked", "pages": (10, 14)},
    {"num": "03", "title": "The King and the Foolish Monkey", "pages": (15, 18)},
    {"num": "04", "title": "Beginnings of Traffic Lights", "pages": (19, 22)},
    {"num": "05", "title": "The Telephone", "pages": (23, 26)},
    {"num": "06", "title": "Swar Kokila : Lata Mangeshkar", "pages": (27, 31)},
    {"num": "07", "title": "Sachin Tendulkar", "pages": (32, 35)},
    {"num": "08", "title": "Bhagat Singh", "pages": (36, 39)},
    {"num": "09", "title": "About Garba", "pages": (40, 43)},
    {"num": "10", "title": "Boat Races Festival Kerala", "pages": (44, 47)},
    {"num": "11", "title": "Lifecycle of a Frog", "pages": (48, 51)},
    {"num": "12", "title": "Kaveri", "pages": (52, 55)},
    {"num": "13", "title": "Spring", "pages": (56, 59)},
    {"num": "14", "title": "Be Kind", "pages": (60, 62)},
    {"num": "15", "title": "A Child's Thought of God", "pages": (63, 66)}
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
        sys.exit(1)
        
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    doc = fitz.open(PDF_PATH)
    lang = glob.Language("en-US")
    engine = ocr.OcrEngine.try_create_from_language(lang)
    
    if not engine:
        print("Error: Could not initialize Windows OCR engine for language 'en-US'.")
        sys.exit(1)
        
    print(f"Opened {PDF_PATH} ({len(doc)} pages). Starting OCR processing...")
    
    ocr_results = {}
    for p in range(1, len(doc) + 1):
        text = await ocr_page(engine, doc[p-1])
        ocr_results[p] = text
        if p % 10 == 0 or p == len(doc):
            print(f"  Processed page {p}/{len(doc)}")
            
    print("\nGenerating chapter markdown files under 'chapters/'...")
    for ch in CHAPTER_MAP:
        start_p, end_p = ch["pages"]
        ch_text = []
        for p in range(start_p, end_p + 1):
            page_content = ocr_results.get(p, "").strip()
            ch_text.append(f"### Page {p}\n\n{page_content}")
            
        full_content = f"# Chapter {ch['num']}: {ch['title']}\n\n"
        full_content += f"**Source**: *My Book of English COMPREHENSION & COMPOSITION 4* (Pages {start_p}-{end_p})\n\n"
        full_content += "---\n\n"
        full_content += "## Complete Textbook Content & Exercises (OCR Extracted)\n\n"
        full_content += "\n\n---\n\n".join(ch_text)
        
        file_path = os.path.join(OUTPUT_DIR, f"chapter_{ch['num']}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(full_content)
        print(f"  ✓ Saved chapter_{ch['num']}.md")

    print("\nSUCCESS: All chapter source files created with OCR text & exercises.")

if __name__ == "__main__":
    asyncio.run(run_ocr())
