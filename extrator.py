import io
from urllib.request import Request, urlopen

from PyPDF2 import PdfFileReader


def get_pdf_from_url(url):
    remote_file = urlopen(Request(url)).read()
    memory_file = io.BytesIO(remote_file)
    pdf_file = PdfFileReader(memory_file)
    return pdf_file

if __name__ == '__main__': 
    url = "https://siteru.paginas.ufsc.br/files/2022/09/Site-05-a-11.09-3.pdf"
    pdf_file = get_pdf_from_url(url)
    content = pdf_file.getPage(0).extract_text()
    print(content)