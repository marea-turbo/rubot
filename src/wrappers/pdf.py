import io

from requests import get
from datetime import datetime, timedelta
from PyPDF2 import PdfFileReader


def build_pdf_url(date: datetime) -> str:
    monday = date - timedelta(days=date.weekday())
    sunday = monday + timedelta(days=6)
    return f"https://siteru.paginas.ufsc.br/files/{date.year}/{date.strftime('%m')}" \
           f"/Site-{monday.strftime('%d')}-a-{sunday.strftime('%d')}.{date.strftime('%m')}-{1}.pdf"


def get_pdf(url: str):
    print(url)
    remote_file = get(url).content
    memory_file = io.BytesIO(remote_file)
    pdf_file = PdfFileReader(memory_file)
    return pdf_file.getPage(0).extract_text()
