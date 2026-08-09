# 👑 Master Project Directive — English Question Bank Engine
## ICSE / CBSE / State Board Series (Classes I to VIII)

---

## 🎯 Master Objectives

This workspace serves as the master factory for generating high-quality, board-aligned English Question Banks and publication-grade PDF documents for **Classes I to VIII**.

---

## 📁 Directory Architecture

```
s:\Question Bank making\
├── brain.md                         <-- Workspace brain & system architecture
├── master_prompt.md                 <-- This file — master generation rules
├── index.md                         <-- Workspace index & repository hub
├── progress.md                      <-- Progress dashboard & metrics
├── paper_blueprint.md               <-- Examination paper blueprint
├── COMPREHENSION BOOK\              <-- Source textbook PDFs (Books 1–8)
└── English books\                   <-- All book repositories
    └── BookN_QuestionBank\          <-- Self-contained Book Project (N = 1 to 8)
        ├── brain.md                 <-- Book-specific context & rules
        ├── index.md                 <-- Book index
        ├── progress.md              <-- Book progress tracker
        ├── master_prompt.md         <-- Book-specific directive
        ├── paper_blueprint.md       <-- Book-specific exam blueprint
        ├── chapters\                <-- Raw textbook OCR text (chapter_01.md ... chapter_15.md)
        ├── question_bank\           <-- Generated question files & PDFs per chapter
        │   └── chapter_XX\
        │       ├── mcqs.md (50 Qs)
        │       ├── fill_in_the_blanks.md (50 Qs)
        │       ├── true_false.md (50 Qs)
        │       ├── short_answer.md (50 Qs)
        │       ├── long_answer.md (50 Qs)
        │       ├── extract_based.md (50 Qs)
        │       └── Chapter_XX_Question_Bank.pdf
        └── scripts\                 <-- Automation & PDF generation scripts
```

---

## 📐 6-Category Question Taxonomy (Per Chapter)

Every chapter produces **300 questions** across 6 standardized category files:

| # | Category | File | Description |
|---|----------|------|-------------|
| 1 | **MCQs** | `mcqs.md` | 4-option MCQs: factual recall, vocabulary meaning, antonym/synonym, odd-one-out, inference |
| 2 | **Fill in the Blanks** | `fill_in_the_blanks.md` | Sentence completion: key vocabulary, grammar terms, text-based facts, missing words |
| 3 | **True / False** | `true_false.md` | Statement validation: chapter facts, character actions, event sequences — with justification |
| 4 | **Short Answer** | `short_answer.md` | 1–3 sentence answers: Who/What/Where/Why/How, definitions, brief explanations |
| 5 | **Long Answer** | `long_answer.md` | 5+ sentence responses: character analysis, theme discussion, moral reasoning, HOTS |
| 6 | **Extract Based** | `extract_based.md` | Prose/poem extracts with RTC sub-questions: speaker, context, vocabulary, line meaning, inference |

> **Note**: The exact question style should be adapted for the grade level of each book (e.g., simpler language for Class I–II, more analytical for Class VI–VIII).

---

## 🏷️ Universal Metadata Schema

Every question MUST include:

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

---

## ⚖️ Quality & Pedagogical Standards

1. **Zero Placeholders**: Never use `TBD`, dummy text, or incomplete answers.
2. **Bloom's Taxonomy Distribution**:
   - 30% Remembering — factual recall, definitions
   - 30% Understanding — explanations, summaries, cause-effect
   - 25% Applying — grammar application, contextual vocabulary
   - 15% Analyzing & Evaluating — inference, character analysis, theme extraction
3. **Age-Appropriate Language**: Match vocabulary and sentence complexity to the target grade level.
4. **Complete Answer Keys**: Every question must have a fully worked-out answer or model response.
5. **No Duplicates**: Each question must test a distinct skill or concept.

---

## 🔄 Execution Pipeline

```powershell
# Step 1: OCR Text Extraction from Textbook PDF
.\.venv\Scripts\python.exe "English books\BookX_QuestionBank\scripts\ocr_book_pdf.py"

# Step 2: Generate question content (manual — AI-assisted markdown generation)

# Step 3: Compile Chapter PDFs
.\.venv\Scripts\python.exe "English books\BookX_QuestionBank\scripts\compile_chapter_pdf.py" --all

# Step 4: Build Master PDF
.\.venv\Scripts\python.exe "English books\BookX_QuestionBank\scripts\compile_master_book_pdf.py"
```
