import src.wrappers.pdf as pdf
import src.wrappers.html as html

from datetime import datetime, timedelta


week_menu = {}


def format_menu(menu_data: dict, day: int) -> str:
    """ 
        ### formato do menu_data:
        dia: [
            quibe, meu pau, pepino, cebola, ...
        ], ...
    """

    menu = "**" + menu_data[day][0] + '**\n'
    for content in menu_data[day][1:]:
        menu += "• " + content + '\n'

    return menu[:-1]


def get_menu(date: datetime) -> str:
    global week_menu

    if date.day in week_menu.keys(): return format_menu(week_menu, date.day)

    # url = pdf.build_pdf_url(date)
    # tomorrow_date = (date+timedelta(days=1))
    # today, tomorrow = date.strftime('%d/ %m/ %Y'), tomorrow_date.strftime('%d/ %m/ %Y')

    # # if tomorrow is monday (0)
    # if not tomorrow_date.weekday():
    #     tomorrow = "\n\n"

    # t = pdf.get_pdf(url)
    # menu = t[t.find(today)-len(today)-1:t.rfind(tomorrow)-len(tomorrow)-1]
    # return menu

    week_menu = html.get_menu_table(date.day)
    return format_menu(week_menu, date.day)


def get_today() -> str:
    return get_menu(datetime.now())

def get_tomorrow() -> str:
    return get_menu(datetime.now()+timedelta(days=1))

def get_week() -> str:
    week = ""
    now = datetime.now()
    monday = now - timedelta(days=now.weekday())

    for i in range(7):
        week += get_menu(monday+timedelta(days=i)) + '\n\n'
    return week[:-2]