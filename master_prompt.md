# 👑 Master Project Directive — Universal Multi-Subject Question Bank Engine
## ICSE / CBSE / State Board Series (Classes I to VIII + All Academic Subjects)

---

## 🎯 Master Objectives & Scope Expansion

This workspace serves as the master factory for generating high-quality, board-aligned Question Banks and publication-grade PDF documents for **ALL ACADEMIC SUBJECTS** across Primary & Middle School (Classes I to VIII and future grade extensions).

### Supported Subject Disciplines
1. 📖 **English (Language & Literature)**: Comprehension, Composition, Grammar, RTC & Poetry Analysis.
2. 🔢 **Mathematics**: Number Systems, Arithmetic, Geometry, Algebra, Data Handling & Word Problems.
3. 🔬 **Science & EVS**: Physics, Chemistry, Biology, Environmental Studies, Experiments & Diagrams.
4. 🌍 **Social Science**: History, Civics, Political Science, Geography, Map Work & Source Analysis.
5. 🇮🇳 **Hindi & Regional Languages**: Comprehension, Vyakaran (Grammar), Patra/Anuchhed Lekhan, Kavita/Gadya RTC.
6. 💻 **Computer Studies & Coding**: Digital Literacy, Hardware/Software, Algorithms, Logic & Practical Computing.
7. 💡 **General Knowledge & Aptitude**: Current Affairs, World Facts, Logical Reasoning & General Awareness.

---

## 📁 Multi-Subject Directory Architecture

All present and future book repositories in this workspace adhere to a strictly unified folder layout adaptable to any subject:

```
s:\Question Bank making\
├── brain.md                         <-- Top-level workspace brain & multi-subject architecture
├── master_prompt.md                 <-- Master root prompt directive (This file)
├── index.md                         <-- Top-level multi-subject workspace index
├── progress.md                      <-- Top-level multi-subject progress dashboard
├── COMPREHENSION BOOK\              <-- Source textbook PDFs (All Subjects & Classes)
└── BookN_QuestionBank\              <-- Self-contained Book/Subject Project (N = 1 to 8+)
    ├── index.md                     <-- Book/Subject index
    ├── progress.md                  <-- Book/Subject tracker
    ├── master_prompt.md             <-- Subject-specific directive
    ├── brain.md                     <-- Subject-specific context
    ├── paper_blueprint.md           <-- Examination blueprint
    ├── chapters\                    <-- Raw textbook OCR text files (`chapter_01.md` ... `chapter_15.md`)
    ├── question_bank\               <-- Generated category markdown files & PDFs per chapter
    │   └── chapter_XX\
    │       ├── [cat_01].md (50 Qs)
    │       ├── [cat_02].md (50 Qs)
    │       ├── [cat_03].md (50 Qs)
    │       ├── [cat_04].md (50 Qs)
    │       ├── [cat_05].md (50 Qs)
    │       ├── [cat_06].md (50 Qs)
    │       └── Chapter_XX_Question_Bank.pdf
    ├── generated_papers\            <-- Full ICSE/CBSE Sample Papers & Answer Keys
    └── scripts\                     <-- Automation & PDF generation scripts
        ├── ocr_book_pdf.py
        ├── generate_chapter_questions.py
        ├── compile_chapter_pdf.py
        ├── compile_master_book_pdf.py
        └── update_project_trackers.py
```

---

## 📑 Subject-Specific Category Taxonomies (6 Categories per Chapter)

Every chapter in every subject contains **300 questions** divided across 6 standardized category files:

### 1. English Taxonomy
`reading_comprehension.md` (50 Qs) | `guided_writing.md` (50 Qs) | `grammar_language.md` (50 Qs) | `picture_based.md` (50 Qs) | `short_answer.md` (50 Qs) | `extract_stanza.md` (50 Qs)

