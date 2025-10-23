#python-03-controle-premiers.py

from math import sqrt

def premier(n: int) -> bool:
    """
    Vérifie si un entier n est premier ou non.

    :param n: L'entier dont on veut vérifier la primalité.
    :type n: int
    :return: Un booléen indiquant si n est premier.
    :rtype: bool
    :raise ValueError: n est plus petit que 2.

    >>> premier(25)
    25 = 5 x 5 : False
    False
    >>> premier (3)
    3 : True
    True
    >>> premier (-10)
    Traceback (most recent call last):
        ...
    ValueError: n devrait être plus grand que 2
    """

    # On vérifie que n est supérieur à 1, afin que le test ait un sens.
    if n < 2:
        raise ValueError("n devrait être plus grand que 2")

    print(n, end=" ")

    p = True

    # On ne parcourt les nombres que de 2 à la racine carrée de n
    for i in range(2, int(sqrt(n)) + 1):
        # Si n est divisible par i, alors il n'est pas premier
        if n % i == 0:
            p = False
            print("= " + str(i) + " x " + str(n // i), end=" ")
            break

    print(": " + str(p))

    return p

def main():
    premier(int(input("Entrez un nombre entier > 1\n")))

if __name__ == '__main__':
    main()