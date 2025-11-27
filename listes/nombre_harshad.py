def is_harshad(n: int) -> bool:
    """Retourne la vérité de "n est un nombre de Harshad"

    :param n: entier à tester
    :type n: int
    :returns: True si n est un nombre de Harshad, False sinon
    :rtype: bool

    >>> [ is_harshad(i) for i in [12, 14, 18, 19, 20, 21, 24, 26, 27] ]
    [True, False, True, False, True, True, True, False, True]
    """
    return n%sum(int(i) for i in str(n)) == 0

def main():
    not_finished = True
    while not_finished:
        user_input = input("Entrez un nombre entier positif ")
        try:
            n_hashard = is_harshad(int(user_input))
            if n_hashard:
                print(f"{user_input} est un nombre d'Hashard")
            else:
                print(f"{user_input} n'est pas un nombre d'Hashard")
            not_finished = False
        except ValueError:
            print(f"L'entrée {user_input} n'est pas valide")

if __name__ == '__main__':
    main()