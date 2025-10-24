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
    :raise ValueError: n est négatif.

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
    ValueError: n devrait être positif
    """

    # On vérifie que n est positif, afin que le test ait un sens.
    if n < 0:
        raise ValueError("n devrait être positif")

    if n < 2:
        return False, n
    if n==2 or n==3:
        return True, None
    if n%2 == 0:
        return False, 2
    if n%3 == 0:
        return False, 3

    i = 5
    while i*i <= n:
        if n%i == 0:
            return False, i
        if n%(i+2)==0:
            return False, i+2
        i+=6

    return True, None

def premier(n: int) -> bool:
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
    ValueError: n devrait être positif
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