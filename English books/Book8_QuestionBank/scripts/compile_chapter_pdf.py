r"""
=============================================================================
Script: compile_chapter_pdf.py
Description: ReportLab PDF compilation tool that binds all 10 category files 
             of a chapter into a styled, professional 50+ page PDF document 
             (Chapter_XX_Question_Bank.pdf).
Usage: .\.venv\Scripts\python.exe QuestionBank\scripts\compile_chapter_pdf.py --chapter 01
=============================================================================
"""

import os
import sys
import argparse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUESTION_BANK_DIR = os.path.join(BASE_DIR, "question_bank")

def compile_pdf(chapter_num):
    ch_dir = os.path.join(QUESTION_BANK_DIR, f"chapter_{chapter_num}")
    output_pdf = os.path.join(ch_dir, f"Chapter_{chapter_num}_Question_Bank.pdf")
    
    if not os.path.exists(ch_dir):
        print(f"Error: Chapter directory does not exist: {ch_dir}")
        sys.exit(1)
        
    # Order of 10 Category Files
    files_order = [
        ("1. Multiple Choice Questions (MCQs)", "mcq.md"),
        ("2. Fill in the Blanks (Fillups)", "fillups.md"),
        ("3. True or False Statements", "true_false.md"),
        ("4. Short Answer Questions", "short.md"),
        ("5. Long Answer & HOTS Questions", "long.md"),
        ("6. Vocabulary & Word Power", "vocabulary.md"),
        ("7. Grammar & Language Skills", "grammar.md"),
        ("8. Extract & Passage Based Questions", "extract_based.md"),
        ("9. Case & Scenario Based Questions", "case_based.md"),
        ("10. Picture & Visual Based Questions", "picture_based.md")
    ]
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=colors.HexColor('#1E3A8A'),
        alignment=1,
        spaceAfter=6
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Heading2'],
        fontName='Helvetica',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#2563EB'),
        alignment=1,
        spaceAfter=15
    )

    section_heading_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#1E3A8A'),
        spaceBefore=12,
        spaceAfter=8,
        keepWithNext=True
    )

    q_title_style = ParagraphStyle(
        'QTitle',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#0F172A'),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'QBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#334155'),
        spaceAfter=4
    )

    meta_style = ParagraphStyle(
        'QMeta',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#64748B'),
        spaceAfter=4
    )

    ans_style = ParagraphStyle(
        'QAns',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor('#166534'),
        spaceBefore=2,
        spaceAfter=6
    )

    def add_header_footer(canvas, doc_obj):
        canvas.saveState()
        canvas.setFont("Helvetica-Bold", 8)
        canvas.setFillColor(colors.HexColor('#64748B'))
        canvas.drawString(54, 750, f"CLASS IV ENGLISH QUESTION BANK — CHAPTER {chapter_num}")
        canvas.setStrokeColor(colors.HexColor('#E2E8F0'))
        canvas.setLineWidth(0.5)
        canvas.line(54, 742, 558, 742)
        
        canvas.line(54, 45, 558, 45)
        canvas.setFont("Helvetica", 8)
        canvas.drawString(54, 32, "Confidential - Comprehensive 10-Category Question Bank")
        canvas.drawRightString(558, 32, f"Page {doc_obj.page}")
        canvas.restoreState()

    doc_obj = SimpleDocTemplate(
        output_pdf,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    story = []
    story.append(Spacer(1, 10))
    story.append(Paragraph("📚 CLASS IV ENGLISH QUESTION BANK", title_style))
    story.append(Paragraph(f"CHAPTER {chapter_num} QUESTION BANK (250 QUESTIONS)", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#2563EB'), spaceAfter=15))

    summary_data = [
        [Paragraph("<b>Subject:</b> English", body_style), Paragraph("<b>Class:</b> IV", body_style)],
        [Paragraph(f"<b>Chapter:</b> {chapter_num}", body_style), Paragraph("<b>Total Questions:</b> 250 (25 per category across 10 files)", body_style)],
        [Paragraph("<b>Source:</b> Praxis Comprehension & Composition 4", body_style), Paragraph("<b>Board / Blueprint:</b> ICSE Class IV English Pattern", body_style)]
    ]
    t = Table(summary_data, colWidths=[250, 250])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t)
    story.append(Spacer(1, 15))

    for title, filename in files_order:
        file_path = os.path.join(ch_dir, filename)
        if not os.path.exists(file_path):
            continue
            
        story.append(Paragraph(title, section_heading_style))
        story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#94A3B8'), spaceAfter=10))
        
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
        for line in lines:
            line_str = line.strip().replace("<br>", "<br/>")
            if not line_str or line_str.startswith("# ") or line_str == "---":
                continue
                
            if line_str.startswith("### Question"):
                story.append(Paragraph(line_str.replace("### ", ""), q_title_style))
            elif line_str.startswith("- **Question ID**:") or line_str.startswith("- **Difficulty**:") or line_str.startswith("- **Bloom Level**:") or line_str.startswith("- **Topic**:") or line_str.startswith("- **Marks**:") or line_str.startswith("- **Type**"):
                clean_meta = line_str.replace("- **", "").replace("**:", ": ")
                story.append(Paragraph(f"<i>{clean_meta}</i>", meta_style))
            elif line_str.startswith("- **Question**:") or line_str.startswith("- **Statement**:") or line_str.startswith("- **Case / Scenario**:") or line_str.startswith("- **Visual Prompt**:") or line_str.startswith("> **Reading Context**"):
                q_text = line_str.replace("- **Question**:", "<b>Question:</b>").replace("- **Statement**:", "<b>Statement:</b>").replace("- **Case / Scenario**:", "<b>Case / Scenario:</b>").replace("- **Visual Prompt**:", "<b>Visual Prompt:</b>")
                story.append(Paragraph(q_text, body_style))
            elif line_str.startswith("  - (A)") or line_str.startswith("  - (B)") or line_str.startswith("  - (C)") or line_str.startswith("  - (D)"):
                opt_text = line_str.strip().replace("- ", "")
                story.append(Paragraph(f"&nbsp;&nbsp;&nbsp;&nbsp;{opt_text}", body_style))
            elif line_str.startswith("- **Model Answer**:") or line_str.startswith("- **Answer Key**:") or line_str.startswith("- **Expected Answer**:") or line_str.startswith("- **Model Answer / Key**:") or line_str.startswith("| **CH"):
                ans_text = line_str.replace("- **Model Answer**:", "<b>Model Answer:</b>").replace("- **Answer Key**:", "<b>Answer Key:</b>").replace("- **Model Answer / Key**:", "<b>Model Answer / Key:</b>")
                story.append(Paragraph(ans_text, ans_style))
            elif line_str.startswith("| Question ID") or line_str.startswith("|-------------"):
                continue
            else:
                story.append(Paragraph(line_str, body_style))
                
        story.append(Spacer(1, 15))
        story.append(PageBreak())

    doc_obj.build(story, onFirstPage=add_header_footer, onLaterPages=add_header_footer)
    print(f"SUCCESS: PDF generated -> {output_pdf}")

def main():
    parser = argparse.ArgumentParser(description="Compile Chapter Question Bank Markdown files into a PDF.")
    parser.add_argument("--chapter", type=str, default="01", help="Chapter number (e.g. 01, 02)")
    args = parser.parse_args()
    compile_pdf(args.chapter)

if __name__ == "__main__":
    main()
