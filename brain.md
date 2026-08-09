# 🧠 Root Workspace Brain — English Question Bank Ecosystem

> **Project Scope**: Standardized English Question Bank & PDF Compilation Engine for ICSE, CBSE & State Boards (Classes I to VIII)  
> **Subject**: English (Language & Literature)  
> **Repository Root**: `s:\Question Bank making\`  
> **Books Root**: `s:\Question Bank making\English books\`  
> **Virtual Environment**: `s:\Question Bank making\.venv\Scripts\python.exe`

---

## 🏛️ System Architecture

This workspace operates as a scalable English question bank generation engine. All book projects live under the `English books\` directory and follow an identical structural, metadata, and compilation blueprint.

```
s:\Question Bank making\
├── brain.md                         <-- Top-level workspace brain & system architecture
├── master_prompt.md                 <-- Master root prompt directive & generation rules
├── index.md                         <-- Top-level workspace index & repository hub
├── progress.md                      <-- Top-level progress dashboard & metrics
├── paper_blueprint.md               <-- Examination paper blueprint
├── COMPREHENSION BOOK\              <-- Source textbook PDFs (Classes 1–8)
├── .venv\                           <-- Shared Python virtual environment
└── English books\                   <-- All book repositories
    ├── Book1_QuestionBank\          <-- Class I English Question Bank
    ├── Book2_QuestionBank\          <-- Class II English Question Bank
    ├── Book3_QuestionBank\          <-- Class III English Question Bank
    ├── Book4_QuestionBank\          <-- Class IV English Question Bank
    ├── Book5_QuestionBank\          <-- Class V English Question Bank
    ├── Book6_QuestionBank\          <-- Class VI English Question Bank
    ├── Book7_QuestionBank\          <-- Class VII English Question Bank
    └── Book8_QuestionBank\          <-- Class VIII English Question Bank
```

---

## 📐 Universal 6-Category Question Taxonomy (Per Chapter)

Each chapter contains **300 questions** organized into 6 category files (50 questions per file):

| # | Category | File Name | Description |
|---|----------|-----------|-------------|
| 1 | **MCQs** | `mcqs.md` | Multiple Choice Questions with 4 options (A, B, C, D) — factual recall, vocabulary, inference, odd-one-out |
| 2 | **Fill in the Blanks** | `fill_in_the_blanks.md` | Sentence completion testing text accuracy, grammar terms, vocabulary, and key concepts |
| 3 | **True / False** | `true_false.md` | Statement validation with detailed justification in answer keys |
| 4 | **Short Answer** | `short_answer.md` | Concise 1–3 sentence answers testing comprehension, recall, and understanding |
| 5 | **Long Answer** | `long_answer.md` | Detailed 5+ sentence responses — character analysis, theme discussion, HOTS, moral reasoning |
| 6 | **Extract Based** | `extract_based.md` | Prose/poem extracts with Reference to Context (RTC) sub-questions — speaker, context, vocabulary, meaning |

---

## 🏷️ Universal Metadata Schema

Every generated question MUST strictly conform to this metadata block format:

```markdown
### Question [N]
- **Question ID**: CH[XX]-[TYPE]-[NNN]
- **Type**: [MCQ | Fill in the Blanks | True/False | Short Answer | Long Answer | Extract Based]
- **Difficulty**: [Easy | Medium | Hard]
- **Bloom Level**: [Remembering | Understanding | Applying | Analyzing | Evaluating | Creating]
- **Topic**: [Specific Sub-topic / Concept Name]
- **Marks**: [1 | 2 | 3 | 5]

**Question**:
[Clear, precise question text]

- (A) [Option A]  ← (for MCQs only)
- (B) [Option B]
- (C) [Option C]
- (D) [Option D]

- **Answer Key**: Full explanation / model answer
```

**Question ID Prefixes:**
- `CHXX-MCQ-NNN` — MCQs
- `CHXX-FIB-NNN` — Fill in the Blanks
- `CHXX-TF-NNN` — True / False
- `CHXX-SA-NNN` — Short Answer
- `CHXX-LA-NNN` — Long Answer
- `CHXX-EXT-NNN` — Extract Based

---

## ⚡ Automation & Compilation Pipeline

All Python scripts operate from within each book's `scripts/` directory:

1. **OCR Textbook Text Extraction**:
   ```powershell
   .\.venv\Scripts\python.exe "English books\BookX_QuestionBank\scripts\ocr_book_pdf.py"
   ```
2. **Chapter PDF Compilation**:
   ```powershell
   .\.venv\Scripts\python.exe "English books\BookX_QuestionBank\scripts\compile_chapter_pdf.py" --all
   ```
3. **Master Book PDF Compilation**:
   ```powershell
   .\.venv\Scripts\python.exe "English books\BookX_QuestionBank\scripts\compile_master_book_pdf.py"
   ```
