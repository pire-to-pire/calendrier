def chamallows(debut: int, mort: int, chparj: int, multiplicateur: float) -> tuple[int,int] :
    nbcham = 1
    j = 0
    debutj = debut * 365
    mortj = mort * 365
    while chparj * nbcham < mortj - j:
        nbcham *= multiplicateur
        j += 1
    Ran = j // 365
    Rj = j % 365
    return Ran, Rj


print(chamallows(13, 100, 3, 1.2))

