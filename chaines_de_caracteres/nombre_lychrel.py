def lychrel(n: int, max_iteration = 1000) -> int:
    """Retourne le nombre d'itérations nécessaires pour obtenir un nombre palindrome

    :param n: nombre entier soumis au processus de Lychrel
    :param max_iteration: le nombre d'itérations maximum
    :type n: int
    :type max_iteration: int
    :returns: le nombre d'itérations nécessaires pour obtenir un nombre palindrome
    :rtype: int

    >>> n = 50
    >>> lychrel(n)
    1
    >>> n = 55
    >>> lychrel(n)
    2
    >>> n = 59
    >>> lychrel(n)
    3
    >>> n = 69
    >>> lychrel(n)
    4
    >>> n = 79
    >>> lychrel(n)
    6
    >>> n = 89
    >>> lychrel(n)
    24
    >>> n = 107
    >>> lychrel(n)
    1
    >>> n = 108
    >>> lychrel(n)
    1
    >>> n = 109
    >>> lychrel(n)
    2
    """
    k = 0
    # On fixe un nombre d'itérations afin de limiter les crashs
    while k < max_iteration:
        k+=1
        string_n = str(n)
        # On inverse la string
        string_n_inversee = string_n[::-1]
        string_addition = str(n+int(string_n_inversee))
        # Si la string d'addition est égale à son inverse, alors elle est un palindrome
        if string_addition == string_addition[::-1]:
            return k
        n = int(string_addition)
    return -1

def main():
    # liste de nombres suspectés d'être des nombres de Lychrel
    x = [196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887, 978, 986]
    l = [ lychrel(i) for i in range(1,200) if i not in x ]
    print(l)
    print(lychrel(1186060307891929990))
    pass

if __name__ == "__main__":
    main()