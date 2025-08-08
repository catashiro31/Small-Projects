import glob
from pathlib import Path
from fpdf import FPDF
# Get Path
filepaths = glob.glob('Text/*.txt')
pdf = FPDF(orientation='P',unit='mm',format='A4')
for filepath in filepaths:
    filename = Path(filepath).stem
    # Get Text
    with open(filepath,'r') as file:
        content = file.read()
    # Print Title and Content
    pdf.add_page()
    pdf.set_font(family='Times',style='B',size=24)
    pdf.cell(w=0, h=10, txt=filename.capitalize(), border=0, ln=1, align='L')
    pdf.ln(5)
    pdf.set_font(family='Times',style='',size=14)
    pdf.multi_cell(w=0, h=6, txt=content, border=0, align='J')

pdf.output('output.pdf')