from typing import List, Set
from listes.extensions import searchext

def searchext_unique(l: List[str]) -> Set[str]:
    """
    Identifie les extensions de la liste de fichiers passée en argument

    :param l: liste des noms de fichier sous forme de chaine de caractères
    :type l: list
    :returns: Liste des extensions sous forme de chaine de caractères
    :rtype: set

    >>> s = searchext_unique(['ARJ.PIF', 'atiogl.xml', 'ativpsrm.bin', 'bfsvc.exe'])
    >>> isinstance(s, set) # vrai si s est un set
    True
    >>> print(sorted(list(s)))
    ['bin', 'exe', 'pif', 'xml']
    >>> s = searchext_unique(['HelpPane.exe', 'hh.exe', 'HPMProp.INI', 'IE9_main.log'])
    >>> isinstance(s, set) # vrai si s est un set
    True
    >>> print(sorted(list(s)))
    ['exe', 'ini', 'log']
    >>> s = searchext_unique(['win.ini', 'WindowsShell', 'WindowsUpdate.log', 'winhelp.exe'])
    >>> isinstance(s, set) # vrai si s est un set
    True
    >>> print(sorted(list(s)))
    ['exe', 'ini', 'log']
    """
    s = set(searchext(l))
    return s


def main():
    # s = searchext_unique(['HelpPane.exe', 'hh.exe', 'HPMProp.INI', 'IE9_main.log'])
    # print(s)
    pass


if __name__ == "__main__":
    main()