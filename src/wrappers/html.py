import requests
import bs4


context = "https://ru.ufsc.br/ru/"


def get_menu_table(day: int) -> dict:
    response = requests.get(context)
    assert response.status_code < 300

    soup = bs4.BeautifulSoup(response.content, "html.parser")
    menu_to_parse = soup.find("table")
    
    menu_data = {}

    current_key = None
    # current_sub_key = None

    for row in menu_to_parse.find_all('tr')[1:250]:
        cols = [col.text.strip() for col in row.find_all('td') if col.text]

        for text in cols:
            if text.isupper():
                menu_data[text] = [text]
                current_key = text
                # current_sub_key = None

            elif text[:2].isdigit():
                menu_data[int(text[:2])] = menu_data.pop(current_key)
                current_key = int(text[:2])

            elif text.endswith(':'):
                continue

            # elif text.endswith(':') or current_sub_key is None:
            #     menu_data[current_key][text] = []
            #     current_sub_key = text

            else:
                menu_data[current_key] += [text]

    return menu_data