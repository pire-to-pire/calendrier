import datetime
from itertools import zip_longest
from typing import List


def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


class Calendrier:
    taille = 20

    def __init__(self, moment: datetime.datetime, **kwargs):
        self.moment = moment

    def __str__(self):
        return self.titre()

    def calendrier(self) -> List[str]:
        liste = self.debut()
        liste.extend(self.milieu())
        liste.extend(self.fin())
        return liste

    def calendrier_str(self) -> str:
        return "\n".join(self.calendrier())

    def debut(self) -> List[str]:
        return [self.titre(), self.barre_jours()]

    def milieu(self) -> List[str]:
        mois = []
        semaine = self.espaces()
        for loop in range(1, int(self.dernier_jour_mois().day) + 1):
            if self.milieu_taille_semaine(semaine):
                self.milieu_semaine_str(mois, semaine)
                semaine = []
            self.milieu_semaine(semaine, loop)
        mois.append(" ".join(semaine) + "   " * (7 - len(semaine)))
        return mois

    def milieu_semaine(self, semaine: List[str], jour: int) -> List[str]:
        semaine.append(self.jour_str(jour))
        return semaine

    def milieu_taille_semaine(self, semaine: List[str]):
        if len(semaine) > 6:
            return True
        else:
            return False

    def milieu_semaine_str(self, mois: List[str], semaine: List[str]):
        return mois.append(" ".join(semaine))

    def fin(self) -> List[str]:
        return [self.barre_jours()]

    def jour_str(self, jour: int) -> str:
        return str(jour).zfill(2)

    def nombre_espaces(self) -> int:
        return self.premier_jour_mois().weekday()

    def espaces(self) -> List[str]:
        semaine = []
        for loop in range(self.nombre_espaces()):
            semaine.append("  ")
        return semaine

    def dernier_jour_mois(self) -> datetime.datetime:
        month_plus_un = self.moment.month % 12 + 1
        premier_mois_suivant = self.moment.replace(month=month_plus_un, day=1)
        return premier_mois_suivant - datetime.timedelta(days=1)

    def titre(self) -> str:
        nommoisdico = {1: "Janvier", 2: "Février", 3: "Mars", 4: "Avril", 5: "Mai", 6: "Juin",
                       7: "Juillet", 8: "Août", 9: "Septembre", 10: "Octobre", 11: "Novembre",
                       12: "Décembre"}
        return nommoisdico[self.moment.month].center(self.taille)

    def barre_jours(self) -> str:
        return "Lu Ma Me Je Ve Sa Di"

    def premier_jour_mois(self) -> datetime.datetime:
        return self.moment.replace(day=1)

    def calendrier_mois_suivant(self) -> 'Calendrier':
        return type(self)(self.moment + datetime.timedelta(days=30))


class CalendrierColor(Calendrier):
    def __init__(self, moment, coloring: bool = True, **kwargs):
        super().__init__(moment)
        self.coloring = coloring

    def calendrier_mois_suivant(self) -> 'Calendrier':
        calendrier = super().calendrier_mois_suivant()
        calendrier.coloring = False
        return calendrier

    def jour_str(self, jour: int) -> str:
        if jour == self.moment.day and self.coloring:
            return '\033[36m' + super().jour_str(jour) + '\033[0m'
        else:
            return super().jour_str(jour)


class CalendrierBorder(Calendrier):
    taille = 22

    def barre_jours(self) -> str:
        return "│" + super().barre_jours() + "│"

    def debut(self):
        return [self.titre(), "┌" + "─" * 20 + "┐", self.barre_jours()]

    def fin(self):
        return [self.barre_jours(), "└" + "─" * 20 + "┘"]

    def milieu(self) -> List[str]:
        liste = []
        for element in super().milieu():
            liste.append("│" + element + "│")
        return liste


class CalendrierBold(Calendrier):

    def jour_str(self, jour: int) -> str:
        date_jour = datetime.datetime(self.moment.year, self.moment.month, jour)
        if date_jour.isoweekday() == 6 or date_jour.isoweekday() == 7:
            return '\033[1m' + str(super().jour_str(jour)) + '\033[0m'
        else:
            return str(super().jour_str(jour))


class CalendrierMix1(CalendrierBorder, CalendrierColor):
    pass


class CalendrierMix2(CalendrierBorder, CalendrierColor, CalendrierBold):
    pass


class Ephemeride:
    calendar_class = CalendrierMix2

    def __init__(self, moment):
        self.moment = moment
        self.nombredecal = 4
        self.nombredespaces = 4
        self.longueur = self.nombredespaces * (self.nombredecal - 1) + self.calendar_class.taille * self.nombredecal

    def get_calendar_list(self) -> List['Calendrier']:
        liste = []
        for mois in range(1, 13):
            if mois == self.moment.month:
                cal = self.calendar_class(moment=self.moment)
            else:
                cal = self.calendar_class(moment=self.moment.replace(month=mois, day=1), coloring=False)
            liste.append(cal)
        return liste

    def calendriers(self, liste: list['Calendrier']) -> List[str]:
        listeglobale = [" " * self.longueur, self.titre()]
        for listedecal in grouper(liste, self.nombredecal, fillvalue=None):
            listedelistedeligne = []
            for cal in listedecal:
                if cal is not None:
                    listedelistedeligne.append(cal.calendrier())
            for listedeNelements in zip_longest(*listedelistedeligne, fillvalue=" " * self.calendar_class.taille):
                listeglobale.append((" " * self.nombredespaces).join(listedeNelements))
        return listeglobale

    def calendriers_str(self, liste: list['Calendrier']) -> str:
        return "\n".join(self.calendriers(liste))

    def titre(self) -> str:
        taille = self.longueur
        return str(self.moment.year).center(taille)


class EphemerideBordure(Ephemeride):

    def barre_haut(self) -> str:
        barre = "─"
        return "┌" + barre * self.longueur + "┐"

    def barre_bas(self) -> str:
        barre = "─"
        return "└" + barre * self.longueur + "┘"

    def calendriers(self, liste: list['Calendrier']) -> List[str]:
        listeglobalebordure = [self.barre_haut()]
        for lignes in super().calendriers(liste):
            listeglobalebordure.append("│" + lignes + "│")
        listeglobalebordure.append(self.barre_bas())
        return listeglobalebordure


eph = EphemerideBordure(datetime.datetime.now())
cal1 = CalendrierMix2(moment=datetime.datetime.now())

print(eph.calendriers_str(eph.get_calendar_list()))