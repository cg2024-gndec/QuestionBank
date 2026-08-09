# 🛠️ Question Bank Project Python Utility Scripts

This directory contains standalone Python utility scripts used for text extraction, OCR, question generation, and PDF compilation for the **Class IV English Question Bank** project.

---

## 🐍 Virtual Environment Requirements

All scripts are executed using the project's local virtual environment (`.venv`):

```powershell
# Virtual Environment Path
s:\Question Bank making\.venv\Scripts\python.exe
```

### Installed Dependencies inside `.venv`
* `pypdf` (PDF text extraction)
* `pymupdf` / `fitz` (PDF rendering & rasterization)
* `pillow` (Image processing)
* `reportlab` (PDF document generation)
* `fpdf2` & `markdown` (Markdown parsing)
* `winrt-Windows.Media.Ocr` (Native Windows Media OCR engine)
* `winrt-Windows.Graphics.Imaging`, `winrt-Windows.Storage.Streams`, `winrt-Windows.Foundation`, `winrt-Windows.Globalization` (Windows WinRT bindings)

---

## 📜 Script Index & Usage

### 1. `ocr_book_pdf.py`
- **Purpose**: Runs native Windows Media OCR on all 80 pages of `COMPREHENSION_BOOK_4.pdf` to extract chapter texts, word meanings, and textbook exercise questions.
- **Output**: Populates `QuestionBank/chapters/chapter_01.md` through `chapter_15.md`.
- **Usage**:
  ```powershell
  .\.venv\Scripts\python.exe QuestionBank\scripts\ocr_book_pdf.py
  ```

---

### 2. `generate_chapter_questions.py`
- **Purpose**: Generates 25 questions per file across all 7 category files (`mcq.md`, `fillups.md`, `true_false.md`, `short.md`, `long.md`, `vocabulary.md`, `grammar.md`) following `brain.md` taxonomy and metadata schemas.
- **Output**: Populates `QuestionBank/question_bank/chapter_XX/` with 175 questions.
- **Usage**:
  ```powershell
  .\.venv\Scripts\python.exe QuestionBank\scripts\generate_chapter_questions.py --chapter 01
  ```

---

### 3. `compile_chapter_pdf.py`
- **Purpose**: Uses ReportLab to bind all 7 markdown category files of a chapter into a styled, professional 40+ page PDF document.
- **Output**: Generates `QuestionBank/question_bank/chapter_XX/Chapter_XX_Question_Bank.pdf`.
- **Usage**:
  ```powershell
  .\.venv\Scripts\python.exe QuestionBank\scripts\compile_chapter_pdf.py --chapter 01
  ```

---

### 4. `update_project_trackers.py`
- **Purpose**: Audits generated question files and PDF outputs to track project completion status.
- **Usage**:
  ```powershell
  .\.venv\Scripts\python.exe QuestionBank\scripts\update_project_trackers.py
  ```

---

## 🔄 Execution Order for Processing New Chapters

When adding or generating a new chapter (e.g. Chapter 02):
1. **Extract/Verify Source Text**:
   `.\.venv\Scripts\python.exe QuestionBank\scripts\ocr_book_pdf.py`
2. **Generate Question Bank (175 Questions)**:
   `.\.venv\Scripts\python.exe QuestionBank\scripts\generate_chapter_questions.py --chapter 02`
3. **Compile PDF Document**:
   `.\.venv\Scripts\python.exe QuestionBank\scripts\compile_chapter_pdf.py --chapter 02`
4. **Audit & Update Trackers**:
   `.\.venv\Scripts\python.exe QuestionBank\scripts\update_project_trackers.py`
