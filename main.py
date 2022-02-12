X = 0
compteurdecolonnes=0
taille = 31
debut=6
#debut=(debut-1)
print("Lu Ma Me Je Ve Sa Di")
for vides in range (0,debut):
    print(end="   ")
for semaine in range(1, (taille + 6) // 7 + 1):
    for jours in range(X + 1, X + 8):
        string_jours = str(jours) + " "
        string_jours = string_jours.zfill(3)
        if jours > taille:
            string_jours = ""
        print(string_jours, end="")
    print("")
    X = jours
print("Lu Ma Me Je Ve Sa Di")
