import requests
import json
from bs4 import BeautifulSoup
import datetime


class Link:
    def __init__(self):
        self.list = []

    def to_json(self):
        with open(datetime.datetime.now().strftime('%Y-%m-%d-%S') + '.json', 'w') as archivo:
            json.dump(self.list, archivo, sort_keys=False, indent=4)

    def scrapping(self, url1z):
        url1 = url1z
        r = requests.get(url1)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'html.parser')
        items = soup.find_all('table')[0]
        search = items.find_all('tr')
        cont = 0
        cont2 = 0
        cont3 = 0
        cont4 = 0
        d1 = ""
        d2 = ""
        d3 = ""
        d4 = ""
        d5 = ""
        d6 = ""
        d7 = ""
        d8 = ""
        d9 = ""
        d10 = ""
        d11 = ""
        d12 = ""
        d13 = ""
        d14 = ""
        d15 = ""
        c = {}
        list = []
        for A1 in search:
            if cont > 1:
                ext = A1.find_all(class_='tddatos')
                for res in ext:
                    if cont2 == 0:
                        d1 = res.text
                        cont2 += 1
                    elif cont2 == 1:
                        d2 = res.text
                        cont2 += 1
                    elif cont2 == 2:
                        d3 = res.text
                        cont2 += 1
                    elif cont2 == 3:
                        d4 = res.text
                        cont2 += 1
                    elif cont2 == 4:
                        d5 = res.text
                        cont2 += 1
                    elif cont2 == 5:
                        d6 = res.text
                        cont2 += 1
                    elif cont2 == 6:
                        d7 = res.text
                        cont2 += 1
                    elif cont2 == 7:
                        look = res.find_all(class_='tdprofesor')
                        for view in look:
                            if cont4 == 0:
                                d14 = view.text
                                cont4 += 1
                            elif cont4 == 1:
                                d15 = view.text
                                cont4 += 1
                        cont4 = 0
                        h1 = A1.find(class_='td1').find_all('td')
                        for obt in h1:
                            if cont3 == 0:
                                d8 = obt.text
                                cont3 += 1
                            elif cont3 == 1:
                                d9 = obt.text
                                cont3 += 1
                            elif cont3 == 2:
                                d10 = obt.text
                                cont3 += 1
                            elif cont3 == 3:
                                d11 = obt.text
                                cont3 += 1
                            elif cont3 == 4:
                                d12 = obt.text
                                cont3 += 1
                            elif cont3 == 5:
                                d13 = obt.text
                                cont3 += 1
                        cont2 += 1
                        cont3 = 0
                        c = {
                            'NRC': d1,
                            'Codigo': d2,
                            'Nombre carrera': d3,
                            'Sec': d4,
                            'CR': d5,
                            'CUP': d6,
                            'DIS': d7,
                            'Ses': d8,
                            'Horario': d9,
                            'Dias': d10,
                            'Edificio': d11,
                            'Aula': d12,
                            'Periodo': d13,
                            'ses': d14,
                            'maestro': d15
                        }
                        self.list.append(c)
                cont2 = 0
            cont += 1
