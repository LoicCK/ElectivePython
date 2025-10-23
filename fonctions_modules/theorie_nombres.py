from controle_execution.controle_premiers import premier

def fermat(n: int) -> int:
    """
    Un nombre de Fermat est un nombre qui peut s’écrire sous la forme 2^(2^n)+1, avec n un entier naturel.
    Pour en savoir plus : https://fr.wikipedia.org/wiki/Nombre_de_Fermat

    :param n: L'entier dont on veut calculer le nombre de Fermat.
    :type n: int
    :return: Le nombre de Fermat de n.
    :rtype: int

    >>> fermat(0)
    3
    >>> fermat(1)
    5
    >>> fermat(2)
    17
    >>> fermat(3)
    257
    >>> fermat(4)
    65537
    >>> fermat(5)
    4294967297
    """
    f_n = 2**(2**n) + 1
    return f_n

def first_non_prime_fermat() -> int:
    """
    Permet d'avoir le premier nombre de Fermat non premier.

    :return: Le premier nombre de Fermat non premier.
    :rtype: int

    >>> first_non_prime_fermat()
    4294967297
    """
    n = 0
    while True:
        f_n = fermat(n)
        # Permet de savoir si Fn est premier ou non
        f_n_non_premier = not premier(f_n)
        if f_n_non_premier:
            return f_n
        n+=1

def next_prime(n: int) -> int:
    """
    Permet d'avoir le premier entier premier n' tel que n' > n.

    :param n: Le nombre n
    :type n: int
    :return: Le nombre n'
    :rtype: int

    >>> next_prime(1)
    2
    >>> next_prime(2)
    3
    >>> next_prime(7)
    11
    >>> next_prime(10)
    11
    >>> next_prime(20)
    23
    """
    if n < 2:
        return 2
    # Nous voulons le prochain nombre premier, qui est forcément impair
    if n%2==0:
        n+=1
    else:
        n+=2
    while True:
        n_est_premier = premier(n)
        if n_est_premier:
            return n
        n+=2

def couple_prime_after(n: int) -> int:
    """
    Deux nombres premiers jumeaux sont deux nombres premiers qui ne diffèrent que de 2.
    Cette fonction permet d'avoir le premier élément du couple (n', n'') tel que n<n'<n'' .
    Pour en savoir plus : https://fr.wikipedia.org/wiki/Nombres_premiers_jumeaux

    :param n: Le nombre n
    :type n: int
    :return: Le nombre n'
    :rtype: int

    >>> couple_prime_after(1)
    3
    >>> couple_prime_after(3)
    5
    >>> couple_prime_after(5)
    11
    >>> couple_prime_after(7)
    11
    >>> couple_prime_after(20)
    29
    """
    while True:
        n = next_prime(n)
        next_n_est_premier = premier(n + 2)
        if next_n_est_premier:
            return n

def germain_prime_after(n: int) -> int:
    """
    Un nombre premier G est appelé nombre premier de Sophie Germain si 2*G+1 est aussi un nombre premier.
    Cette fonction permet d'avoir le premier nombre premier G tel que G > n.
    Pour en savoir plus : https://fr.wikipedia.org/wiki/Nombre_premier_de_Sophie_Germain
    :param n: Le nombre n
    :type n: int
    :return: Le nombre premier G
    :rtype: int
    """
    while True:
        n = next_prime(n)
        n_s_g_est_premier = premier(2 * n + 1)
        if n_s_g_est_premier:
            return n


def main():
     # Couple examples
    print(fermat(5))
    print(first_non_prime_fermat())
    print(next_prime(100000))
    print(couple_prime_after(100000))
    print(germain_prime_after(100000))


if __name__ == "__main__":
    main()