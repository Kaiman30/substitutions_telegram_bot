import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://auto-meh.ru/studentu/ochnoe-otdelenie/zameny-ochnogo-otdeleniya.html"

page = requests.get(URL)

def parsing():
    soup = BeautifulSoup(page.text, "lxml")
    table = soup.find('div', class_="itemFullText").find('table').find_all('td')

    substitutions = []

    for item in table:
        p_tag = item.find('p')
        if p_tag is not None:
            substitutions.append(p_tag.text)
        else:
            substitutions.append("")
        
        with open("subs.txt", "w") as file:
            for i in substitutions:
                file.writelines(i + '\n')

    return substitutions