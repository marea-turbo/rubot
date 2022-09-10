import io
from urllib.request import Request, urlopen

from PyPDF2 import PdfFileReader


def get_pdf_from_url(url: str):
    remote_file = urlopen(Request(url)).read()
    memory_file = io.BytesIO(remote_file)
    pdf_file = PdfFileReader(memory_file)
    return pdf_file
