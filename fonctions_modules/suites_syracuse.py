from typing import Tuple


def syracuse(n: int) -> Tuple[int, int, int]:
    """
    Une suite de Syracuse est une suite d'entiers naturels définie de la manière suivante :
    on part d'un nombre entier strictement positif ; s’il est pair, on le divise par 2 ;
    s’il est impair, on le multiplie par 3 et l'on ajoute 1.
    En répétant l’opération, on obtient une suite d'entiers strictement positifs dont chacun ne dépend
    que de son prédécesseur.

    Par exemple, à partir de 14, on construit la suite des nombres :
    14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1, 4, 2, 1 et ainsi de suite.
    C'est la suite de Syracuse du nombre 14. Après que le nombre 1 a été atteint, la suite des valeurs 1, 4, 2, 1, 4, 2…
    se répète indéfiniment en un cycle de longueur 3, appelé cycle trivial.

    Pour en savoir plus : https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse

    :param n: Le nombre entier
    :type n: int
    :return: Un tuple contenant le temps de vol, l'altitude maximale et le temps de vol en altitude
    :rtype: Tuple[int, int, int]

    >>> syracuse(15)
    (17, 160, 10)
    >>> syracuse(127)
    (46, 4372, 23)
    """

    # Initialisation des variables
    uk = n
    tv = 0
    am = n
    tva = 0
    tva_fixe= False

    # Tant que la suite n'est pas terminée
    while uk!=1:
        # Calcul du n suivant
        uk = (uk // 2) if (uk % 2 == 0) else (uk * 3 + 1)

        # Mise à jour du temps de vol (tv)
        tv+=1

        # Mise à jour de l'altitude maximale (am)
        if uk > am: am = uk

        # Mise à jour du temps de vol en altitude (tva) si nécessaire
        if not tva_fixe:
            if uk >= n:
                tva = tv
            else:
                tva_fixe = True

    # Retour de tv, tva, am
    return tv, am, tva


def main():
    n = 0
    while n <= 0:
        try:
            s_input = input("Veuillez entrer un entier strictement positif : ")
            n = int(s_input)
            if n <= 0:
                print("Erreur : Le nombre doit être supérieur à 0.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide.")

    tv, am, tva = syracuse(n)

    print(f"\n--- Résultats pour n = {n} ---")
    print(f"Temps de vol             : {tv}")
    print(f"Altitude maximale        : {am}")
    print(f"Temps de vol en altitude : {tva}")

if __name__ == "__main__":
    main()