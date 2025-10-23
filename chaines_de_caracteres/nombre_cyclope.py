def is_cyclope(n):
    """retourne la vérité de "n est un nombre cyclope"

    :param n: nombre à tester
    :type n: int
    :returns: True si "n est un nombre cyclope". False sinon
    :rtype: bool

    >>> n = 1230456
    >>> is_cyclope(n)
    True
    >>> n = 1237456
    >>> is_cyclope(n)
    False
    >>> n = 120056
    >>> is_cyclope(n)
    False
    """
    n_string = str(n)
    longueur_n = len(n_string)
    longueur_est_impaire = longueur_n%2==1
    a_zero_au_milieu = n_string[longueur_n//2] == '0'
    return longueur_est_impaire and a_zero_au_milieu


def main():
    user_input = input("Entrez un nombre entier > 0 ")
    try:
        number = int(user_input)
        print(number, end=" ")
        if is_cyclope(number):
            print("est un nombre cyclope")
        else:
            print("n'est pas un nombre cyclope")
    except ValueError as e:
        print(f"L'entrée {user_input} n'est pas bonne. {e}")


if __name__ == "__main__":
    main()