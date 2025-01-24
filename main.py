from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

topics = pd.read_csv("topics.csv")


def add_lines(n=1, y_start=0, y_offset=10):
    for i in range(n):
        y_line = y_start + y_offset * i
        pdf.line(10, y_line, 200, y_line)


for index, row in topics.iterrows():
    pdf.add_page()

    # Add header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.line(10, 21, 200, 21)
    pdf.cell(w=0, h=12, text=row["Topic"], align="L", ln=1)

    # Add 10 lines
    add_lines(27, 21, 10)

    # Add footer
    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, text=row["Topic"], align="R", ln=1)

    # Add additional pages per topic
    for _ in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(272)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, text=row["Topic"], align="R", ln=1)
        add_lines(27, 21, 10)


pdf.output("output.pdf")
