def ispalindrome(p: str) -> bool:
    """
    Permet de savoir si une chaîne de caractères est un palindrome
    :param p: La chaîne de caractères
    :type p: str
    :return: Un booléen indiquant si la chaîne est un palindrome
    :rtype: bool
    >>> ispalindrome("radar")
    True
    >>> ispalindrome("bonjour")
    False
    >>> ispalindrome("Ésope, reste ici et se repose !")
    True
    >>> ispalindrome("Engage le jeu que je le gagne")
    True
    >>> ispalindrome("")
    True
    """
    translation_table = str.maketrans('àâäéèêëîïôöûüç','aaaeeeeiioouuc')
    chaine_clean = p.lower().translate(translation_table)
    chaine_finale = ""
    for lettre in chaine_clean:
        if lettre.isalnum():
            chaine_finale+=lettre
    return chaine_finale == chaine_finale[::-1]


def main():
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()