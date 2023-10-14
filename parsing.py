import requests
from bs4 import BeautifulSoup


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'
}

def parse_table():
    
    URL = "https://auto-meh.ru/studentu/ochnoe-otdelenie/zameny-ochnogo-otdeleniya.html"
    page = requests.get(URL, headers=HEADERS)
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


def parse_day():
    URL = "https://auto-meh.ru/studentu/ochnoe-otdelenie/zameny-ochnogo-otdeleniya.html"
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.text, "lxml")
    
    day = soup.find('div', class_="itemFullText").find('p').text
    
    return day


def parse_practice() -> str:
    URL = "https://auto-meh.ru/studentu/ochnoe-otdelenie/zameny-ochnogo-otdeleniya.html"
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.text, "lxml")
    
    practice = soup.find('div', class_="itemFullText").find_all('p')[1].text
    
    return practice


def parse_duty():
    URL = "https://auto-meh.ru/studentu/ochnoe-otdelenie/zameny-ochnogo-otdeleniya.html"
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.text, "lxml")
    
    duty = soup.find('div', class_="itemFullText").find_all('p')[2].text
    
    return duty

def parse_modifyDate():
    URL = "https://auto-meh.ru/studentu/ochnoe-otdelenie/zameny-ochnogo-otdeleniya.html"
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.text, "lxml")
    
    modifyDate = soup.find('span', class_="itemDateModified").text
    
    return modifyDate