def check_password(password):
    """
    Teste la robustesse d'un password

    :param password: chaine de caractères
    :type password: str
    :returns: True or False
    :rtype: bool

    >>> check_password('A1213pokl')
    False
    >>> check_password('bAse730onE')
    True
    >>> check_password('asasasasasasasaas')
    False
    >>> check_password('QWERTYqwerty')
    False
    >>> check_password('123456123456')
    False
    >>> check_password('QwErTy911poqqqq')
    True
    """

    est_assez_long = len(password) >= 10
    a_un_chiffre = any(c.isdecimal() for c in password)
    a_une_minuscule = password.upper() != password
    a_une_majuscule = password.lower() != password

    return est_assez_long and a_un_chiffre and a_une_minuscule and a_une_majuscule


def main():
    pw = input("Entrez un mdp : ")
    if check_password(pw):
        print(f"{pw} est un mot de passe robuste!")
    else:
        print(f"{pw} n'est pas un bon mot de passe!")


if __name__ == '__main__':
    main()