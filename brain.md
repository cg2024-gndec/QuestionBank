# 🧠 Question Bank Intelligence & Taxonomy (brain.md) - ICSE Board Perspective

> This document defines the intelligence, standards, taxonomy, metadata, and generation rules for the entire Class IV English Question Bank project aligned with **ICSE (CISCE)** curriculum guidelines.  
> Every chapter, every category file, and every generated question must follow these rules without exception.

---

# Project Objective

Create a high-quality, ICSE-aligned, comprehensive Question Bank for Class IV English that:

- Covers every concept, vocabulary word, character, event, poem stanza, and moral from every chapter.
- Incorporates ICSE-style question types (**Reference to Context - RTC**, **Do as Directed Grammar Transformations**, **Case & Real-World Scenario Analysis**, **Picture & Visual Observation**, and **Guided Composition**).
- Maintains high linguistic precision and age-appropriate sophistication for ICSE Class IV students (8–10 years).
- Supports multiple cognitive difficulty levels based on Bloom's Taxonomy.
- Enables automatic generation of unlimited, balanced, non-duplicative 60–80 mark ICSE sample papers.

---

# Comprehensive ICSE Question Taxonomy

Every chapter question bank contains questions across the following **10 Core Categories**:

| Category | File Name | ICSE Format & Purpose Description |
|----------|-----------|----------------------------------|
| **MCQ** | `mcq.md` | Multiple Choice Questions with 4 options (A, B, C, D) testing factual recall, vocabulary, and literary details. |
| **Fill in the Blanks** | `fillups.md` | Single-blank sentence completion testing text accuracy, grammar terms, and key concepts. |
| **True / False** | `true_false.md` | Statement validation with detailed justifications in answer keys. |
| **Short Answer** | `short.md` | Concise 2-mark questions requiring 1–3 sentence ICSE-standard answers. |
| **Long Answer & HOTS** | `long.md` | 5-mark extended responses, character comparisons, moral dilemmas, and theme analysis. |
| **Vocabulary & Word Power** | `vocabulary.md` | Meanings, antonyms, synonyms, homophones, idioms, word formation (prefixes/suffixes), spelling corrections, and dictionary order. |
| **Grammar & Language Skills** | `grammar.md` | ICSE "Do as Directed": Nouns (Common, Proper, Collective, Abstract), Pronouns, Adjectives (Degrees), Verbs & Tenses, Adverbs, Prepositions, Conjunctions, Articles, Direct/Indirect Speech, Sentence Transformation, Punctuation. |
| **Extract / Passage Based (RTC)** | `extract_based.md` | **ICSE Reference to Context (RTC)**: Prose/Poem extracts followed by sub-questions (speaker, context, vocabulary, line meaning, character motive). |
| **Case / Scenario Based** | `case_based.md` | Real-life situational analysis, moral choice evaluation, value-based decisions, and practical student scenarios. |
| **Picture / Visual Based** | `picture_based.md` | Image observation, question framing (*"How many..."*), visual storytelling, object description, and scene analysis. |

---

# Difficulty Levels & Bloom's Mapping (ICSE Standard)

Every chapter maintains a balanced cognitive difficulty distribution:

| Level | Percentage | Cognitive Level (Bloom's) | Target Question Types |
|-------|:----------:|---------------------------|-----------------------|
| **Easy** | **35%** | Remember, Understand | Direct MCQs, Fillups, Spelling, Antonyms, Simple True/False |
| **Medium** | **40%** | Apply, Understand | Grammar transformations, Conjunctions, Degrees of comparison, Short Answers, RTC direct recall |
| **Hard** | **15%** | Analyze, Evaluate | Character comparison, RTC contextual inference, Homophones, Vocabulary nuances |
| **HOTS** | **10%** | Evaluate, Create | Case-based scenarios, Moral reasoning, Creative writing, Long Answers |

---

# Metadata Schema for Every Question

Every generated question MUST include the following metadata block:

```markdown
### Question [N]
- **Question ID**: CH[XX]-[TYPE]-[NNN]
- **Type**: [MCQ / Fillups / True_False / Short / Long / Vocabulary / Grammar / Extract_Based / Case_Based / Picture_Based]
- **Difficulty**: [Easy / Medium / Hard / HOTS]
- **Bloom Level**: [Remember / Understand / Apply / Analyze / Evaluate / Create]
- **Topic**: [Topic / Sub-concept]
- **Marks**: [1 / 2 / 5]
- **Question**: [Exact question text]
- **Answer Key / Model Answer**: [Full answer with explanation]
```

Question ID Prefixes:
- `CHXX-MCQ-NNN`
- `CHXX-FIL-NNN`
- `CHXX-TF-NNN`
- `CHXX-SA-NNN`
- `CHXX-LA-NNN`
- `CHXX-VOC-NNN`
- `CHXX-GRA-NNN`
- `CHXX-EXT-NNN` (Reference to Context / RTC)
- `CHXX-CAS-NNN` (Case / Scenario Based)
- `CHXX-PIC-NNN` (Picture / Visual Based)

---

# Specific Generation Rules for ICSE Alignment

## 1. Extract / Passage Based Questions (`extract_based.md`)
- Provide a 4–6 sentence prose or poem extract (Reference to Context).
- Include sub-questions testing:
  1. *Who said this to whom? / Where is this taking place?* (Context & Speaker)
  2. Direct factual recall from extract.
  3. Contextual vocabulary meaning or antonym/synonym in context.
  4. Character emotion / intent / motive.
  5. Title / Theme / Moral inference.

## 2. Grammar & Language Skills (`grammar.md`)
- Strictly follow ICSE Class IV Grammar syllabus:
  - **Nouns**: Proper, Common, Collective, Abstract
  - **Adjectives**: Quality, Quantity, Number, Degrees of Comparison
  - **Verbs & Tenses**: Simple Present, Simple Past, Present Continuous, Past Continuous
  - **Adverbs**: Manner, Time, Place
  - **Prepositions & Conjunctions**: Correct usage and sentence joining
  - **Articles**: A, An, The
  - **Punctuation & Direct/Indirect Speech**

## 3. Case / Scenario Based Questions (`case_based.md`)
- Present real-life student scenarios related to the chapter's core values (honesty, presence of mind, choosing good friends, perseverance).
- Ask students to apply critical thinking and evaluate choices.

## 4. Picture / Visual Based Questions (`picture_based.md`)
- Include visual observation prompts, question framing, object descriptions, and scene sequencing.