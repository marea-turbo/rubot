import requests
import bs4
import re


context = "https://ru.ufsc.br/ru/"


def get_table_dict() -> str:
    response = requests.get(context)
    assert response.status_code < 300

    soup = bs4.BeautifulSoup(response.content, "html.parser")
    table = soup.find("table")

    menu_data = {}
    current_key = None

    for row in table.find_all('tr')[1:]:
        day_raw = row.text.replace("II", "").split()

        for word in day_raw:
            if word.isupper():
                menu_data[word] = [word]
                current_key = word

            elif word[:2].isdigit():
                menu_data[int(word[:2])] = menu_data.pop(current_key)
                current_key = int(word[:2])

            elif word.endswith(':'):
                start_section = day_raw.index(word)
                section = []

                for w in day_raw[start_section:][1:]:
                    if w.endswith(':'): break
                    section.append(w)

                menu_data[current_key] += re.findall('[a-zA-Z][^A-Z]*', " ".join(section).replace('/', ''))

    return menu_data