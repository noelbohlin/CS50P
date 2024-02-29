""" från uppgiften shirtificate från CS50 """

from fpdf import FPDF

class PDF(FPDF): # pylint: disable=R0903
    def header(self):
        self.image("shirtificate.png", 10, 70, 190)
        self.set_font("helvetica", "", 55)
        self.cell(0, 57, "CS50 Shirtificate", align="C")
        self.ln(20)


def main():
    pdf = PDF()
    pdf.add_page(orientation="portrait", format="a4")

    pdf.set_font("helvetica", size=28)
    pdf.set_text_color(255,255,255)

    pdf.cell(0, 213, f"{input('Name: ')} took CS50", align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
