# coding: utf-8

import requests, csv
from bs4 import BeautifulSoup
# Pour accéder aux articles en archive du journal Le Monde
baseUrl = "https://www.lemonde.fr/archives-du-monde/"

fichier = "lemonde.csv"

entetes = {
    "User-Agent":"Éloi Fournier, étudiant en journalisme à l'UQAM / contact: eloifournier@gmail.com"
}

# Pour créer mes variables de jours/mois
journée = list(range(1,32))
mois = list(range(10,13))
année = 2019
n = 0
m = 0

# Pour coller les jours et mois à l'URL
for m in mois: 
    if m < 10: 
        m = "0" + str(m)    
    for jour in journée: 
        # print(jour)
        if jour < 10: 
            jour = "0" + str(jour)
        for page in range(1,11):    
            urlArticle = baseUrl + str(jour) + "-" + str(m) + "-" + str(année) + "/" + str(page) + "/"
            print(urlArticle)
            site = requests.get(urlArticle, headers=entetes)    
            page = BeautifulSoup(site.text, "html.parser")

            articles = page.find_all("a", class_="teaser__link")
    
            for article in articles: 
                n += 1
                # print(article)
                urlArticle = article["href"]
                print(n, urlArticle)

                siteArticle = requests.get(urlArticle, headers=entetes)
                pageArticle = BeautifulSoup(siteArticle.text, "html.parser")

                try: 
                    nomAuteur = pageArticle.find("span", class_="meta__author").text.strip()
                    print(nomAuteur)
                    if "Agence France-Presse" in nomAuteur: 
                        print("AFP")
                    titreArticle = pageArticle.find("h1", class_="article__title")
                    print(titreArticle)
                    dateArticle = pageArticle.find("span", class_="meta__date")
                    print(dateArticle)
                    pars = pageArticle.find_all("p", class_="article__paragraph")
                    texte = ""
                    for par in pars: 
                        texte += par.text + " "
                        # print(par.text)  
                    texte = texte.strip()
                    print(texte)  
                    if "Agence France-Presse" not in nomAuteur: 
                        dead = open(fichier,"a")
                        obies = csv.writer(dead)
                        obies.writerow([nomAuteur, titreArticle, dateArticle, texte])            
                except: 
                    print("Rien")

                print("."*10)