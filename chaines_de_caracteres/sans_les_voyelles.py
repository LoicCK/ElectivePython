def remove_vowels_it(s):
    """Retire les voyelles de la chaîne de caractère passée en paramètre

    :param s: chaine de caractère à traiter
    :type s: str
    :returns: chaine de caractère privée de ses voyelles
    :rtype: str

    >>> s = "elephant"
    >>> remove_vowels_it(s)
    'lphnt'
    >>> s = "crocodile"
    >>> remove_vowels_it(s)
    'crcdl'
    >>> s = "girafe"
    >>> remove_vowels_it(s)
    'grf'
    >>> s = "phacochere"
    >>> remove_vowels_it(s)
    'phcchr'
    >>> s = "ornithorynque"
    >>> remove_vowels_it(s)
    'rnthrnq'
    """
    out = ""
    for c in s:
        if c in "aeiouy": continue
        out += c
    return out

def remove_vowels_rec(s):
    """Retire les voyelles de la chaîne de caractère passée en paramètre

    :param s: chaine de caractère à traiter
    :type s: str
    :returns: chaine de caractère privée de ses voyelles
    :rtype: str

    >>> s = "elephant"
    >>> remove_vowels_rec(s)
    'lphnt'
    >>> s = "crocodile"
    >>> remove_vowels_rec(s)
    'crcdl'
    >>> s = "girafe"
    >>> remove_vowels_rec(s)
    'grf'
    >>> s = "phacochere"
    >>> remove_vowels_rec(s)
    'phcchr'
    >>> s = "ornithorynque"
    >>> remove_vowels_rec(s)
    'rnthrnq'
    """
    if s=="":
        return ""
    c = s[0]
    if c in "aeiouy":
        return remove_vowels_it(s[1:])
    else:
        return c + remove_vowels_it(s[1:])

def main():
    pass
    s = "elephant"
    print(remove_vowels_it(s))

if __name__ == "__main__":
    main()