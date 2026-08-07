r"""
=============================================================================
Script: compile_master_book_pdf.py
Description: Master ReportLab PDF compiler for Book 4 (Class IV English).
             Stitches all 15 chapters (4,472 questions) into a single,
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
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, PageBreak, Table, TableStyle, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUESTION_BANK_DIR = os.path.join(BASE_DIR, "question_bank")
OUTPUT_PDF_PATH = os.path.join(BASE_DIR, "Book4_Master_Question_Bank.pdf")

CHAPTER_INFO = [
    {"num": "01", "title": "Empty Pot", "qs": 300},
    {"num": "02", "title": "The Cave that Talked", "qs": 272},
    {"num": "03", "title": "The King and the Foolish Monkey", "qs": 300},
    {"num": "04", "title": "Beginnings of Traffic Lights", "qs": 300},
    {"num": "05", "title": "The Telephone", "qs": 300},
    {"num": "06", "title": "Swar Kokila: Lata Mangeshkar", "qs": 300},
    {"num": "07", "title": "Sachin Tendulkar", "qs": 300},
    {"num": "08", "title": "Bhagat Singh", "qs": 300},
    {"num": "09", "title": "About Garba", "qs": 300},
    {"num": "10", "title": "Boat Races Festival Kerala", "qs": 300},
    {"num": "11", "title": "Lifecycle of a Frog", "qs": 300},
    {"num": "12", "title": "Kaveri", "qs": 300},
    {"num": "13", "title": "Spring", "qs": 300},
    {"num": "14", "title": "Be Kind", "qs": 300},
    {"num": "15", "title": "A Child's Thought of God", "qs": 300},
]

class MasterNumberedCanvas(canvas.Canvas):
    """Two-pass canvas to draw running header & footer across master document."""
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
        self.saveState()
        
        # Suppress running header/footer on cover page (page 1)
        if self._pageNumber > 1:
            # Header
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(colors.HexColor('#1E3A8A'))
            self.drawString(36, 762, "ICSE / CBSE CLASS IV ENGLISH -- MASTER QUESTION BANK")
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor('#6B7280'))
            self.drawRightString(576, 762, "15 Chapters | 4,472 Questions")
            self.setStrokeColor(colors.HexColor('#CBD5E1'))
            self.setLineWidth(0.5)
            self.line(36, 756, 576, 756)

            # Footer
            page_str = f"Page {self._pageNumber} of {page_count}"
            self.drawRightString(576, 25, page_str)
            self.drawString(36, 25, "Confidential & Proprietary -- Comprehensive Question Bank Series")
            self.line(36, 36, 576, 36)

        self.restoreState()

def md_to_reportlab_tags(text):
    """Converts Markdown inline syntax into ReportLab XML markup."""
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
    text = re.sub(r'`(.*?)`', r'<font name="Courier">\1</font>', text)
    return text

def parse_markdown_to_elements(filepath, styles):
    """Parses a category .md file into ReportLab flowable elements."""
    elements = []
    if not os.path.exists(filepath):
        return elements

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    in_table = False
    table_rows = []

    for line in lines:
        raw_line = line.rstrip("\r\n")
        stripped = raw_line.strip()

        if "|" in stripped and ("---" in stripped or stripped.startswith("|")):
            if "---" in stripped:
                continue
            in_table = True
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            table_rows.append(cells)
            continue
        elif in_table:
            if table_rows:
                t_data = []
                for row_idx, r in enumerate(table_rows):
                    row_cells = []
                    for c in r:
                        c_formatted = md_to_reportlab_tags(c)
                        st = styles['TableHeader'] if row_idx == 0 else styles['TableCell']
                        row_cells.append(Paragraph(c_formatted, st))
                    t_data.append(row_cells)

                t = Table(t_data, hAlign='LEFT')
                t.setStyle(TableStyle([
                    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F3F4F6')),
                    ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor('#1E3A8A')),
                    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
                    ('TOPPADDING', (0,0), (-1,-1), 5),
                    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#D1D5DB')),
                ]))
                elements.append(Spacer(1, 4))
                elements.append(t)
                elements.append(Spacer(1, 6))
            in_table = False
            table_rows = []

        if not stripped:
            continue

        if stripped.startswith("# "):
            h_text = md_to_reportlab_tags(stripped[2:])
            elements.append(Spacer(1, 10))
            elements.append(Paragraph(h_text, styles['H1']))
            elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#1E3A8A'), spaceAfter=8))
        elif stripped.startswith("## "):
            h_text = md_to_reportlab_tags(stripped[3:])
            elements.append(Spacer(1, 8))
            elements.append(Paragraph(h_text, styles['H2']))
        elif stripped.startswith("### "):
            h_text = md_to_reportlab_tags(stripped[4:])
            elements.append(Spacer(1, 6))
            elements.append(Paragraph(h_text, styles['H3']))
        elif stripped == "---":
            elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#E5E7EB'), spaceBefore=6, spaceAfter=6))
        elif stripped.startswith(">"):
            quote_text = md_to_reportlab_tags(stripped.lstrip("> "))
            elements.append(Spacer(1, 3))
            elements.append(Paragraph(quote_text, styles['Blockquote']))
            elements.append(Spacer(1, 3))
        elif stripped.startswith("- **Answer Key"):
            ans_text = md_to_reportlab_tags(stripped)
            elements.append(Paragraph(ans_text, styles['AnswerKey']))
            elements.append(Spacer(1, 4))
        elif stripped.startswith("- **Question ID") or stripped.startswith("- **"):
            meta_text = md_to_reportlab_tags(stripped)
            elements.append(Paragraph(meta_text, styles['Metadata']))
        elif stripped.startswith("- (") or stripped.startswith("  - ("):
            opt_text = md_to_reportlab_tags(stripped.strip("- "))
            elements.append(Paragraph(opt_text, styles['Option']))
        elif stripped.startswith("- ") or stripped.startswith("  - "):
            item_text = md_to_reportlab_tags(stripped.lstrip("- "))
            elements.append(Paragraph(item_text, styles['Bullet']))
        else:
            p_text = md_to_reportlab_tags(stripped)
            elements.append(Paragraph(p_text, styles['Body']))

    return elements

def build_master_pdf():
    print(f"Building Consolidated Master Book PDF -> {OUTPUT_PDF_PATH}...")

    if os.path.exists(OUTPUT_PDF_PATH):
        try:
            os.remove(OUTPUT_PDF_PATH)
            print("Removed old master PDF.")
        except Exception as e:
            print(f"Warning: Could not remove old file ({e}). Overwriting.")

    styles = getSampleStyleSheet()

    custom_styles = {
        'CoverTitle': ParagraphStyle('CoverTitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=26, leading=32, textColor=colors.HexColor('#1E3A8A'), alignment=1, spaceAfter=10),
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
        'Bullet': ParagraphStyle('BulletCustom', parent=styles['Normal'], fontName='Helvetica', fontSize=9, leading=12.5, textColor=colors.HexColor('#334155'), leftIndent=12, spaceAfter=2),
        'AnswerKey': ParagraphStyle('AnswerKeyCustom', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, leading=12, textColor=colors.HexColor('#15803D'), backColor=colors.HexColor('#DCFCE7'), borderColor=colors.HexColor('#86EFAC'), borderWidth=0.5, borderPadding=4, spaceBefore=3, spaceAfter=6, leftIndent=10),
        'TableHeader': ParagraphStyle('TH', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9, leading=11, textColor=colors.HexColor('#1E3A8A'), alignment=0),
        'TableCell': ParagraphStyle('TC', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=11, textColor=colors.HexColor('#334155'), alignment=0),
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

    # ================= COVER PAGE =================
    story.append(Spacer(1, 100))
    story.append(Paragraph("ICSE &amp; CBSE CLASS IV ENGLISH", custom_styles['CoverSubtitle']))
    story.append(Paragraph("MASTER QUESTION BANK", custom_styles['CoverTitle']))
    story.append(HRFlowable(width="80%", thickness=3, color=colors.HexColor('#1E3A8A'), spaceBefore=10, spaceAfter=25))
    story.append(Paragraph("<b>15 Complete Chapters | 6 Exam Categories | 4,472 Total Questions</b>", custom_styles['CoverMeta']))
    story.append(Paragraph("Aligned with CISCE &amp; CBSE Curriculum Standards for Primary English", custom_styles['CoverMeta']))
    story.append(Spacer(1, 140))
    story.append(Paragraph("<b>Includes:</b> Section A Passage MCQs | Section B Guided Composition | Section C Grammar | Section D Picture &amp; RTC Tasks", custom_styles['CoverMeta']))
    story.append(Paragraph("<b>Publication Edition</b>: 2026-2027 Master Reference", custom_styles['CoverMeta']))
    story.append(PageBreak())

    # ================= TABLE OF CONTENTS =================
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
            Paragraph("6 Categories (Section A-D)", custom_styles['TOCDetail'])
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

    # ================= CHAPTER CONTENT STITCHING =================
    files_order = [
        ("1. Reading Comprehension (Section A)", "reading_comprehension.md"),
        ("2. Guided Writing (Section B)", "guided_writing.md"),
        ("3. Grammar & Language Skills (Section C)", "grammar_language.md"),
        ("4. Picture-Based Questions (Section D)", "picture_based.md"),
        ("5. Short Answer Questions (Section D)", "short_answer.md"),
        ("6. Extract & Stanza Analysis (Section D)", "extract_stanza.md")
    ]

    for ch in CHAPTER_INFO:
        ch_num = ch["num"]
        ch_dir = os.path.join(QUESTION_BANK_DIR, f"chapter_{ch_num}")
        if not os.path.exists(ch_dir):
            print(f"Skipping missing chapter directory: {ch_dir}")
            continue

        # Chapter Cover / Divider Page
        story.append(Spacer(1, 20))
        story.append(Paragraph(f"CHAPTER {ch_num}", custom_styles['ChBannerSub']))
        story.append(Paragraph(ch['title'].upper(), custom_styles['ChBanner']))
        story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#1E3A8A'), spaceBefore=10, spaceAfter=15))
        story.append(Paragraph(f"Total Questions: <b>{ch['qs']}</b> | Standard: <b>ICSE/CBSE Class IV English</b>", custom_styles['CoverMeta']))
        story.append(Spacer(1, 15))

        for cat_title, filename in files_order:
            filepath = os.path.join(ch_dir, filename)
            elements = parse_markdown_to_elements(filepath, custom_styles)
            if elements:
                story.extend(elements)
                story.append(Spacer(1, 10))

        story.append(PageBreak())

    doc.build(story, canvasmaker=MasterNumberedCanvas)
    print(f"[SUCCESS] Consolidated Master Book PDF generated: {OUTPUT_PDF_PATH}")

if __name__ == "__main__":
    build_master_pdf()
