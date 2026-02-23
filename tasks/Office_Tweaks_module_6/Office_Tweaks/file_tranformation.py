from docx2pdf import convert
from pdf2docx import Converter
import os

class Transformation:

    def pdf_to_docx(self, pdf_file):
        name, _ = os.path.splitext(pdf_file)
        docx_file = name + ".docx"

        converter = Converter(pdf_file)
        converter.convert(docx_file)
        converter.close()

        return docx_file

    def docx_to_pdf(self, docx_file):
        name, _ = os.path.splitext(docx_file)
        pdf_file = name + ".pdf"

        convert(docx_file, pdf_file)

        return pdf_file