### 2. Mathematics Taxonomy
`conceptual_mcqs.md` (50 Qs) | `mental_math_fillups.md` (50 Qs) | `do_as_directed_math.md` (50 Qs) | `word_problems.md` (50 Qs) | `visual_geometry_data.md` (50 Qs) | `formulae_reasoning.md` (50 Qs)

### 3. Science & EVS Taxonomy
`objective_mcqs.md` (50 Qs) | `fillups_truefalse.md` (50 Qs) | `short_definitions.md` (50 Qs) | `diagram_based.md` (50 Qs) | `long_answer_science.md` (50 Qs) | `experiment_application.md` (50 Qs)

### 4. Social Science Taxonomy
`fact_chronology_mcqs.md` (50 Qs) | `terms_definitions.md` (50 Qs) | `short_explanations.md` (50 Qs) | `map_diagram_work.md` (50 Qs) | `long_analytical.md` (50 Qs) | `source_extract_based.md` (50 Qs)

---

## 🏷️ Universal Metadata Schema

Every question generated across any subject MUST include complete metadata:

```markdown
### Question ID: BK{BookNum}_{SubCode}_CH{ChNum}_CAT{CatNum}_Q{QNum}
- **Subject**: [English | Mathematics | Science | EVS | Social Science | Hindi | Computer Studies | GK]
- **Type**: [MCQ | Numerical | Word Problem | Fill in the Blanks | Matching | Do As Directed | Short Answer | Long Answer | Diagram | RTC Extract]
- **Difficulty**: [Easy | Medium | Hard]
- **Bloom Level**: [Remembering | Understanding | Applying | Analyzing | Evaluating | Creating]
- **Topic**: [Specific Sub-topic / Concept Name]
- **Marks**: [1 | 2 | 3 | 5]

**Question**:
[Clear, precise question text. Use LaTeX \( ... \) for mathematical equations and scientific notations]

- (A) [Option A]
- (B) [Option B]
- (C) [Option C]
- (D) [Option D]

- **Answer Key**: **(Option Letter)** Complete step-by-step solution / model answer text.
```

---

## ⚖️ Multi-Subject Quality & Pedagogical Standards

1. **Zero Placeholders**: Never use `TBD`, dummy placeholders, or incomplete answers. Every question must be fully worked out.
2. **Mathematical & Scientific Formatting**: Use inline LaTeX `\( ... \)` or block LaTeX `$$ ... $$` for math symbols, fractions, powers, square roots, and chemical equations.
3. **Step-by-Step Numerical Solutions**: In Mathematics and Science numericals, the answer key MUST show full step-by-step working: Formula $\rightarrow$ Substitution $\rightarrow$ Calculation $\rightarrow$ Final Answer with Units.
4. **Bloom's Taxonomy Distribution**:
   - **30% Remembering**: Direct factual recall, definitions, formula identification.
   - **30% Understanding**: Conceptual explanations, summaries, cause-and-effect.
   - **25% Applying**: Word problems, numerical calculation, grammar application, scientific experiments.
   - **15% Analyzing & Evaluating**: Source extracts, RTC poetry analysis, multi-step problem solving, error detection.

---

## 🔄 Execution Pipeline for Any Subject

```powershell
# Step 1: OCR Text Extraction from Textbook PDF
.\.venv\Scripts\python.exe BookX_QuestionBank\scripts\ocr_book_pdf.py

# Step 2: Generate Questions for Target Subject & Chapter
.\.venv\Scripts\python.exe BookX_QuestionBank\scripts\generate_chapter_questions.py --subject [ENG|MATH|SCI|SST|HIN|CS] --chapter 01

# Step 3: Batch Compile Chapter PDFs
.\.venv\Scripts\python.exe BookX_QuestionBank\scripts\compile_chapter_pdf.py --all

# Step 4: Build Consolidated Master Subject PDF
.\.venv\Scripts\python.exe BookX_QuestionBank\scripts\compile_master_book_pdf.py

# Step 5: Audit & Update Multi-Subject Trackers
.\.venv\Scripts\python.exe BookX_QuestionBank\scripts\update_project_trackers.py
```
