import src.pdf as pdf

from datetime import datetime, timedelta


def get_menu(date: datetime) -> str:
    url = pdf.build_pdf_url(date)
    # menu = ''.join()
    return url


def get_today() -> str:
    return get_menu(datetime.now())

def get_tomorrow() -> str:
    return get_menu(datetime.now()+timedelta(days=1))

def get_week() -> str:
    pass
