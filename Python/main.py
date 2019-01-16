##! /usr/bin/python
# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup

sexton = "http://www.itsrugby.fr/joueur-4545.html"
vulivuli = "http://www.itsrugby.fr/joueur-17678.html"
ford = "http://www.itsrugby.fr/joueur-18596.html"
<<<<<<< HEAD
bobo = "http://www.itsrugby.fr/joueur_1859.html"
reponse = urllib.request.urlopen(sexton)
=======
reponse = urllib.request.urlopen(ford)
>>>>>>> origin/master
html = reponse.read().decode(reponse.headers.get_content_charset())
soup = BeautifulSoup(html, features="html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text(separator="|")
# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
textBio = '\n'.join(chunk for chunk in chunks if chunk not in ["","|","|:|","| |"])
# print(textBio)
textStat = textBio
# print(textStat)

def getJoueurBio(text):
    nom = text.split("Nom|\n|",1)[1].split("|\n| Age")[0].replace("\n","")
    print("Nom:", nom)

    age_date = text.split("Age|\n|",1)[1].split("|\n| Prenom")[0].replace("\n","")
    # print(age_date)
    age = age_date[0:2]
    date = age_date[-11:-1]
    print("Âge:", age)
    print("Date de naissance:", date)

    prenom = text.split("Prenom|\n|",1)[1].split("|\n| Poste")[0].replace("\n","")
    print("Prénom:", prenom)

    poste = text.split("Poste|\n",1)[1].split("\n| Nationalité")[0].replace("\n","")
    print("Poste:", poste)

    nation = text.split("Nationalité|\n|",1)[1].split("|\n| Mensuration")[0].replace("\n","").strip()
    print("Nation:", nation)

    poids_taille = text.split("Mensuration|\n",1)[1].split("\n|Recommander")[0].split("\n",1)
    poids = int(poids_taille[0].split(" ")[0])
    taille = int(poids_taille[1].split(" ")[0]+poids_taille[1].split(" ")[2])
    print("Poids:", poids)
    print("Taille:", taille)

def txt2value(str):
    if str == "-":
        value = 0
    else:
        value = int(str)
    return value

<<<<<<< HEAD
def getJoueurClubStat(text):
    table = text.split("|Min.|\n",1)[1]
    table = table.split("|Copyright",1)[0]
    # print(table)
    bool_sp = False

    for line in table.splitlines():
        line_split = list(filter(None, line.split("|")))
        quotient = len(line_split) // 11
        reste = len(line_split) % 11
        print(len(line_split), quotient, reste, line_split)

        if len(line_split) == 1:
            saison = line_split[0]
            continue
        elif reste == 2:
            saison_prec = line_split[-1]
            bool_sp = True

        # print(saison)
        saisonList, club, competition, points, joues, titularisations, essais, penalites, drops, transformations, cartons_jaunes, cartons_rouges, minutes = ([] for i in range(13))

        for i in range(0, quotient):
            saisonList.append(saison)
            club.append(line_split[0])
            competition.append(line_split[11*i+1])
            points.append(txt2value(line_split[11*i+2]))
            joues.append(txt2value(line_split[11*i+3]))
            titularisations.append(txt2value(line_split[11*i+4]))
            essais.append(txt2value(line_split[11*i+5]))
            penalites.append(txt2value(line_split[11*i+6]))
            drops.append(txt2value(line_split[11*i+7]))
            transformations.append(txt2value(line_split[11*i+8]))
            cartons_jaunes.append(txt2value(line_split[11*i+9]))
            cartons_rouges.append(txt2value(line_split[11*i+10]))
            minutes.append(txt2value(line_split[11*i+11]))

        # print(saisonList, club, competition, points, joues, titularisations, essais, penalites, drops, transformations, cartons_jaunes, cartons_rouges, minutes)

        resume_saison = []
        for i in range(len(saisonList)):
            compet = []
            compet.append(saisonList[i])
            compet.append(club[i])
            compet.append(competition[i])
            compet.append(points[i])
            compet.append(joues[i])
            compet.append(titularisations[i])
            compet.append(essais[i])
            compet.append(penalites[i])
            compet.append(drops[i])
            compet.append(transformations[i])
            compet.append(cartons_jaunes[i])
            compet.append(cartons_rouges[i])
            compet.append(minutes[i])
            resume_saison.append(compet)

        if bool_sp:
            saison = saison_prec
            bool_sp = False

        print(resume_saison)

# getJoueurBio(textBio)
getJoueurClubStat(textStat)
=======
def getJoueurStat(text):
    table = text.split("|Min.|",1)[1]
    table = table.split("|Copyright",1)[0]
    print(table)

    for line in table.splitlines():
        if len(line) < 8:
            saison = line.replace("|","")
        else:
            line_split = line.split("|")
            club = line_split[0]
            competition = line_split[1]
            points = txt2value(line_split[2])
            joues = txt2value(line_split[3])
            titularisations = txt2value(line_split[4])
            essais = txt2value(line_split[5])
            penalites = txt2value(line_split[6])
            drops = txt2value(line_split[7])
            transformations = txt2value(line_split[8])
            cartons_jaunes = txt2value(line_split[9])
            cartons_rouges = txt2value(line_split[10])
            minutes = txt2value(line_split[11])
            if len(line_split) == 14: #Ligne du premier club dans la saison
                saison_prec = line_split[13]
            elif len(line_split) == 25: #Ligne avec deux compétitions



# getJoueurBio(textBio)
getJoueurStat(textStat)
>>>>>>> origin/master
