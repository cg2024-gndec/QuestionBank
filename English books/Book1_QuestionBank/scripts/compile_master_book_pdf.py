r"""
=============================================================================
Script: compile_master_book_pdf.py
Description: Master ReportLab PDF compiler for Book 1 (Class I English).
             Stitches all 15 chapters (4,500 questions) into a single,
             publication-ready master PDF complete with cover page,
             Table of Contents, chapter divider banners, and running headers.
=============================================================================
"""

import os
import sys
import re
import argparse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, PageBreak, Table, TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUESTION_BANK_DIR = os.path.join(BASE_DIR, "question_bank")
OUTPUT_PDF_PATH = os.path.join(BASE_DIR, "Book1_Master_Question_Bank.pdf")

CHAPTER_INFO = [
    {"num": "01", "title": "The Monkey and the Crocodile", "qs": 300},
    {"num": "02", "title": "The Stork and the Crab", "qs": 300},
    {"num": "03", "title": "The Elephants and the Mice", "qs": 300},
    {"num": "04", "title": "Invention of 'The Popsicle'", "qs": 300},
    {"num": "05", "title": "Father of the Nation", "qs": 300},
    {"num": "06", "title": "My Favourite Cartoon", "qs": 300},
    {"num": "07", "title": "Our National Animal", "qs": 300},
    {"num": "08", "title": "The Ganga River", "qs": 300},
    {"num": "09", "title": "Sunflower", "qs": 300},
    {"num": "10", "title": "The Animal Store", "qs": 300},
    {"num": "11", "title": "At the Zoo", "qs": 300},
    {"num": "12", "title": "Furry Bear", "qs": 300},
    {"num": "13", "title": "The Boy and the Bird", "qs": 300},
    {"num": "14", "title": "The Lion and the Mouse", "qs": 300},
    {"num": "15", "title": "Picture Story: Kindness to Animals", "qs": 300},
]

class MasterNumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        if self._pageNumber == 1:
            return # Skip cover page
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor('#6B7280'))
        
        self.drawString(36, 762, "CBSE / ICSE Class I English -- Master Question Bank")
        self.setStrokeColor(colors.HexColor('#E5E7EB'))
        self.setLineWidth(0.5)
        self.line(36, 756, 576, 756)
            
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(576, 25, page_str)
        self.drawString(36, 25, "Confidential & Proprietary -- Class I Question Bank Series")
        self.setStrokeColor(colors.HexColor('#E5E7EB'))
        self.setLineWidth(0.5)
        self.line(36, 36, 576, 36)
        
        self.restoreState()

def md_to_reportlab_tags(text):
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
    text = re.sub(r'`(.*?)`', r'<font name="Courier">\1</font>', text)
    return text

