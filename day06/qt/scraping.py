import requests
from bs4 import BeautifulSoup
import json

url = 'https://fr.wikipedia.org/wiki/Liste_de_plats_africains'
req = requests.get(url)

soup = BeautifulSoup(req.text, "html.parser")
# print(soup)

print(soup.title)
print(soup.title.string)
print(soup.h1)
print(soup.h1.string)
print(soup.h1.attrs)

div = soup.html.find_all("div")

lignes = soup.html.find_all("tr")

plats = []
for ligne in lignes:
    cell = ligne.find_all("td")
    if (len(cell) > 0):
        if (cell[0].find("a")):
            lien = "https://fr.wikipedia.org/" + cell[0].find("a").get('href')
        else:
            lien = ""

        if (cell[1].find("img")):
            img = "https:" + cell[1].find("img").get('src')
        else:
            img = ""

        plat = {
            'nom': cell[0].get_text().strip(),
            'url_recette': lien,
            'url_image': img,
            'pays': cell[2].get_text().strip(),
            'description': cell[3].get_text().strip(),
        }
        plats.append(plat)

with open("cuisine.json", 'w') as outfile:
    json.dump(plats, outfile, indent=4)
