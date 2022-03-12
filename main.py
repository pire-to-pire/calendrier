from datetime import *


def calendrier():
    class Color:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'
    dateactuelle = date.today()
    nommoisdico = {"01": "Janvier", "02": "Février", "03": "Mars", "04": "Avril", "05": "Mai", "06": "Juin",
                   "07": "Juillet", "08": "Août", "09": "Septembre", "10": "Octobre", "11": "Novembre",
                   "12": "Décembre", }
    dateactuelleliste = dateactuelle.split("-")
    taille = taillemoisdico[dateactuelleliste[1]]
    mois = nommoisdico[dateactuelleliste[1]]
    mois = mois.center(20)
    jour1annee = premierjourannee(dateactuelleliste[0])
    jour1mois = premierjourmois(dateactuelleliste[0], dateactuelleliste[1], jour1annee)
    debut = (int(jour1mois)) - 1
    compteurdecolonnes = debut
    print(mois)
    print("")
    print("Lu Ma Me Je Ve Sa Di")
    for vides in range(0, debut):
        print(end="   ")
    for loop in range(1, taille + 1):
        if dateactuelleliste[2] != (str(loop)).zfill(2):
            print(str(loop).zfill(2), end=" ")
        else:
            print(Color.DARKCYAN + str(loop).zfill(2) + Color.END, end=" ")
        compteurdecolonnes += 1
        if compteurdecolonnes == 7 and loop != taille:
            compteurdecolonnes = 0
            print("")
    print("")
    print("Lu Ma Me Je Ve Sa Di")


calendrier()
