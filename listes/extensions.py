from typing import List

def searchext(l: List[str]) -> List[str]:
    """
    Identifie les extensions de la liste de fichiers passée en argument

    :param l: liste des noms de fichier sous forme de chaine de caractères
    :type l: list
    :returns: Liste des extensions sous forme de chaine de caractères
    :rtype: list

    >>> l = searchext(['ARJ.PIF', 'atiogl.xml', 'ativpsrm.bin', 'bfsvc.exe'])
    >>> isinstance(l, list) # vrai si l est une liste
    True
    >>> print(l)
    ['pif', 'xml', 'bin', 'exe']

    >>> l = searchext(['HelpPane.exe', 'hh.exe', 'HPMProp.INI', 'IE9_main.log'])
    >>> isinstance(l, list) # vrai si l est une liste
    True
    >>> print(l)
    ['exe', 'exe', 'ini', 'log']

    >>> l = searchext(['win.ini', 'WindowsShell', 'WindowsUpdate.log', 'winhelp.exe'])
    >>> isinstance(l, list) # vrai si l est une liste
    True
    >>> print(l)
    ['ini', 'log', 'exe']

    >>> l = searchext(['Gfxv2_0.exe.config', 'pstask.dll', 'GfxValDisplayLog.bin'])
    >>> isinstance(l, list) # vrai si l est une liste
    True
    >>> print(l)
    ['config', 'dll', 'bin']
    """

    # une list comprehension e des extensions sous forme de chaine de caractères
    e = [fichier.split(".")[-1].lower() for fichier in l if '.' in fichier]

    return e