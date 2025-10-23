from math import sqrt
from typing import Tuple, Optional
import functools

@functools.cache
def decomposer_en_facteurs(n: int) -> Tuple[bool, Optional[int]]:
    """
    Vérifie si un entier n est premier ou non.

    :param n: L'entier dont on veut vérifier la primalité.
    :type n: int
    :return: Un tuple (booléen, entier optionnel) indiquant si n est premier, et son éventuel premier diviseur.
    :rtype: Tuple[bool, Optional[int]]
    :raise ValueError: n est plus petit que 2.

>>> decomposer_en_facteurs(25)
    (False, 5)
    >>> decomposer_en_facteurs(3)
    (True, None)
    >>> decomposer_en_facteurs(2)
    (True, None)
    >>> decomposer_en_facteurs(97)
    (True, None)
    >>> decomposer_en_facteurs(100)
    (False, 2)
    >>> decomposer_en_facteurs (-10)
    Traceback (most recent call last):
        ...
    ValueError: n devrait être plus grand que 1
    """

    # On vérifie que n est supérieur à 1, afin que le test ait un sens.
    if n < 2:
        raise ValueError("n devrait être plus grand que 1")

    if n==2:
        return True, None

    if n%2 == 0:
        return False, 2

    # On ne parcourt les nombres que de 2 à la racine carrée de n
    for i in range(3, int(sqrt(n)) + 1, 2):
        # Si n est divisible par i, alors il n'est pas premier
        if n % i == 0:
            return False, i

    return True, None

def premier(n: int) -> int:
    """
    Permet de savoir si n est un premier ou non.

    :param n: L'entier n.
    :type n: int
    :return: Un booléen indiquant si n est premier.
    :rtype: bool

    >>> premier(25)
    False
    >>> premier(3)
    True
    >>> premier(2)
    True
    >>> premier(97)
    True
    >>> premier(100)
    False
    >>> premier(-10)
    Traceback (most recent call last):
        ...
    ValueError: n devrait être plus grand que 1
    """
    return decomposer_en_facteurs(n)[0]

def main():
    entree = input("Entrez un nombre entier > 1\n")
    try:
        nombre = int(entree)
        est_premier, diviseur = decomposer_en_facteurs(nombre)

        print(f"{nombre}",end=" ")

        if not est_premier:
            print(f"= {diviseur} x {nombre // diviseur}", end=" ")
        print(f": {str(est_premier)}")
    except ValueError as e:
        print(f"L'entrée {entree} n'est pas bonne. {e}")


if __name__ == '__main__':
    main()