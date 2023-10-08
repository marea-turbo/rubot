import src.wrappers.pdf as pdf
import src.wrappers.html as html

from datetime import datetime, timedelta
from pytz import timezone


week_menu = {}


def format_menu(day_menu: list) -> str:
    """ 
        ### formato do day_menu:
        [
            DIA-DA-SEMANA, quibe, meu pau, pepino, cebola, ...
        ]
    """

    menu = "*" + day_menu[0] + '*\n'
    for content in day_menu[1:]:
        menu += "• " + content.strip() + '\n'

    return menu[:-1]


def get_menu(date: datetime) -> str:
    global week_menu

    try:
        return format_menu(week_menu[date.day])
    except KeyError:
        week_menu = html.get_menu_dict(date)

    try:
        return format_menu(week_menu[date.day])
    except Exception as e:
        return f"""
        bruh :( não consegui pegar o cardápio
        """


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