from fpdf import FPDF
from wsl.util import open_in_windows_browser

pdf = FPDF(orientation='P', unit='mm', format='A4')

pdf.add_page()

pdf.set_font(family="Times", style='B', size=10)

pdf.cell(w=0, h=12, txt='Hello! PDF', align='L', ln=1, border=0.25)
pdf.cell(w=0, h=12, txt='The whole new PDF', align='L', ln=1, border=0.25)

pdf.output('output.pdf')

open_in_windows_browser('output.pdf')

