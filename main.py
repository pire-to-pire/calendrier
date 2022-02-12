def calendrier(taille, debut, mois):
    X = 0
    compteurdecolonnes = 0
    compteurdecolonnes = debut
    mois=mois.center(20)
    print(mois)
    print("")
    print("Lu Ma Me Je Ve Sa Di")
    for vides in range(0, debut):
        print(end="   ")
    for loop in range(1, taille + 1):
        print(str(loop).zfill(2), end=" ")
        compteurdecolonnes += 1
        if compteurdecolonnes == 7:
            compteurdecolonnes = 0
            print("")
    print("")
    print("Lu Ma Me Je Ve Sa Di")

calendrier(28,4,"Janvier")
