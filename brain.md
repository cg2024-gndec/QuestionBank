# 🧠 Question Bank Intelligence & Taxonomy (brain.md)
# CBSE/ICSE Board Perspective — Class IV English

> This document defines the intelligence, standards, taxonomy, metadata, and generation rules for the entire Class IV English Question Bank project.
> **Reference**: CBSE Class 4 English Sample Paper (Set 1, 60 Marks, 4 Sections) — actual exam pattern.
> Every chapter, every category file, and every generated question must follow these rules without exception.

---

# Project Objective

Create a high-quality, exam-aligned, comprehensive Question Bank for Class IV English that:

- Mirrors the **exact question types** found in actual CBSE/ICSE Class IV English examinations.
- Covers every chapter's concepts, characters, vocabulary, grammar, and themes.
- Maintains high linguistic precision and age-appropriate sophistication for Class IV students (8–10 years).
- Supports multiple cognitive difficulty levels based on Bloom's Taxonomy.
- Enables automatic generation of unlimited, balanced, non-duplicative sample papers.

---

# Exam Pattern (Source: CBSE Class 4 English Sample Paper)

| Section | Name | Marks | Question Style |
|---------|------|------:|----------------|
| **Section A** | Reading Comprehension | 16 | 2 passages × 4 MCQs each (2M each) |
| **Section B** | Writing Skills | 12 | Guided paragraph (6 sentences) + Guided description (6 sentences) |
| **Section C** | Grammar & Language | 12 | Do as Directed — degrees, conjunctions, spelling, antonyms, synonyms, question words |
| **Section D** | Textbook-Based | 20 | Picture questions + Short answers (list 4 items) + Extract/Stanza analysis |
| **Total** | | **60** | |

---

# 6-Category Question Taxonomy (Exam-Aligned)

Every chapter question bank contains questions across exactly **6 categories** (50 questions each = 300 per chapter):

| # | Category | File Name | Exam Section | Format Description |
|---|----------|-----------|-------------|---------------------|
| 1 | **Reading Comprehension** | `reading_comprehension.md` | Section A | Short passage (4–8 sentences) followed by 4 MCQs: factual recall, vocabulary meaning, antonym/synonym in context, odd-one-out OR best title |
| 2 | **Guided Writing** | `guided_writing.md` | Section B | 6-sentence paragraph frames with sentence starters / keyword prompts / descriptive writing tasks with blanks |
| 3 | **Grammar & Language** | `grammar_language.md` | Section C | Do as Directed: degrees of comparison table, join with conjunctions, fill missing letters, circle question word, write opposite, write similar word, correct spelling |
| 4 | **Picture-Based Questions** | `picture_based.md` | Section D (Q7) | Frame "How many..." questions from described scene, observe and describe, correct spelling, visual storytelling |
| 5 | **Short Answer Questions** | `short_answer.md` | Section D (Q8,Q9) | List 4 items/names/places/creatures from text or poem; 1–3 sentence textbook/poem-based answers |
| 6 | **Extract & Stanza Analysis** | `extract_stanza.md` | Section D (Q10) | Short prose/poem extract with sub-questions: rhyming word pairs, poet's message/intent, character details (list 4), stanza meaning |

---

# Difficulty Levels & Bloom's Mapping (CBSE Standard)

| Level | Percentage | Cognitive Level | Target Question Types |
|-------|:----------:|----------------|-----------------------|
| **Easy** | **40%** | Remember, Understand | Direct MCQs, factual recall, list items, fill frames |
| **Medium** | **40%** | Apply, Understand | Grammar transformations, vocabulary in context, guided composition |
| **Hard / HOTS** | **20%** | Analyze, Evaluate, Create | Best title inference, poet's intent, character analysis, antonym/synonym in context |

---

# Metadata Schema for Every Question

Every generated question MUST include the following metadata block:

```markdown
### Question [N]
- **Question ID**: CH[XX]-[TYPE]-[NNN]
- **Type**: [RC / GW / GL / PB / SA / ES]
- **Difficulty**: [Easy / Medium / Hard / HOTS]
- **Bloom Level**: [Remember / Understand / Apply / Analyze / Evaluate / Create]
- **Topic**: [Specific topic / sub-skill]
- **Marks**: [1 / 2 / 6]
- **Question**: [Exact question text]
- **Answer Key / Model Answer**: [Full answer with explanation]
```

