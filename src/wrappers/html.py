import requests
import bs4
import re


context = "https://ru.ufsc.br/ru/"


def get_tag_str(tag) -> str:
    for child in tag.children:
        if type(child) == bs4.Tag:
            return get_tag_str(child)
        print(child.text)


def get_table_string(day: int) -> str:
    response = requests.get(context)
    assert response.status_code < 300

    soup = bs4.BeautifulSoup(response.content, "html.parser")
    table = soup.find("table")
    print(get_tag_str(table))
    
    # ba = re.sub(r'(\n){2,}', '', table_to_parse.text)
    # print(ba)

    # menu_data = {}

    # current_key = None

    # for row in menu_to_parse.find_all('tr')[1:250]:
    #     cols = [col.text.strip() for col in row.find_all('td') if col.text]

    #     for text in cols:
    #         if text.isupper():
    #             menu_data[text] = [text]
    #             current_key = text

    #         elif text[:2].isdigit():
    #             menu_data[int(text[:2])] = menu_data.pop(current_key)
    #             current_key = int(text[:2])

    #         elif text.endswith(':'):
    #             continue

    #         else:
    #             menu_data[current_key] += [text]

    # return menu_data