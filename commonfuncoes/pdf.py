import fitz
import pdfplumber

def read_pdf(file:str) -> str:

    file_text = ""

    with fitz.open(file) as doc:
        for page in doc:
            file_text += page.getText()
    return file_text

def ler_pdf(file:str) -> str:

    with pdfplumber.open(file) as pdf:
        first_page = pdf.pages[0]
        content = first_page.extract_text()
        return content

