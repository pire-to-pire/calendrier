X = 0
compteurdecolonnes = 0
taille = 31
debut = 6
compteurdecolonnes = debut
# debut=(debut-1)
print("Lu Ma Me Je Ve Sa Di")
for vides in range(0, debut):
    print(end="   ")
for loop in range(1,taille+1):
    print(str(loop).zfill(2), end=" ")
    compteurdecolonnes=compteurdecolonnes+1
    if compteurdecolonnes==7:
        compteurdecolonnes=0
        print("")
print("")
print("Lu Ma Me Je Ve Sa Di")
