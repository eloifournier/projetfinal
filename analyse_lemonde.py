# coding: utf-8

import csv, spacy
from collections import Counter

tal = spacy.load("fr_core_news_md")

lemonde = "lemonde.csv"

f = open(lemonde, encoding="latin-1")
articles = csv.reader(f)
next(articles)

tousMots = []
bigrams = []

for article in articles: 
    # print (article)
    doc = tal(str(article))
    tokens = [token.text for token in doc]
    for token in doc: 
        # print(token.text)
        lemmas = [token.lemma_ for token in doc if token.is_stop == False and token.is_punct == False]
    for lemma in lemmas: 
        tousMots.append(lemma)
    # for x, y in enumerate(lemmas[:-1]):
    #     bigrams.append("{} {}".format(lemmas[x], lemmas[x+1]))
    # print(len(bigrams))

    # print(bigrams)

freq = Counter(lemmas)
print(freq.most_common(101))