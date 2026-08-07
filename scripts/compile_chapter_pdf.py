r"""
=============================================================================
Script: compile_chapter_pdf.py
Description: Advanced ReportLab PDF compiler for Book4 Question Banks.
             Parses Markdown tags (headers, bold, italics, blockquotes, tables,
             lists, answer keys) and compiles a beautifully styled, professional
             PDF for each chapter.
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

class NumberedCanvas(canvas.Canvas):
    """Two-pass canvas to add running header and 'Page X of Y' footer."""
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
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor('#6B7280'))
        
        # Header (pages 2+)
        if self._pageNumber > 1:
            self.drawString(36, 762, "CBSE / ICSE Class IV English -- Question Bank")
            self.setStrokeColor(colors.HexColor('#E5E7EB'))
            self.setLineWidth(0.5)
            self.line(36, 756, 576, 756)
            
        # Footer (all pages)
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(576, 25, page_str)
        self.drawString(36, 25, "Confidential & Proprietary -- Question Bank Series")
        self.setStrokeColor(colors.HexColor('#E5E7EB'))
        self.setLineWidth(0.5)
        self.line(36, 36, 576, 36)
        
        self.restoreState()

def md_to_reportlab_tags(text):
    """Converts Markdown inline syntax (**bold**, *italic*, code) into ReportLab XML markup."""
    # Escape ampersands and angle brackets first (careful not to double escape)
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    
    # Bold: **text** -> <b>text</b>
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    
    # Italic: *text* or _text_ -> <i>text</i>
    text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
    
    # Code / inline tags: `text` -> <font name="Courier">\1</font>
    text = re.sub(r'`(.*?)`', r'<font name="Courier">\1</font>', text)
    
    return text

def parse_markdown_to_elements(filepath, styles):
    """Parses a category .md file into ReportLab flowable elements."""
    elements = []
    
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    in_table = False
    table_rows = []
    
    for line in lines:
        raw_line = line.rstrip("\r\n")
        stripped = raw_line.strip()
        
        # Table detection
        if "|" in stripped and ("---" in stripped or stripped.startswith("|")):
            if "---" in stripped:
                continue # Skip divider row
            in_table = True
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            table_rows.append(cells)
            continue
        elif in_table:
            # End of table
            if table_rows:
                # Build ReportLab Table
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

        # Headers
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
            # Blockquote / Callout
            quote_text = md_to_reportlab_tags(stripped.lstrip("> "))
            elements.append(Spacer(1, 3))
            elements.append(Paragraph(quote_text, styles['Blockquote']))
            elements.append(Spacer(1, 3))
        elif stripped.startswith("- **Answer Key"):
            # Answer key line
            ans_text = md_to_reportlab_tags(stripped)
            elements.append(Paragraph(ans_text, styles['AnswerKey']))
            elements.append(Spacer(1, 4))
        elif stripped.startswith("- **Question ID"):
            meta_text = md_to_reportlab_tags(stripped)
            elements.append(Paragraph(meta_text, styles['Metadata']))
        elif stripped.startswith("- **"):
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

def build_pdf(chapter_num):
    ch_dir = os.path.join(QUESTION_BANK_DIR, f"chapter_{chapter_num}")
    output_pdf = os.path.join(ch_dir, f"Chapter_{chapter_num}_Question_Bank.pdf")
    
    if not os.path.exists(ch_dir):
        print(f"Error: Chapter directory does not exist: {ch_dir}")
        sys.exit(1)
        
    # REMOVE EXISTING PDF IF PRESENT
    if os.path.exists(output_pdf):
        try:
            os.remove(output_pdf)
            print(f"Removed existing PDF: {output_pdf}")
        except Exception as e:
            print(f"Warning: Could not remove old PDF ({e}), overwriting.")

    files_order = [
        ("1. Reading Comprehension (Section A)", "reading_comprehension.md"),
        ("2. Guided Writing (Section B)", "guided_writing.md"),
        ("3. Grammar & Language Skills (Section C)", "grammar_language.md"),
        ("4. Picture-Based Questions (Section D)", "picture_based.md"),
        ("5. Short Answer Questions (Section D)", "short_answer.md"),
        ("6. Extract & Stanza Analysis (Section D)", "extract_stanza.md")
    ]
    
    styles = getSampleStyleSheet()
    
    # Custom Palette & Typography
    custom_styles = {
        'DocTitle': ParagraphStyle('DocTitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=22, leading=26, textColor=colors.HexColor('#0F172A'), alignment=1, spaceAfter=4),
        'DocSubtitle': ParagraphStyle('DocSubtitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=12, leading=16, textColor=colors.HexColor('#2563EB'), alignment=1, spaceAfter=12),
        'H1': ParagraphStyle('H1', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=16, leading=20, textColor=colors.HexColor('#1E3A8A'), spaceBefore=14, spaceAfter=6),
        'H2': ParagraphStyle('H2', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=13, leading=17, textColor=colors.HexColor('#1D4ED8'), spaceBefore=10, spaceAfter=4),
        'H3': ParagraphStyle('H3', parent=styles['Heading3'], fontName='Helvetica-Bold', fontSize=11, leading=15, textColor=colors.HexColor('#0F172A'), spaceBefore=8, spaceAfter=3),
        'Body': ParagraphStyle('BodyTextCustom', parent=styles['Normal'], fontName='Helvetica', fontSize=9.5, leading=13.5, textColor=colors.HexColor('#334155'), spaceAfter=4),
        'Blockquote': ParagraphStyle('BlockquoteCustom', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=9, leading=13, textColor=colors.HexColor('#1E293B'), backColor=colors.HexColor('#F1F5F9'), borderColor=colors.HexColor('#CBD5E1'), borderWidth=0.5, borderPadding=6, spaceAfter=6),
        'Metadata': ParagraphStyle('MetadataCustom', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=11.5, textColor=colors.HexColor('#475569'), leftIndent=10, spaceAfter=2),
        'Option': ParagraphStyle('OptionCustom', parent=styles['Normal'], fontName='Helvetica', fontSize=9, leading=12.5, textColor=colors.HexColor('#1E293B'), leftIndent=20, spaceAfter=2),
        'Bullet': ParagraphStyle('BulletCustom', parent=styles['Normal'], fontName='Helvetica', fontSize=9, leading=12.5, textColor=colors.HexColor('#334155'), leftIndent=12, spaceAfter=2),
        'AnswerKey': ParagraphStyle('AnswerKeyCustom', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9, leading=13, textColor=colors.HexColor('#15803D'), backColor=colors.HexColor('#DCFCE7'), borderColor=colors.HexColor('#86EFAC'), borderWidth=0.5, borderPadding=4, spaceBefore=3, spaceAfter=6, leftIndent=10),
        'TableHeader': ParagraphStyle('TH', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9, leading=11, textColor=colors.HexColor('#1E3A8A'), alignment=0),
        'TableCell': ParagraphStyle('TC', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=11, textColor=colors.HexColor('#334155'), alignment=0),
    }

    doc = SimpleDocTemplate(
        output_pdf,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=45,
        bottomMargin=45
    )
    
    story = []
    
    # Cover Header
    story.append(Paragraph(f"CHAPTER {chapter_num} QUESTION BANK", custom_styles['DocTitle']))
    story.append(Paragraph("CBSE & ICSE CLASS IV ENGLISH -- EXAM ALIGNED SERIES", custom_styles['DocSubtitle']))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#1E3A8A'), spaceAfter=15))
    
    for cat_title, filename in files_order:
        filepath = os.path.join(ch_dir, filename)
        if not os.path.exists(filepath):
            continue
            
        elements = parse_markdown_to_elements(filepath, custom_styles)
        if elements:
            story.extend(elements)
            story.append(Spacer(1, 10))
            
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[OK] Compiled PDF successfully: {output_pdf}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--chapter", help="Chapter number (e.g. 01, 12)")
    parser.add_argument("--all", action="store_true", help="Compile all 15 chapters sequentially")
    args = parser.parse_args()

    if args.all:
        print("Starting batch compilation for all 15 chapters...")
        for ch_num in range(1, 16):
            ch_str = f"{ch_num:02d}"
            print(f"\n--- Compiling Chapter {ch_str} PDF ---")
            build_pdf(ch_str)
        print("\n[SUCCESS] Batch compilation of all 15 chapters completed.")
    elif args.chapter:
        build_pdf(args.chapter)
    else:
        parser.print_help()

