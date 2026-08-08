# 🧠 Root Workspace Brain — Multi-Subject Question Bank Ecosystem

> **Project Scope**: Standardized Multi-Subject Question Bank & PDF Compilation Engine for ICSE, CBSE & State Boards (Classes I to VIII + Future Grades & Subjects)  
> **Supported Subjects**: English, Mathematics, Science / EVS, Social Studies (History, Civics, Geography), Hindi, Computer Studies, General Knowledge  
> **Repository Root**: `s:\Question Bank making\`  
> **Virtual Environment**: `s:\Question Bank making\.venv\Scripts\python.exe`

---

## 🏛️ System Architecture & Dynamic Multi-Subject Engine

This workspace operates as a universal, scalable question bank generation engine capable of handling **all academic subjects** across primary and middle school grade levels. Every subject/book project follows an identical structural, metadata, and compilation blueprint.

```
s:\Question Bank making\
├── brain.md                         <-- Top-level workspace brain & system architecture (Multi-Subject)
├── master_prompt.md                 <-- Master root prompt directive & multi-subject generation rules
├── index.md                         <-- Top-level multi-subject workspace index & repository hub
├── progress.md                      <-- Top-level multi-subject progress dashboard & metrics
├── COMPREHENSION BOOK\              <-- Source textbook PDFs (All Subjects & Classes)
├── .venv\                           <-- Shared Python virtual environment
├── Book1_QuestionBank\              <-- Class I Question Bank Project (Multi-Subject)
├── Book2_QuestionBank\              <-- Class II Question Bank Project (Multi-Subject)
├── Book3_QuestionBank\              <-- Class III Question Bank Project (Multi-Subject)
├── Book4_QuestionBank\              <-- Class IV Question Bank Project (Completed English Baseline & Multi-Subject Extension)
├── Book5_QuestionBank\              <-- Class V Question Bank Project (Multi-Subject)
├── Book6_QuestionBank\              <-- Class VI Question Bank Project (Multi-Subject)
├── Book7_QuestionBank\              <-- Class VII Question Bank Project (Multi-Subject)
└── Book8_QuestionBank\              <-- Class VIII Question Bank Project (Multi-Subject)
```

---

## 📐 Universal Subject Taxonomies (6 Exam Categories per Chapter)

Each chapter in any subject contains **300 questions** organized into 6 category files (50 questions per file), tailored to the subject discipline:

### 1. English & Language Arts
1. `reading_comprehension.md` (50 Qs) — Section A Passage MCQs & Vocabulary
2. `guided_writing.md` (50 Qs) — Section B Paragraph frames, essays, letters & compositions
3. `grammar_language.md` (50 Qs) — Section C Grammar (Do as Directed, tenses, speech, prepositions)
4. `picture_based.md` (50 Qs) — Section D Visual observation, scene tasks & spot-the-error
5. `short_answer.md` (50 Qs) — Section D Item/character listing & textbook recall
6. `extract_stanza.md` (50 Qs) — Section D Reference to Context (RTC) prose & poem extracts

### 2. Mathematics & Quantitative Reasoning
1. `conceptual_mcqs.md` (50 Qs) — Section A Fundamentals, definitions, properties & MCQs
2. `mental_math_fillups.md` (50 Qs) — Section B Speed calculations, fill-in-blanks, true/false
3. `do_as_directed_math.md` (50 Qs) — Section C Direct evaluations, simplification, equations
4. `word_problems.md` (50 Qs) — Section D Real-world application word problems (step-by-step)
5. `visual_geometry_data.md` (50 Qs) — Section D Geometry shapes, graphs, tables, visual angles
6. `formulae_reasoning.md` (50 Qs) — Section D Assertion-reason, formula recall, short proofs

### 3. Science & EVS (Environmental Studies)
1. `objective_mcqs.md` (50 Qs) — Section A Concept MCQs, odd-one-out, match the following
2. `fillups_truefalse.md` (50 Qs) — Section B Key terminology, blanks, scientific statements
3. `short_definitions.md` (50 Qs) — Section C Give reasons, definitions, differentiate between
4. `diagram_based.md` (50 Qs) — Section D Label diagrams, process flowcharts, visual tasks
5. `long_answer_science.md` (50 Qs) — Section D Detailed scientific explanations & structures
6. `experiment_application.md` (50 Qs) — Section D Practical activities, observation scenarios

### 4. Social Studies (History, Civics, Geography)
1. `fact_chronology_mcqs.md` (50 Qs) — Section A Event dates, places, terms, objective MCQs
2. `terms_definitions.md` (50 Qs) — Section B Historical & geographical terminology blanks
3. `short_explanations.md` (50 Qs) — Section C 2–3 line conceptual answers & brief notes
4. `map_diagram_work.md` (50 Qs) — Section D Map identification, landform diagrams, symbols
5. `long_analytical.md` (50 Qs) — Section D Cause & effect, detailed history/civics answers
6. `source_extract_based.md` (50 Qs) — Section D Historical source extracts, case studies

---

## 🏷️ Universal Multi-Subject Metadata Schema

Every generated question in every subject MUST strictly conform to the unified metadata block format:

```markdown
### Question ID: BK{BookNum}_{SubCode}_CH{ChNum}_CAT{CatNum}_Q{QNum}
- **Subject**: [English | Mathematics | Science | EVS | Social Science | Hindi | Computer Studies | GK]
- **Type**: [MCQ | Numerical | Word Problem | Fill in the Blanks | Matching | Do As Directed | Short Answer | Long Answer | Diagram | RTC Extract]
- **Difficulty**: [Easy | Medium | Hard]
- **Bloom Level**: [Remembering | Understanding | Applying | Analyzing | Evaluating | Creating]
- **Topic**: [Specific Sub-topic / Concept Name]
- **Marks**: [1 | 2 | 3 | 5]

**Question**:
[Clear, precise question text. Uses LaTeX formatting like \( x^2 + y^2 = r^2 \) for Math/Science when applicable]

- (A) [Option A]
- (B) [Option B]
- (C) [Option C]
- (D) [Option D]

- **Answer Key**: **(Option Letter)** Full Explanation / Step-by-Step Solution / Model Answer
```

---

## ⚡ Automation & Multi-Subject Compilation Pipeline

All Python scripts operate dynamically regardless of the subject discipline:

1. **OCR Textbook Text Extraction**:
   ```powershell
   .\.venv\Scripts\python.exe BookX_QuestionBank\scripts\ocr_book_pdf.py
   ```
2. **Subject Question Generation**:
   ```powershell
   .\.venv\Scripts\python.exe BookX_QuestionBank\scripts\generate_chapter_questions.py --subject [ENG|MATH|SCI|SST|HIN|CS] --chapter XX
   ```
3. **ReportLab Chapter PDF Compilation**:
   ```powershell
   .\.venv\Scripts\python.exe BookX_QuestionBank\scripts\compile_chapter_pdf.py --all
   ```
4. **Master Book PDF Compilation**:
   ```powershell
   .\.venv\Scripts\python.exe BookX_QuestionBank\scripts\compile_master_book_pdf.py
   ```
5. **Multi-Subject Metric Audit**:
   ```powershell
   .\.venv\Scripts\python.exe BookX_QuestionBank\scripts\update_project_trackers.py
   ```
