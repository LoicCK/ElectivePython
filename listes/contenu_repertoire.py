import os

def scand(r):
    """
    Sépare les fichiers et les répertoires du répertoire passé en argument

    :param r: répertoire à analyser
    :type r: str
    :returns: Liste des noms de fichier sous forme de chaine de caractères, Liste des noms de répertoire sous forme de chaine de caractères
    :rtype: tuple(list, list)

    >>> f, d = scand('C:\\Windows')
    >>> isinstance(f, list) # vrai si f est une liste
    True
    >>> len(f) == 0
    False
    >>> isinstance(d, list) # vrai si d est une liste
    True
    >>> len(d) == 0
    False
    """
    f = []
    d = []

    contenu_du_dossier = os.scandir(r)

    for elt in contenu_du_dossier:
        elt_full_path = os.path.join(r, elt)
        if os.path.isfile(elt_full_path):
            f.append(elt.name)
        elif os.path.isdir(elt_full_path):
            d.append(elt.name)

    return f, d


def main():
    not_finished = True
    while not_finished:
        user_input = input("Entrez un chemin de dossier ")
        try:
            f, d = scand(user_input)
            print("--- Fichiers ---")
            print(f)
            print("\n--- Dossiers ---")
            print(d)
            not_finished = False
        except FileNotFoundError:
            print(f"\nERREUR : Le chemin '{user_input}' n'existe pas.")
        except NotADirectoryError:
            print(f"\nERREUR : Le chemin '{user_input}' est un fichier, pas un dossier.")
        except PermissionError:
            print(f"\nERREUR : Vous n'avez pas les droits pour lire '{user_input}'.")
        except OSError as e:
            print(f"\nERREUR SYSTÈME : Une erreur est survenue en accédant à ce chemin : {e}")
        if not_finished:
            print("Veuillez réessayer.\n")

    pass


if __name__ == '__main__':
    main()