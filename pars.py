import requests
from bs4 import BeautifulSoup

def parse():

    urL = "https://www.omgtu.ru/general_information/the-structure/the-department-of-university.php"

    response = requests.get(urL)

    soup = BeautifulSoup(response.text,"html.parser")


    data = soup.find("div", id = "pagecontent")
    data_ul = data.find_all("ul")
    return data_ul

def read():
    data_ul = parse()
    file = open("кафедры.txt","w")
    for i in data_ul:
        name = i.find("li").text.lstrip().replace("\n","") + "\n"
            
        file.write(name)

    file.close()






    