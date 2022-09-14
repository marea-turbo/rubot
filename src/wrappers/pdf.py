import io

from requests import get
from datetime import datetime, timedelta
from PyPDF2 import PdfFileReader


context = "https://siteru.paginas.ufsc.br/files/"


def build_pdf_url(date: datetime) -> str:
    monday = date - timedelta(days=date.weekday())
    sunday = monday + timedelta(days=6)
    return f"{context}{date.year}/{date.strftime('%m')}" \
           f"/Site-{monday.strftime('%d')}-a-{sunday.strftime('%d')}.{date.strftime('%m')}-{1}.pdf"


def get_page_string(url: str, page: int) -> str:
    remote_file = get(url).content
    memory_file = io.BytesIO(remote_file)
    pdf_file = PdfFileReader(memory_file)
    return pdf_file.getPage(page).extract_text()


def get_menu_table() -> dict:
    url = build_pdf_url
