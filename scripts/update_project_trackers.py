r"""
=============================================================================
Script: update_project_trackers.py
Description: Updates index.md and progress.md metrics based on chapter 
             question counts and compiled PDFs.
Usage: .\.venv\Scripts\python.exe QuestionBank\scripts\update_project_trackers.py
=============================================================================
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(BASE_DIR, "index.md")
PROGRESS_PATH = os.path.join(BASE_DIR, "progress.md")
QUESTION_BANK_DIR = os.path.join(BASE_DIR, "question_bank")

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
        
        for q_file in ["mcq.md", "fillups.md", "true_false.md", "short.md", "long.md", "vocabulary.md", "grammar.md", "extract_based.md", "case_based.md", "picture_based.md"]:
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

if __name__ == "__main__":
    audit_project()
