def is_happy(n: int, historique=None) -> bool:
    """
    Retourne la vérité de "n est un nombre heureux
    Pour en savoir plus : https://fr.wikipedia.org/wiki/Nombre_heureux

    :param n: entier à tester
    :param historique: l'historique des nombres testés, afin de ne pas tomber dans une boucle infinie
    :type n: int
    :returns: True si n est un nombre heureux, False sinon
    :rtype: bool

    >>> [i for i in range(10,40) if is_happy(i) ]
    [10, 13, 19, 23, 28, 31, 32]
    >>> [i for i in range(310,340) if is_happy(i) ]
    [310, 313, 319, 320, 326, 329, 331, 338]
    """
    if historique is None:
        historique = []
    elif n in historique:
        return False
    if n == 1:
        return True
    return is_happy(sum([int(i)**2 for i in str(n)]), historique+[n])

def main():
    not_finished = True
    while not_finished:
        user_input = input("Rentrez un nombre entier positif ")
        try:
            if is_happy(int(user_input)):
                print(f"{user_input} est un nombre heureux")
            else:
                print(f"{user_input} n'est pas un nombre heureux")
            not_finished = False
        except ValueError:
            print("L'entrée n'est pas valide")

if __name__ == '__main__':
    main()