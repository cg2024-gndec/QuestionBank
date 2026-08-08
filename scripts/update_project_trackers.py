r"""
=============================================================================
Script: update_project_trackers.py
Description: Updates index.md and progress.md metrics based on 6-category
             chapter question counts and compiled PDFs in Book4.
=============================================================================
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(BASE_DIR, "index.md")
PROGRESS_PATH = os.path.join(BASE_DIR, "progress.md")
QUESTION_BANK_DIR = os.path.join(BASE_DIR, "question_bank")

CATEGORIES = [
    "reading_comprehension.md",
    "guided_writing.md",
    "grammar_language.md",
    "picture_based.md",
    "short_answer.md",
    "extract_stanza.md"
]

def audit_project():
    completed_chapters = []
    total_questions = 0
    
    for ch_folder in sorted(os.listdir(QUESTION_BANK_DIR)):
        ch_path = os.path.join(QUESTION_BANK_DIR, ch_folder)
        if not os.path.isdir(ch_path) or not ch_folder.startswith("chapter_"):
            continue
            
        ch_num = ch_folder.replace("chapter_", "")
        ch_q_count = 0
        has_pdf = os.path.exists(os.path.join(ch_path, f"Chapter_{ch_num}_Question_Bank.pdf"))
        
        for q_file in CATEGORIES:
            f_path = os.path.join(ch_path, q_file)
            if os.path.exists(f_path):
                with open(f_path, "r", encoding="utf-8") as fh:
                    content = fh.read()
                q_count = content.count("### Question")
                ch_q_count += q_count
                
        if ch_q_count > 0:
            completed_chapters.append({
                "num": ch_num,
                "questions": ch_q_count,
                "has_pdf": has_pdf
            })
            total_questions += ch_q_count
            
    print(f"Audit Results: {len(completed_chapters)} completed chapters, {total_questions} total questions.")
    return completed_chapters, total_questions

def update_trackers(completed_chapters, total_questions):
    # Update progress.md
    with open(PROGRESS_PATH, "w", encoding="utf-8") as f:
        f.write(f"""# 📈 Book 4 Progress Tracker -- ICSE/CBSE Class IV English

> **Target**: 15 Chapters | 6 Exam-Aligned Categories | 50 Questions/File (300 Qs/Chapter) | Total Target: 4,500 Questions

---

## 📊 Summary Metrics

| Metric | Target | Current | Completion % |
|--------|-------:|--------:|-------------:|
| **Completed Chapters** | 15 | {len(completed_chapters)} | {len(completed_chapters)/15*100:.1f}% |
| **Total Questions** | 4,500 | {total_questions} | {total_questions/4500*100:.1f}% |
| **Category Scheme** | 6 CBSE Types | 6 Active | 100% |

---

## 📑 Chapter Progress Breakdown

| Chapter | Status | Questions Generated | PDF Compiled |
|---------|--------|-------------------:|:------------:|
""")
        for i in range(1, 16):
            ch_num = f"{i:02d}"
            ch_info = next((c for c in completed_chapters if c["num"] == ch_num), None)
            if ch_info:
                status = "✅ Complete" if ch_info["questions"] >= 300 else "⏳ In Progress"
                pdf_str = "✅ Yes" if ch_info["has_pdf"] else "⏳ Pending"
                f.write(f"| Chapter {ch_num} | {status} | {ch_info['questions']} | {pdf_str} |\n")
            else:
                f.write(f"| Chapter {ch_num} | ⏳ Pending | 0 | ⏳ Pending |\n")

    # Update index.md
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(f"""# 🗂️ Book 4 Index -- ICSE/CBSE Class IV English

> **Structure**: 15 Chapters × 6 Exam Categories × 50 Questions = 4,500 Total Questions

---

## 📋 Exam-Aligned Question Taxonomy (6 Categories)

1. `reading_comprehension.md` -- Section A Passage MCQs (50 Qs)
2. `guided_writing.md` -- Section B Guided Paragraph/Description (50 Qs)
3. `grammar_language.md` -- Section C Do as Directed Grammar (50 Qs)
4. `picture_based.md` -- Section D Q7 Picture & Visual Tasks (50 Qs)
5. `short_answer.md` -- Section D Q8/Q9 Short Answer Listing (50 Qs)
6. `extract_stanza.md` -- Section D Q10 Extract & Stanza Analysis (50 Qs)

---

## 📚 Chapter Directory

""")
        for i in range(1, 16):
            ch_num = f"{i:02d}"
            ch_info = next((c for c in completed_chapters if c["num"] == ch_num), None)
            q_cnt = ch_info["questions"] if ch_info else 0
            f.write(f"- [Chapter {ch_num}](file:///{BASE_DIR.replace('\\', '/')}/question_bank/chapter_{ch_num}) -- {q_cnt} Questions\n")

if __name__ == "__main__":
    ch_list, total_q = audit_project()
    update_trackers(ch_list, total_q)
    print("Trackers updated successfully.")
