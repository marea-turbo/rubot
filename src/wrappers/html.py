import pprint
import re
from datetime import datetime

import bs4
import requests


context = "https://ru.ufsc.br/ru/"


def get_menu_dict(date: datetime) -> dict:
    weekday = date.weekday()
    response = requests.get(context)

    soup = bs4.BeautifulSoup(response.content, "html.parser")
    text = soup.find("table").text

    raw_weeks: list = [raw_week.split("\n") for raw_week in text.strip().split("\n\n\n")][1::]
    pprint.pprint(raw_weeks)
    menu_data: dict = dict(zip(range(date.day - weekday, date.day - weekday + 7), iter(raw_weeks)))

    pprint.pprint(menu_data)

    return menu_data
