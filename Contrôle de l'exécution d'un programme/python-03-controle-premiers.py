#python-03-controle-premiers.py

from math import sqrt
from typing import Tuple, Optional

def premier(n: int) -> Tuple[bool, Optional[int]]:
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

def main():
    nombre = int(input("Entrez un nombre entier > 1\n"))
    try:
        est_premier, diviseur = premier(nombre)

        print(f"{nombre}",end=" ")

        if not est_premier:
            print(f"= {diviseur} x {nombre // diviseur}", end=" ")
        print(f": {str(est_premier)}")
    except ValueError as e:
        print(f"L'entrée {nombre} n'est pas bonne. {e}")


if __name__ == '__main__':
    main()