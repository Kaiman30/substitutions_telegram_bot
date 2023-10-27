import requests
from bs4 import BeautifulSoup


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'
}



def parse_tables():
    URL = "https://auto-meh.ru/studentu/ochnoe-otdelenie/zameny-ochnogo-otdeleniya.html"
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.text, "lxml")
    
    tables = soup.find('div', class_="itemFullText").find_all('table')
    tables_count = len(tables)
    
    # Если на странице больше двух таблиц (Замены + распределение)
    if tables_count > 2:
        table1 = tables[0].find_all('td')
        table2 = tables[1].find_all('td')
        
        substitutions = []
        substitutions2 = []
        
        for item in table1:
            p_tag = item.find('p')
            if p_tag is not None:
                substitutions.append(p_tag.text)
            else:
                substitutions.append("")
        
            with open("subs.txt", "w") as file:
                for i in substitutions:
                    file.writelines(i + '\n')
        
        for item in table2:
            p_tag = item.find('p')
            if p_tag is not None:
                substitutions2.append(p_tag.text)
            else:
                substitutions2.append("")
        
        with open("subs2.txt", "w") as file:
            for i in substitutions2:
                file.writelines(i + '\n')
                
        return substitutions, substitutions2
    
    # Если на странице две таблицы (Замены + распределение)
    elif tables_count == 2:
        table1 = tables[0].find_all('td')
        
        substitutions = []
        
        for item in table1:
            p_tag = item.find('p')
            if p_tag is not None:
                substitutions.append(p_tag.text)
            else:
                substitutions.append("")
        
            with open("subs.txt", "w") as file:
                for i in substitutions:
                    file.writelines(i + '\n')
                    
        return substitutions
                


# def parse_table1():
#     URL = "https://auto-meh.ru/studentu/ochnoe-otdelenie/zameny-ochnogo-otdeleniya.html"
#     page = requests.get(URL, headers=HEADERS)
#     soup = BeautifulSoup(page.text, "lxml")
    
    
#     table = soup.find('div', class_="itemFullText").find('table').find_all('td')
    
#     substitutions = []

#     for item in table:
#         p_tag = item.find('p')
#         if p_tag is not None:
#             substitutions.append(p_tag.text)
#         else:
#             substitutions.append("")
        
#         with open("subs.txt", "w") as file:
#             for i in substitutions:
#                 file.writelines(i + '\n')

#     return substitutions


# def parse_table2():
#     URL = "https://auto-meh.ru/studentu/ochnoe-otdelenie/zameny-ochnogo-otdeleniya.html"
#     page = requests.get(URL, headers=HEADERS)
#     soup = BeautifulSoup(page.text, "lxml")
    
    
#     table = soup.find('div', class_="itemFullText").find('table')[1].find_all('td')
    
#     substitutions = []

#     for item in table:
#         p_tag = item.find('p')
#         if p_tag is not None:
#             substitutions.append(p_tag.text)
#         else:
#             substitutions.append("")
        
#         with open("subs2.txt", "w") as file:
#             for i in substitutions:
#                 file.writelines(i + '\n')

#     return substitutions

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