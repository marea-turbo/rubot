import src.pdf as pdf

from datetime import datetime, timedelta, timezone
from re import search


def get_menu(date: datetime) -> str:
    url = pdf.build_pdf_url(date)
    tomorrow_date = (date+timedelta(days=1))
    today, tomorrow = date.strftime('%d/ %m/ %Y'), tomorrow_date.strftime('%d/ %m/ %Y')

    # if tomorrow is monday (0)
    if not tomorrow_date.weekday():
        tomorrow = "\n\n"

    t = pdf.get_pdf(url)
    menu = t[t.find(today)-len(today)-1:t.rfind(tomorrow)-len(tomorrow)-1]
    return menu


def get_today() -> str:
    return get_menu(datetime.now())

def get_tomorrow() -> str:
    return get_menu(datetime.now()+timedelta(days=1))

def get_week() -> str:
    pass
