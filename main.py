"""
Auteur : Enis Béziau [1H]
Permet à l'utilisateur de convertir un nombre écrit dans une base quelconque de [2 ; 16] et de le convertir dans
une base quelconque de [2 ; 16].
L'utilisateur peut également taper 's'' pour écrire le nombre de départ ou convertir le nombre d'arrivée en shadok
"""

conversion_lettres = 'ABCDEF'


def quelconque_vers_base_10(nombre: str, base_depart: int) -> int:
    """
    Prend en argument un nombre (sous la forme d'une str) écrit dans la base correspondante au 2e argument `base_depart`
    Renvoie un entier, le nombre écrit en base 10
    """
    resultat = 0
    for puissance, cara in enumerate(nombre[::-1]):  # inverse la chaine car on doit parcourir à l'envers
        if cara.isalpha():
            resultat = (10 + conversion_lettres.index(cara)) * base_depart ** puissance + resultat
        else:
            resultat = int(cara) * base_depart ** puissance + resultat
    return resultat


# Jeu de tests
assert quelconque_vers_base_10("123", 5) == 38
assert quelconque_vers_base_10("10", 8) == 8
assert quelconque_vers_base_10("0101010101", 2) == 341
assert quelconque_vers_base_10('0', 13) == 0
assert quelconque_vers_base_10("ABCDEF", 16) == 11_259_375
assert quelconque_vers_base_10("18A407", 11) == 291_980


def base_10_vers_quelconque(nombre: int, base_arrivee: int) -> str:
    """
    Prend en paramètre un entier écrit en base 10 et la base dans laquelle il faut la convertir
    Renvoie une chaine de caractères donnant l'écriture base `base_arrivee` de `nombre`
    """
    if nombre == 0:  # 0 vaut 0 pour toute base, on renvoie donc '0' pour éviter de renvoyer ''
        return '0'
    nbr_a_modif = nombre  # copie de l'argument car on a besoin de modifier ce nombre et avoir une fonction pure
    result = ''
    while nbr_a_modif > 0:
        reste_division_euclidienne = nbr_a_modif % base_arrivee
        if reste_division_euclidienne >= 10:
            # Vu que reste ≥ 10 ; reste - 10 ≥ 0 donc on peut faire correspondre avec la tab de conversion
            result = str(conversion_lettres[reste_division_euclidienne - 10]) + result
        else:
            # Plutot que de += et de devoir inverser à la fin, on ajoute au début de la chaine la nouvelle chaine
            result = str(reste_division_euclidienne) + result
        nbr_a_modif //= base_arrivee
    return result


# jeu de tests
assert base_10_vers_quelconque(38, 5) == "123"
assert base_10_vers_quelconque(8, 8) == "10"
assert base_10_vers_quelconque(341, 2) == "101010101"
assert base_10_vers_quelconque(0, 13) == '0'
assert base_10_vers_quelconque(11_259_375, 16) == "ABCDEF"
assert base_10_vers_quelconque(291_980, 11) == "18A407"


def shadok_vers_base_4(expression_shadok: str) -> str:
    """
    Prend en paramètre une expression shadok composé de `ga` ; `bu` ; `zo` ; `meu` sous forme de chaine de cara
    Renvoie une chaine de caractère composé de l'écriture en base 4 de l'expression shadokienne donné en argument
    Le fonctionnement se base sur l'unicité des caractères des préfixes shadoks pour les convertir en base 4
    """
    expression_en_base_4 = ''
    for cara in expression_shadok:
        if cara == 'g':
            expression_en_base_4 += '0'
        elif cara == 'b':
            expression_en_base_4 += '1'
        elif cara == 'z':
            expression_en_base_4 += '2'
        elif cara == 'm':
            expression_en_base_4 += '3'
    return expression_en_base_4


# jeu de tests
assert shadok_vers_base_4("ga") == '0'
assert shadok_vers_base_4("bu") == '1'
assert shadok_vers_base_4("zo") == '2'
assert shadok_vers_base_4("meu") == '3'
assert shadok_vers_base_4("gagagagabugagaga") == "00001000"
assert shadok_vers_base_4("meubugazomeumeu") == "310233"
assert shadok_vers_base_4("bumeubugabu") == "13101"
assert shadok_vers_base_4("gagagagaga") == '00000'


def base_4_vers_shadok(nombre: str) -> str:
    """
    Prend en paramètre un nombre (sous la forme d'une str) écrit en base 4
    Renvoie une chaine de caractère composé du nombre en base 4 écrit en shadok
    """
    expression_shadok = ''
    for cara in nombre:
        if cara == '0':
            expression_shadok += "ga"
        elif cara == '1':
            expression_shadok += "bu"
        elif cara == '2':
            expression_shadok += "zo"
        elif cara == '3':
            expression_shadok += "meu"
    return expression_shadok


# jeu de tests
assert base_4_vers_shadok('0') == "ga"
assert base_4_vers_shadok('1') == "bu"
assert base_4_vers_shadok('2') == "zo"
assert base_4_vers_shadok('3') == "meu"
assert base_4_vers_shadok("00001000") == "gagagagabugagaga"
assert base_4_vers_shadok("310233") == "meubugazomeumeu"
assert base_4_vers_shadok("13101") == "bumeubugabu"
assert base_4_vers_shadok('00000') == "gagagagaga"


def main() -> None:
    """
    Fonction lançant la récolte des infos auprès de l'utilisateur
    Renvoie None
    """
    while True:
        base_depart = input("Veuillez entrer la base de départ du nombre à convertir (2 ≤ base ≤ 16)\n==> ")
        # Pas de conversion en entier car l'entrée peut etre composé de lettres majuscules pour les bases ≥ 10
        nombre_depart = input("Veuillez entrer le nombre à convertir\n==> ")
        base_voulue = input("Veuillez entrer la base dans laquelle le nombre entré doit etre convertit \n==> ")

        print(f"Le nombre {nombre_depart} base {base_depart} convertit en base {base_voulue} vaut ", end='')

        if base_depart == base_voulue:
            print(nombre_depart)
        elif base_depart == 's':
            expression_en_base_4 = shadok_vers_base_4(nombre_depart)
            print(quelconque_vers_base_10(expression_en_base_4, 4))
        elif base_voulue == 's':
            nombre_base_10 = quelconque_vers_base_10(nombre_depart, int(base_depart))
            nombre_base_4 = base_10_vers_quelconque(nombre_base_10, 4)
            print(base_4_vers_shadok(nombre_base_4))
        else:
            if base_depart == 10:
                print(base_10_vers_quelconque(int(nombre_depart), int(base_voulue)))
            elif base_voulue == 10:
                print(quelconque_vers_base_10(nombre_depart, int(base_depart)))
            else:
                nbr_base_10 = quelconque_vers_base_10(nombre_depart, int(base_depart))
                print(base_10_vers_quelconque(nbr_base_10, int(base_voulue)))

        return None


if __name__ == '__main__':
    main()
