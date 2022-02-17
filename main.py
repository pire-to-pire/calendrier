# Ca sera utile : https://fr.wikipedia.org/wiki/Calendrier_gr%C3%A9gorien#Jour_de_l'an_des_ann%C3%A9es_normales
# pattern qui se repète sauf pour les années "rondes" (2100, 2200, ...)


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
    dateactuelle = str(date.today())
    nommoisdico = {"01": "Janvier", "02": "Février", "03": "Mars", "04": "Avril", "05": "Mai", "06": "Juin",
                   "07": "Juillet", "08": "Août", "09": "Septembre", "10": "Octobre", "11": "Novembre",
                   "12": "Décembre", }
    taillemoisdico = {"01": 31, "02": 28, "03": 31, "04": 30, "05": 31, "06": 30, "07": 31, "08": 31, "09": 30,
                      "10": 31, "11": 30, "12": 31, }
    dateactuelleliste = dateactuelle.split("-")
    taille = taillemoisdico.get(dateactuelleliste[1])
    mois = nommoisdico.get(dateactuelleliste[1])
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
            print(Color.BLUE + str(loop).zfill(2) + Color.END, end=" ")
        compteurdecolonnes += 1
        if compteurdecolonnes == 7 and loop != taille:
            compteurdecolonnes = 0
            print("")
    print("")
    print("Lu Ma Me Je Ve Sa Di")


def annee_bissextile(a):
    a = float(a)
    b = a / 4
    c = round(a / 4)
    if c != b:
        return False
    else:
        d = a / 100
        e = round(a / 100)
        if d != e:
            return True
        else:
            f = a / 400
            g = round(a / 400)
            if f != g:
                return False
            else:
                return True


def premierjourannee(annee):
    x = 0
    annee = float(annee)
    if annee_bissextile(annee) == False:
        if type(annee / 100) != int or type(annee - 5 / 100) != int or type(annee - 1 / 100) != int or type(
                annee - 9 / 100) != int:
            while (2000 + 28 * x) - annee > 28 or (2000 + 28 * x) - annee < 0:
                x += 1
            anneecle = 2000 + 28 * x
            x = 0
            x = anneecle - annee
            if x == 27 or x == 21 or x == 10:
                return "01"
            if x == 26 or x == 15 or x == 9:
                return "02"
            if x == 25 or x == 14 or x == 3:
                return "03"
            if x == 19 or x == 13 or x == 2:
                return "04"
            if x == 18 or x == 7 or x == 1:
                return "05"
            if x == 23 or x == 17 or x == 6:
                return "06"
            if x == 22 or x == 11 or x == 5:
                return "07"
        else:
            if type(annee / 100) == int:
                x = 0
                while (2000 + 100 * x) - annee > 100 or (2000 + 100 * x) - annee < 0:
                    x += 1
                jour = abs(7 - (2 * x))  # 7=Dimanche, 3=Mercredi, ...
                return jour
            elif type(annee - 1 / 100) == int:
                x = 0
                while (2000 + 100 * x) - annee - 1 > 100 or (2000 + 100 * x) - annee - 1 < 0:
                    x += 1
                jour = abs(6 - (2 * x))  # 7=Dimanche, 3=Mercredi, ...
                return jour
            elif type(annee - 5 / 100) == int:
                x = 0
                while (2000 + 100 * x) - annee - 5 > 100 or (2000 + 100 * x) - annee - 5 < 0:
                    x += 1
                jour = abs(4 - (2 * x))  # 7=Dimanche, 3=Mercredi, ...
                return jour
            elif type(annee - 9 / 100) == int:
                x = 0
                while (2000 + 100 * x) - annee - 9 > 100 or (2000 + 100 * x) - annee - 9 < 0:
                    x += 1
                jour = abs(2 - (2 * x))  # 7=Dimanche, 3=Mercredi, ...
                return jour
    else:
        x = 0
        while (2000 + 100 * x) - annee > 100 or (2000 + 100 * x) - annee < 0:
            x += 1
        anneecle = 2000 + 100 * x
        if anneecle - annee > 12:
            x = 0
            while (2000 + 4 * x) - annee > 4 or (2000 + 4 * x) - annee < 0:
                x += 1
            jour = abs(6 - (2 * x))  # 7=Dimanche, 3=Mercredi, ...
            return jour
        else:
            x = 0
            while (2000 + 100 * x) - annee > 100 or (2000 + 100 * x) - annee < 0:
                x += 1
            anneecle = 2000 + 100 * x
            if anneecle - annee == 12:
                jour = abs(7 - (2 * x))  # 7=Dimanche, 3=Mercredi, ...
                return jour
            elif anneecle - annee == 8:
                jour = abs(4 - (2 * x))  # 7=Dimanche, 3=Mercredi, ...
                return jour
            elif anneecle - annee == 4:
                jour = abs(2 - (2 * x))  # 7=Dimanche, 3=Mercredi, ...
                return jour


def premierjourmois(annee, mois, jour1annee):
    jour = 0
    jour1annee = int(jour1annee)
    if annee_bissextile(annee):
        if mois == "01":
            jour = jour1annee
        if mois == "02":
            jour = (jour1annee + 3) % 7
        if mois == "03":
            jour = (jour1annee + 4) % 7
        if mois == "04":
            jour = jour1annee
        if mois == "05":
            jour = (jour1annee + 2) % 7
        if mois == "06":
            jour = (jour1annee + 5) % 7
        if mois == "07":
            jour = jour1annee
        if mois == "08":
            jour = (jour1annee + 3) % 7
        if mois == "09":
            jour = (jour1annee + 6) % 7
        if mois == "10":
            jour = (jour1annee + 1) % 7
        if mois == "11":
            jour = (jour1annee + 4) % 7
        if mois == "12":
            jour = (jour1annee + 6) % 7
        return jour
    else:
        if mois == "01":
            jour = jour1annee
        if mois == "02":
            jour = (jour1annee + 3) % 7
        if mois == "03":
            jour = (jour1annee + 3) % 7
        if mois == "04":
            jour = (jour1annee + 6) % 7
        if mois == "05":
            jour = (jour1annee + 1) % 7
        if mois == "06":
            jour = (jour1annee + 4) % 7
        if mois == "07":
            jour = (jour1annee + 6) % 7
        if mois == "08":
            jour = (jour1annee + 2) % 7
        if mois == "09":
            jour = (jour1annee + 5) % 7
        if mois == "10":
            jour = jour1annee + 1
        if mois == "11":
            jour = (jour1annee + 3) % 7
        if mois == "12":
            jour = (jour1annee + 5) % 7
        return jour


calendrier()