def build_master_pdf():
    print(f"Building Consolidated Master Book PDF -> {OUTPUT_PDF_PATH}...")
    
    styles = getSampleStyleSheet()
    custom_styles = {
        'CoverTitle': ParagraphStyle('CoverTitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=26, leading=32, textColor=colors.HexColor('#0F172A'), alignment=1, spaceAfter=8),
        'CoverSubtitle': ParagraphStyle('CoverSubtitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=14, leading=18, textColor=colors.HexColor('#2563EB'), alignment=1, spaceAfter=20),
        'CoverMeta': ParagraphStyle('CoverMeta', parent=styles['Normal'], fontName='Helvetica', fontSize=11, leading=16, textColor=colors.HexColor('#475569'), alignment=1, spaceAfter=8),
        'TOCTitle': ParagraphStyle('TOCTitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=18, leading=22, textColor=colors.HexColor('#1E3A8A'), spaceBefore=10, spaceAfter=12),
        'TOCItem': ParagraphStyle('TOCItem', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=10, leading=14, textColor=colors.HexColor('#1E293B')),
        'TOCDetail': ParagraphStyle('TOCDetail', parent=styles['Normal'], fontName='Helvetica', fontSize=9, leading=12, textColor=colors.HexColor('#64748B')),
        'ChBanner': ParagraphStyle('ChBanner', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=22, leading=26, textColor=colors.HexColor('#0F172A'), alignment=1, spaceBefore=20, spaceAfter=8),
        'ChBannerSub': ParagraphStyle('ChBannerSub', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=12, leading=16, textColor=colors.HexColor('#2563EB'), alignment=1, spaceAfter=15),
        'H1': ParagraphStyle('H1', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=15, leading=19, textColor=colors.HexColor('#1E3A8A'), spaceBefore=12, spaceAfter=6),
        'H2': ParagraphStyle('H2', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=12.5, leading=16, textColor=colors.HexColor('#1D4ED8'), spaceBefore=10, spaceAfter=4),
        'H3': ParagraphStyle('H3', parent=styles['Heading3'], fontName='Helvetica-Bold', fontSize=10.5, leading=14.5, textColor=colors.HexColor('#0F172A'), spaceBefore=8, spaceAfter=3),
        'Body': ParagraphStyle('BodyTextCustom', parent=styles['Normal'], fontName='Helvetica', fontSize=9, leading=13, textColor=colors.HexColor('#334155'), spaceAfter=4),
        'Blockquote': ParagraphStyle('BlockquoteCustom', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=9, leading=13, textColor=colors.HexColor('#1E293B'), backColor=colors.HexColor('#F1F5F9'), borderColor=colors.HexColor('#CBD5E1'), borderWidth=0.5, borderPadding=6, spaceAfter=6),
        'Metadata': ParagraphStyle('MetadataCustom', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=11.5, textColor=colors.HexColor('#475569'), leftIndent=10, spaceAfter=2),
        'Option': ParagraphStyle('OptionCustom', parent=styles['Normal'], fontName='Helvetica', fontSize=9, leading=12.5, textColor=colors.HexColor('#1E293B'), leftIndent=20, spaceAfter=2),
        'AnswerKey': ParagraphStyle('AnswerKeyCustom', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, leading=12, textColor=colors.HexColor('#15803D'), backColor=colors.HexColor('#DCFCE7'), borderColor=colors.HexColor('#86EFAC'), borderWidth=0.5, borderPadding=4, spaceBefore=3, spaceAfter=6, leftIndent=10),
    }

    doc = SimpleDocTemplate(
        OUTPUT_PDF_PATH,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=45,
        bottomMargin=45
    )

    story = []

    # COVER PAGE
    story.append(Spacer(1, 100))
    story.append(Paragraph("ICSE &amp; CBSE CLASS I ENGLISH", custom_styles['CoverSubtitle']))
    story.append(Paragraph("MASTER QUESTION BANK", custom_styles['CoverTitle']))
    story.append(HRFlowable(width="80%", thickness=3, color=colors.HexColor('#1E3A8A'), spaceBefore=10, spaceAfter=25))
    story.append(Paragraph("<b>15 Complete Chapters | 6 Exam Categories | 4,500 Total Questions</b>", custom_styles['CoverMeta']))
    story.append(Paragraph("Aligned with CISCE &amp; CBSE Curriculum Standards for Primary Class 1 English", custom_styles['CoverMeta']))
    story.append(Spacer(1, 140))
    story.append(Paragraph("<b>Includes:</b> MCQs | Fill in the Blanks | Story Fillups | True/False | Short Questions | Long Questions", custom_styles['CoverMeta']))
    story.append(Paragraph("<b>Publication Edition</b>: 2026-2027 Master Reference Volume 1", custom_styles['CoverMeta']))
    story.append(PageBreak())

    # TABLE OF CONTENTS
    story.append(Paragraph("TABLE OF CONTENTS", custom_styles['TOCTitle']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1E3A8A'), spaceAfter=15))

    toc_data = [
        [Paragraph("<b>Chapter</b>", custom_styles['TOCItem']), Paragraph("<b>Chapter Title</b>", custom_styles['TOCItem']), Paragraph("<b>Questions</b>", custom_styles['TOCItem']), Paragraph("<b>Categories Covered</b>", custom_styles['TOCItem'])]
    ]

    for ch in CHAPTER_INFO:
        toc_data.append([
            Paragraph(f"<b>Ch {ch['num']}</b>", custom_styles['TOCItem']),
            Paragraph(f"<b>{ch['title']}</b>", custom_styles['TOCItem']),
            Paragraph(f"{ch['qs']} Qs", custom_styles['TOCDetail']),
            Paragraph("6 Categories (MCQs to Long Qs)", custom_styles['TOCDetail'])
        ])

    toc_table = Table(toc_data, colWidths=[50, 200, 70, 220], hAlign='LEFT')
    toc_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E3A8A')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(toc_table)
    story.append(PageBreak())

    files_order = [
        ("1. Multiple Choice Questions (MCQs)", "mcqs.md"),
        ("2. Fill in the Blanks", "fill_in_the_blanks.md"),
        ("3. Fill in the Blanks from Story", "fill_in_blanks_story.md"),
        ("4. True / False Questions", "true_false.md"),
        ("5. Short Answer Questions", "short_answer.md"),
        ("6. Long Answer Questions", "long_answer.md")
    ]

    for ch in CHAPTER_INFO:
        ch_num = ch["num"]
        ch_dir = os.path.join(QUESTION_BANK_DIR, f"chapter_{ch_num}")
        if not os.path.exists(ch_dir):
            continue

        story.append(Spacer(1, 20))
        story.append(Paragraph(f"CHAPTER {ch_num}", custom_styles['ChBannerSub']))
        story.append(Paragraph(f"{ch['title'].upper()}", custom_styles['ChBanner']))
        story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#1E3A8A'), spaceBefore=10, spaceAfter=20))
        story.append(Paragraph("<b>Section Overview:</b> 300 Questions across 6 Standardized Categories", custom_styles['CoverMeta']))
        story.append(PageBreak())

        for cat_title, filename in files_order:
            filepath = os.path.join(ch_dir, filename)
            if not os.path.exists(filepath):
                continue
                
            story.append(Paragraph(f"Ch {ch_num}: {cat_title}", custom_styles['H1']))
            story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#1E3A8A'), spaceAfter=8))
            
            with open(filepath, "r", encoding="utf-8") as f:
                lines = f.readlines()
                
            for line in lines:
                stripped = line.strip()
                if not stripped or stripped.startswith("# ") or stripped == "---":
                    continue
                if stripped.startswith("### "):
                    story.append(Paragraph(md_to_reportlab_tags(stripped[4:]), custom_styles['H3']))
                elif stripped.startswith(">"):
                    story.append(Paragraph(md_to_reportlab_tags(stripped.lstrip("> ")), custom_styles['Blockquote']))
                elif stripped.startswith("- **Answer Key"):
                    story.append(Paragraph(md_to_reportlab_tags(stripped), custom_styles['AnswerKey']))
                elif stripped.startswith("- **Question ID") or stripped.startswith("- **"):
                    story.append(Paragraph(md_to_reportlab_tags(stripped), custom_styles['Metadata']))
                elif stripped.startswith("- (") or stripped.startswith("  - ("):
                    story.append(Paragraph(md_to_reportlab_tags(stripped.lstrip(" -")), custom_styles['Option']))
                else:
                    story.append(Paragraph(md_to_reportlab_tags(stripped), custom_styles['Body']))
                    
            story.append(Spacer(1, 10))

    doc.build(story, canvasmaker=MasterNumberedCanvas)
    print(f"[SUCCESS] Consolidated Master Book PDF generated: {OUTPUT_PDF_PATH}")

if __name__ == "__main__":
    build_master_pdf()
