def is_magic(n: int) -> int:
    """retourne la vérité de "n est un nombre magique"

    :param n: nombre entier à tester
    :type n: int
    :returns: True si "n est un nombre magique". False sinon
    :rtype: bool


    >>> n = 1089
    >>> is_magic(n)
    True
    >>> n = 8019
    >>> is_magic(n)
    False
    >>> n = 10989
    >>> is_magic(n)
    True
    >>> n = 10898
    >>> is_magic(n)
    False
    >>> n = 109989
    >>> is_magic(n)
    True
    >>> n = 108898
    >>> is_magic(n)
    False
    >>> n = 1099989
    >>> is_magic(n)
    True
    >>> n = 1088898
    >>> is_magic(n)
    False
    >>> n = 10891089
    >>> is_magic(n)
    True
    >>> n = 10981089
    >>> is_magic(n)
    False
    >>> n = 10999989
    >>> is_magic(n)
    True
    >>> n = 10999898
    >>> is_magic(n)
    False
    """
    string_n_multiple = str(n*9)
    return string_n_multiple == str(n)[::-1]

def next_magic(n: int, max_iterations = 10000) -> int:
    """
    Permet d'avoir le premier entier a > n tel que a est un nombre magique.

    :param n: Le nombre n
    :param max_iterations: Le nombre d'itérations maximum
    :type n: int
    :type max_iterations: int
    :return: Le nombre a (-1 si pas de nombres magiques dans ]n; n+max_iterations[
    :rtype: int

    >>> next_magic(0)
    1089
    >>> next_magic(1088)
    1089
    >>> next_magic(1089)
    10989
    >>> next_magic(10988)
    10989
    >>> next_magic(10989)
    -1
    >>> next_magic(10891088)
    10891089
    >>> next_magic(0, max_iterations=100)
    -1
    >>> next_magic(1088, max_iterations=1)
    -1
    >>> next_magic(1088, max_iterations=2)
    1089
    >>> next_magic(10989, max_iterations=100000)
    109989
    """
    for i in range(n+1, n+max_iterations):
        if is_magic(i):
            return i
    return -1

def main():
    print(is_magic(1))
    print(is_magic(1089))
    print(is_magic(8019))
    print(is_magic(10989))
    print(next_magic(1088))
    pass


if __name__ == "__main__":
    main()