Question ID Prefixes:
- `CHXX-RC-NNN` — Reading Comprehension
- `CHXX-GW-NNN` — Guided Writing
- `CHXX-GL-NNN` — Grammar & Language
- `CHXX-PB-NNN` — Picture-Based
- `CHXX-SA-NNN` — Short Answer
- `CHXX-ES-NNN` — Extract & Stanza

---

# Specific Generation Rules Per Category

## 1. Reading Comprehension (`reading_comprehension.md`)
- Write a **4–8 sentence passage** based on chapter content OR use chapter extract.
- Follow with exactly **4 MCQs** (A, B, C, D options):
  1. Factual recall ("What did...?", "Where did...?")
  2. Vocabulary meaning in context ("What is the meaning of '___'?")
  3. Antonym/Synonym in context ("Which word in the passage is opposite of '___'?")
  4. Odd-one-out OR best title selection
- Each set of passage + 4 MCQs counts as **4 questions** (Q IDs: RC-001 through RC-004 for first set, RC-005 through RC-008 for second, etc.)
- Total: 50 questions = ~12–13 passage sets

## 2. Guided Writing (`guided_writing.md`)
- Provide exactly **6 sentence frames** with blanks or keyword prompts.
- Topics drawn from chapter themes (characters, events, values, objects in chapter).
- Format: Guided paragraph (Myself / Character / Event) OR Guided description (Object / Place / Animal from chapter).
- Include a **Model Answer** showing completed sentences.
- Each full writing task = **1 question** entry (marks = 6).

## 3. Grammar & Language (`grammar_language.md`)
- Strictly follow CBSE Class IV Grammar:
  - **Degrees of Comparison**: Fill the table (Positive / Comparative / Superlative)
  - **Conjunctions**: Join pairs of sentences using and / but / because / so
  - **Missing Letters**: Complete the word (e.g., `SCR_ _M` → SCREAM)
  - **Question Words**: Circle the question word in given sentences
  - **Antonyms**: Write opposite of given word
  - **Synonyms**: Write a similar word for given word
  - **Spelling Correction**: Rewrite the sentence with correct spelling
- Each individual task = **1 question** (marks = 2).

## 4. Picture-Based Questions (`picture_based.md`)
- Describe a visual scene from chapter context.
- Ask: "Frame a question using **How many**" from the scene.
- Ask: "Write **two sentences** describing what you see."
- Include: Spot the spelling mistake in a sentence, rewrite correctly.
- Visual prompts should tie to chapter events, characters, settings.

## 5. Short Answer Questions (`short_answer.md`)
- Textbook/Poem-based recall questions requiring **list of 4 items**.
- Format: "Name any four ___." / "List four ___ mentioned in the text."
- OR: 1–3 sentence answers to "What...?", "Who...?", "How...?" about chapter content.
- Each question = **1–2 marks**.

## 6. Extract & Stanza Analysis (`extract_stanza.md`)
- Provide a **3–5 line extract** from the chapter (prose or poem stanza).
- Follow with sub-questions:
  (a) Write a pair of **rhyming words** from the extract (for poems).
  (b) What does the poet/author want us to understand? (1 sentence)
  (c) List **4 details** about a character/event from the extract.
  (d) What is the meaning of '___' as used in the extract?
- Each extract set = **1 question entry** (marks = 4).

---

# Quality Standards

- **Accuracy > Rigor > Educational Value > Originality > Formatting**
- Never sacrifice quality for quantity.
- Every question must test a **distinct skill** — no duplicates.
- All answer keys must be **complete, correct, and clearly explained**.
- Language must be **age-appropriate** for Class IV students (8–10 years).

---

# Chapter Completion Rule

A chapter is COMPLETE only when:
✓ Chapter text analyzed & concepts extracted
✓ All **6 category files** generated with **50 questions each** (300 total)
✓ Duplicate check & quality review completed
✓ Styled PDF compiled (`Chapter_XX_Question_Bank.pdf`)
✓ `update_project_trackers.py` executed successfully
✓ `progress.md` and `index.md` updated

---

# Decision Hierarchy

1. `brain.md` (Highest Priority)
2. `paper_blueprint.md`
3. `progress.md`
4. `index.md`
5. Chapter Source Content

---

# Golden Rule

Think like an experienced CBSE examiner setting real papers for Class IV students.
Every question should match the **exact style, format, and difficulty** of actual exam questions while evaluating deep comprehension, language accuracy, and critical thinking.