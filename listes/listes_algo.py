from typing import Tuple

def mini(l: list[int]) -> int:
    """
    Renvoie le minimum d'une liste de nombres

    :param l: La liste de nombres
    :type l: list[int]
    :return: Le minimum de la liste
    :rtype: int
    :raise ValueError: Si la liste est vide

    >>> mini([1, 5, 2, 8, 3])
    1
    >>> mini([-10, -5, -1, -20])
    -20
    >>> mini([42])
    42
    >>> mini([5, 5, 5])
    5
    >>> mini([])
    Traceback (most recent call last):
        ...
    ValueError: La liste est vide
    """
    longueur_l = len(l)
    if longueur_l == 0:
        raise ValueError("La liste est vide")

    minimum = l[0]
    for number in l[1:]:
        if number < minimum:
            minimum = number
    return minimum

def maxi(l: list[int]) -> int:
    """
    Renvoie le maximum d'une liste de nombres

    :param l: La liste de nombres
    :type l: list[int]
    :return: Le maximum de la liste
    :rtype: int
    :raise ValueError: Si la liste est vide

    >>> maxi([1, 5, 2, 8, 3])
    8
    >>> maxi([-10, -5, -1, -20])
    -1
    >>> maxi([42])
    42
    >>> maxi([10, -5, 0, 20, 15])
    20
    >>> maxi([])
    Traceback (most recent call last):
        ...
    ValueError: La liste est vide
    """
    longueur_l = len(l)
    if longueur_l == 0:
        raise ValueError("La liste est vide")

    maximum = l[0]
    for number in l[1:]:
        if number > maximum:
            maximum = number
    return maximum

def ind_mini(l: list[int]) -> int:
    """
    Retourne l'indice de la première occurrence du nombre minimum de la liste

    :param l: La liste de nombres
    :type l: list[int]
    :return: L'indice du minimum
    :rtype: int
    :raise ValueError: Si la liste est vide

    >>> ind_mini([1, 5, 2, 8, 3])
    0
    >>> ind_mini([10, 5, 2, 8, 3])
    2
    >>> ind_mini([-10, -5, -1, -20])
    3
    >>> ind_mini([5, 2, 1, 8, 1])
    2
    >>> ind_mini([42])
    0
    >>> ind_mini([])
    Traceback (most recent call last):
        ...
    ValueError: La liste est vide
    """
    l_min = mini(l)
    indice_du_minimum = l.index(l_min)
    return indice_du_minimum


def ind_maxi(l: list[int]) -> int:
    """
    Retourne l'indice de la première occurrence du nombre maximum de la liste

    :param l: La liste de nombres
    :type l: list[int]
    :return: L'indice du maximum
    :rtype: int
    :raise ValueError: Si la liste est vide

    >>> ind_maxi([1, 5, 2, 8, 3])
    3
    >>> ind_maxi([10, 5, 2, 8, 3])
    0
    >>> ind_maxi([-10, -5, -1, -20])
    2
    >>> ind_maxi([5, 9, 2, 8, 9])
    1
    >>> ind_maxi([42])
    0
    >>> ind_maxi([])
    Traceback (most recent call last):
        ...
    ValueError: La liste est vide
    """
    l_max = maxi(l)
    indice_du_maximum = l.index(l_max)
    return indice_du_maximum

def somme(l: list[int]) -> int:
    """
    Retourne la somme des éléments d'une liste

    :param l: La liste d'entiers
    :type l: list[int]
    :return: La somme (0 si la liste est vide)
    :rtype: int

    >>> somme([1, 2, 3, 4, 5])
    15
    >>> somme([-1, -2, 5, 10])
    12
    >>> somme([42])
    42
    >>> somme([0, 0, -1, 1])
    0
    >>> somme([])
    0
    """
    s = 0
    for number in l:
        s += number
    return s

def moyenne(l: list[int]) -> float:
    """
    Retourne la moyenne des éléments dans une liste d'entiers

    :param l: La liste d'entiers
    :type l: list[int]
    :return: La moyenne
    :rtype: float
    :raise ValueError: Si la liste est vide

    >>> moyenne([1, 2, 3, 4, 5])
    3.0
    >>> moyenne([10, 20, 30])
    20.0
    >>> moyenne([1, 2])
    1.5
    >>> moyenne([42])
    42.0
    >>> moyenne([])
    Traceback (most recent call last):
        ...
    ValueError: La liste est vide
    """
    somme_l = somme(l)
    longueur_l = len(l)
    if longueur_l == 0:
        raise ValueError("La liste est vide")
    moyenne_l = somme_l/longueur_l
    return moyenne_l

def est_trie(l: list[int]) -> int:
    """
    Permet de savoir si une liste d'entiers est croissante, décroissante ou ni l'un ni l'autre

    :param l: La liste d'entiers
    :type l: list[int]
    :return: 1 si la liste est croissante ou constante, -1 si elle est décroissante et 0 sinon.
    :rtype: int

    >>> L = [33, 36, 27, 15, 43, 35, 36, 42, 49, 21]
    >>> est_trie(L)
    0
    >>> L = [15, 21, 27, 33, 35, 36, 36, 42, 43, 49]
    >>> est_trie(L)
    1
    >>> L = [49, 43, 42, 36, 36, 35, 33, 27, 21, 15]
    >>> est_trie(L)
    -1
    """
    longueur_l = len(l)
    if longueur_l < 2:
        return 0

    # On cherche à savoir si la suite peut être croissante et / ou décroissante
    peut_etre_croissant = True
    peut_etre_decroissant = True

    for i in range(0,longueur_l-1):
        if l[i] > l[i+1]:
            peut_etre_croissant = False
        elif l[i] < l[i+1]:
            peut_etre_decroissant = False

    if peut_etre_croissant:
        return 1
    if peut_etre_decroissant:
        return -1
    return 0

# TODO: implement pplslc, doublons, elts_communs, elts_differents, pplsltc, np, pslsm

def pplslc(l: list[int]) -> Tuple[int, int]:
    pass

def doublons(l: list[int]) -> list[int]:
    pass

def elts_communs(l1: list[int], l2: list[int]) -> list[int]:
    pass

def elts_differents(l1: list[int], l2: list[int]) -> list[int]:
    pass

def pplsltc(l: list[int]) -> Tuple[int, int]:
    pass

def np(l: list[int]) -> int:
    pass

def pslsm(l: list[int]) -> Tuple[int, int]:
    pass

def main():
    pass

if __name__ == '__main__':
    main()