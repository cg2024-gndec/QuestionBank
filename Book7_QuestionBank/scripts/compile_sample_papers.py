r"""
=============================================================================
Script: compile_sample_papers.py
Description: ReportLab PDF compilation tool for ICSE Class IV English Sample Papers
             (Set 1 & Set 2).
Usage: .\.venv\Scripts\python.exe QuestionBank\scripts\compile_sample_papers.py
=============================================================================
"""

import os
import sys
import re
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, PageBreak, Table, TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENERATED_PAPERS_DIR = os.path.join(BASE_DIR, "generated_papers")

def clean_md_formatting(text):
    """Clean markdown formatting for ReportLab paragraph text."""
    # Convert bold markdown **text** -> <b>text</b>
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    # Convert italic markdown *text* -> <i>text</i>
    text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
    # Escape ampersands not part of HTML entities
    text = re.sub(r'&(?!amp;|lt;|gt;)', '&amp;', text)
    return text

def compile_paper_pdf(md_filename, pdf_filename):
    md_path = os.path.join(GENERATED_PAPERS_DIR, md_filename)
    pdf_path = os.path.join(GENERATED_PAPERS_DIR, pdf_filename)

    if not os.path.exists(md_path):
        print(f"Error: Markdown file does not exist: {md_path}")
        return False

    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    paper_title_style = ParagraphStyle(
        'PaperTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#1E3A8A'),
        alignment=1,
        spaceAfter=4
    )

    paper_subtitle_style = ParagraphStyle(
        'PaperSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#2563EB'),
        alignment=1,
        spaceAfter=8
    )

    section_style = ParagraphStyle(
        'PaperSection',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=colors.HexColor('#1E3A8A'),
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    )

    question_style = ParagraphStyle(
        'PaperQ',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14.5,
        textColor=colors.HexColor('#0F172A'),
        spaceBefore=8,
        spaceAfter=3,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'PaperBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#334155'),
        spaceAfter=3
    )

    quote_style = ParagraphStyle(
        'PaperQuote',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#1E293B'),
        backColor=colors.HexColor('#F1F5F9'),
        borderColor=colors.HexColor('#CBD5E1'),
        borderWidth=1,
        borderPadding=6,
        spaceBefore=4,
        spaceAfter=6
    )

    tbl_header_style = ParagraphStyle(
        'TblHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11,
        textColor=colors.white,
        alignment=1
    )

    tbl_cell_style = ParagraphStyle(
        'TblCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#1E293B')
    )

    story = []

    def HeaderFooter(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica-Bold', 8)
        canvas.setFillColor(colors.HexColor('#475569'))
        canvas.drawString(36, 762, "ICSE Class IV English Examination Paper | CISCE Guidelines")
        canvas.drawRightString(576, 762, "Max Marks: 60 | Time: 2.5 Hours")
        canvas.setStrokeColor(colors.HexColor('#CBD5E1'))
        canvas.setLineWidth(0.5)
        canvas.line(36, 756, 576, 756)

        canvas.setFont('Helvetica', 8)
        canvas.drawString(36, 20, "Confidential - For School Examination Purpose Only")
        canvas.drawRightString(576, 20, f"Page {doc.page}")
        canvas.line(36, 30, 576, 30)
        canvas.restoreState()

    in_table = False
    table_rows = []

    for line in lines:
        raw_line = line
        line = line.strip()

        if not line:
            if in_table and table_rows:
                # Flush table
                t_data = []
                for row_idx, r in enumerate(table_rows):
                    row_cells = []
                    for c_text in r:
                        st = tbl_header_style if row_idx == 0 else tbl_cell_style
                        row_cells.append(Paragraph(clean_md_formatting(c_text), st))
                    t_data.append(row_cells)
                
                # Determine column widths
                col_count = len(t_data[0]) if t_data else 1
                col_width = (540 / col_count) if col_count > 0 else 540
                
                t = Table(t_data, colWidths=[col_width]*col_count)
                t.setStyle(TableStyle([
                    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E3A8A')),
                    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
                    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
                    ('VALIGN', (0,0), (-1,-1), 'TOP'),
                    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#94A3B8')),
                    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
                    ('TOPPADDING', (0,0), (-1,-1), 4),
                    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
                ]))
                story.append(t)
                story.append(Spacer(1, 6))
                in_table = False
                table_rows = []
            continue

        # Markdown Table parsing
        if line.startswith('|') and line.endswith('|'):
            if '---' in line:
                continue
            cells = [c.strip() for c in line.split('|')[1:-1]]
            if cells:
                in_table = True
                table_rows.append(cells)
            continue

        if in_table and table_rows:
            # End table if non-table line encountered
            t_data = []
            for row_idx, r in enumerate(table_rows):
                row_cells = []
                for c_text in r:
                    st = tbl_header_style if row_idx == 0 else tbl_cell_style
                    row_cells.append(Paragraph(clean_md_formatting(c_text), st))
                t_data.append(row_cells)
            
            col_count = len(t_data[0]) if t_data else 1
            col_width = (540 / col_count) if col_count > 0 else 540
            
            t = Table(t_data, colWidths=[col_width]*col_count)
            t.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E3A8A')),
                ('TEXTCOLOR', (0,0), (-1,0), colors.white),
                ('ALIGN', (0,0), (-1,-1), 'LEFT'),
                ('VALIGN', (0,0), (-1,-1), 'TOP'),
                ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#94A3B8')),
                ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
                ('TOPPADDING', (0,0), (-1,-1), 4),
                ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ]))
            story.append(t)
            story.append(Spacer(1, 6))
            in_table = False
            table_rows = []

        if line.startswith('# '):
            title_text = clean_md_formatting(line[2:])
            story.append(Spacer(1, 4))
            story.append(Paragraph(title_text, paper_title_style))
            story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#1E3A8A'), spaceBefore=4, spaceAfter=8))
        elif line.startswith('## '):
            sec_text = clean_md_formatting(line[3:])
            if "ANSWER KEY" in sec_text.upper():
                story.append(PageBreak())
                story.append(Paragraph(sec_text, paper_title_style))
                story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#1E3A8A'), spaceBefore=4, spaceAfter=8))
            else:
                story.append(Paragraph(sec_text, section_style))
                story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2563EB'), spaceBefore=2, spaceAfter=6))
        elif line.startswith('### '):
            h3_text = clean_md_formatting(line[4:])
            story.append(Paragraph(h3_text, question_style))
        elif line.startswith('#### '):
            h4_text = clean_md_formatting(line[5:])
            story.append(Paragraph(h4_text, question_style))
        elif line.startswith('> '):
            quote_text = clean_md_formatting(line[2:])
            story.append(Paragraph(quote_text, quote_style))
        elif line.startswith('---'):
            story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#CBD5E1'), spaceBefore=6, spaceAfter=6))
        elif line.startswith('**Max. Marks**') or line.startswith('**Time Allowed**') or 'General Instructions' in line:
            story.append(Paragraph(clean_md_formatting(line), paper_subtitle_style))
        else:
            story.append(Paragraph(clean_md_formatting(line), body_style))

    # Flush remaining table if file ends
    if in_table and table_rows:
        t_data = []
        for row_idx, r in enumerate(table_rows):
            row_cells = []
            for c_text in r:
                st = tbl_header_style if row_idx == 0 else tbl_cell_style
                row_cells.append(Paragraph(clean_md_formatting(c_text), st))
            t_data.append(row_cells)
        col_count = len(t_data[0]) if t_data else 1
        col_width = (540 / col_count) if col_count > 0 else 540
        t = Table(t_data, colWidths=[col_width]*col_count)
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E3A8A')),
            ('TEXTCOLOR', (0,0), (-1,0), colors.white),
            ('ALIGN', (0,0), (-1,-1), 'LEFT'),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#94A3B8')),
            ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ]))
        story.append(t)

    doc.build(story, onFirstPage=HeaderFooter, onLaterPages=HeaderFooter)
    print(f"SUCCESS: Sample Paper PDF generated -> {pdf_path}")
    return True

if __name__ == "__main__":
    compile_paper_pdf("Sample_Paper_Set_1.md", "ICSE_Class_4_English_Sample_Paper_Set_1.pdf")
    compile_paper_pdf("Sample_Paper_Set_2.md", "ICSE_Class_4_English_Sample_Paper_Set_2.pdf")
