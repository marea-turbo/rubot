import src.wrappers.pdf as pdf
import src.wrappers.html as html

from datetime import datetime, timedelta
from pytz import timezone


week_menu = {}


def format_menu(menu_data: dict, day: int) -> str:
    """ 
        ### formato do menu_data:
        dia: [
            quibe, meu pau, pepino, cebola, ...
        ], ...
    """

    menu = "*" + menu_data[day][0] + '*\n'
    for content in menu_data[day][1:]:
        menu += "• " + content + '\n'

    return menu[:-1]


def get_menu(date: datetime) -> str:
    global week_menu

    html.get_table_string(date.day)
    return "bla"
    # if date.day in week_menu.keys(): return format_menu(week_menu, date.day)
    # else: week_menu = html.get_menu_table(date.day) 
    
    #  url = pdf.build_pdf_url(date)
    # tomorrow_date = (date+timedelta(days=1
    # return menu


def get_today() -> str:
    return get_menu(datetime.now(timezone("Brazil/East")))

def get_tomorrow() -> str:
    return get_menu(datetime.now(timezone("Brazil/East"))+timedelta(days=1))

# debug method
def get_week() -> str:
    week = ""
    now = datetime.now(timezone("Brazil/East"))
    monday = now - timedelta(days=now.weekday())

    for i in range(7):
        week += get_menu(monday+timedelta(days=i)) + '\n\n'
    return week[:-2]