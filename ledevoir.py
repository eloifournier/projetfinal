# coding: utf-8

import requests, csv
from bs4 import BeautifulSoup
# Pour accéder aux articles en archive du journal Le Monde
baseUrl = "http://m.ledevoir.com/article-"

fichier = "ledevoir.csv"

entetes = {
    "User-Agent":"Éloi Fournier, étudiant en journalisme à l'UQAM / contact: eloifournier@gmail.com"
}

numero = list(range(544623,570036))

# Pour générer les numéros d'article dans l'url
for article in numero: 
   # print("http://m.ledevoir.com/article-" + str(article))
    urlArticle = "http://m.ledevoir.com/article-" + str(article)
    print(urlArticle)
    site = requests.get(urlArticle, headers=entetes)    
    page = BeautifulSoup(site.text, "html.parser")
    # articles = page.find_all("article", class_="article__paragraph")

    try: 
        nomAuteur = page.find("aside", class_="author").find("span").text.strip()
        print(nomAuteur)
        if "Agence France-Presse" in nomAuteur: 
            print("AFP")
        titreArticle = page.find("h1").text.strip()
        print(titreArticle)
        dateArticle = page.find("time").text.strip()
        print(dateArticle)
        pars = page.find("div", class_="editor")
        # for par in pars: 
           # print(par.text.strip())
        texte = pars.text.strip()
        print(texte)
        if "Agence France-Presse" not in nomAuteur: 
            dead = open(fichier,"a")
            obies = csv.writer(dead)
            obies.writerow([nomAuteur, titreArticle, dateArticle, texte])
    except: 
        print("Nada")
        
    print("."*10)