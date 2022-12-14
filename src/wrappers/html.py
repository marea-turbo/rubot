import requests
import bs4
import re
from pprint import pprint


context = "https://ru.ufsc.br/ru/"


def get_menu_dict() -> dict:
    response = requests.get(context)
    assert response.status_code < 300

    soup = bs4.BeautifulSoup(response.content, "html.parser")
    table = soup.find("table")
    text = table.text
    # print(text.strip())
    menu_data = {}
    weekday_regex = re.compile(r"((?:[A-ZÇ]+-)FEIRA)|SÁBADO|DOMINGO")

    itext = text
    for i in range(7):
        print(itext)
        weekday = weekday_regex.search(itext)
        next_weekday = weekday_regex.search(itext, pos=weekday.end()+1)

        try: 
            raw_day_menu = itext[weekday.end()+1:next_weekday.start()-1]
        except AttributeError:
            raw_day_menu = itext[weekday.end()+1:]

        day = re.search(r"^\d{2}|^\d{1}", raw_day_menu)
        without_date = re.sub(r"^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}", "",  raw_day_menu).strip()
        without_doublepoints = re.sub(r".*:", "", without_date)
        menu_data[int(day.group())] = (weekday.group()+'\n' + without_doublepoints).split('\n')
        
        itext = itext[weekday.end()+len(raw_day_menu)+1:]

    return menu_data