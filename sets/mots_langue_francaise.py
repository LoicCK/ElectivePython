#### Imports et définition des variables globales

import random
from typing import List, Set

FILENAME = "corpus.txt"
ALPHABET = list("abcdefghijklmnopqrstuvwxyz")
VOYELLES = list("aeiouy")
CONSONNES = list("bcdfghjklmnpqrstvwxz")


#### Fonctions secondaires

def read_data(filename: str) -> List[str]:
    """Lit le fichier passé en paramètre et retourne une liste de mots.

    :param filename: nom du fichier
    :type filename: str
    :returns: la liste des mots
    :rtype: List[str]

    >>> mots = read_data(FILENAME)
    >>> isinstance(mots, list)
    True
    >>> len(mots)
    336531
    >>> mots[1]
    'à'
    >>> mots[328570]
    'vaincre'
    >>> mots[290761]
    'sans'
    >>> mots[233574]
    'péril'
    >>> mots[221712]
    'on'
    >>> mots[324539]
    'triomphe'
    >>> mots[290761]
    'sans'
    >>> mots[166128]
    'gloire'
    """

    lignes = []
    with open(FILENAME, encoding='utf-8') as f:
        lignes = f.readlines()
    cleand_lignes = [ligne.removesuffix("\n") for ligne in lignes]
    return cleand_lignes


def ensemble_mots(filename: str) -> Set[str]:
    """retourne les mots contenus dans filename

    :param filename: nom du fichier
    :type filename: str
    :returns: le set des mots
    :rtype: Set[str]

    >>> mots = ensemble_mots(FILENAME)
    >>> isinstance(mots, set)
    True
    >>> len(mots)
    336531
    >>> "glomérules" in mots
    True
    >>> "glycosudrique" in mots
    False
    """

    return set(read_data(filename))


def mots_de_n_lettres(mots: Set[str], n: int) -> Set[str]:
    """retourne le sous ensemble des mots de n lettres

    :param mots: ensemble de mots
    :type mots: set
    :param n: nombre de lettres
    :type n: int
    :returns: sous ensemble des mots de n lettres
    :rtype: set

    >>> mots = ensemble_mots(FILENAME)
    >>> m15 = mots_de_n_lettres(mots, 15)
    >>> isinstance(m15, set)
    True
    >>> len(m15)
    8730
    >>> list({ len(mots_de_n_lettres(mots,i)) for i in range(15,26)})
    [4418, 2, 4, 2120, 42, 11, 205, 977, 437, 8730, 94]
    >>> sorted(list(mots_de_n_lettres(mots,23)))[0]
    'constitutionnalisassent'
    >>> sorted(list(mots_de_n_lettres(mots,24)))
    ['constitutionnalisassions', 'constitutionnaliseraient', 'hospitalo-universitaires', 'oto-rhino-laryngologiste']
    >>> sorted(list(mots_de_n_lettres(mots,25)))
    ['anticonstitutionnellement', 'oto-rhino-laryngologistes']
    """
    return {mot for mot in mots if (len(mot) == n)}


def mots_avec(mots: Set[str], s: str) -> Set[str]:
    """retourne le sous ensemble des mots incluant la lettre l

    :param mots: ensemble de mots
    :type mots: set
    :param s: chaine de caractères à inclure
    :type s: str
    :returns: sous ensemble des mots incluant la chaine de caractères s
    :rtype: set

    >>> mots = ensemble_mots(FILENAME)
    >>> mk = mots_avec(mots, 'k')
    >>> isinstance(mk, set)
    True
    >>> len(mk)
    1621
    >>> sorted(list(mk))[35:74:7]
    ['ankyloseraient', 'ankyloserons', 'ankylostome', 'ankylosée', 'ashkénaze', 'bachi-bouzouks']
    >>> sorted(list(mk))[147:359:38]
    ['black', 'blackboulèrent', 'cheikhs', 'cokéfierais', 'dock', 'dénickeliez']
    >>> sorted(list(mk))[999::122]
    ['képi', 'nickela', 'parkérisiez', 'semi-coke', 'stockais', 'week-end']
    """
    return {mot for mot in mots if s in mot}


def cherche1(mots: Set[str], start: str, stop: str, n: int) -> Set[str]:
    """retourne le sous ensemble des mots de n lettres commençant par start et finissant par stop

    :param mots: ensemble de mots
    :type mots: set
    :param start: première lettre
    :type start: str
    :param stop: dernière lettre
    :type stop: str
    :param n: nombre de lettres
    :type n: int
    :returns: sous ensemble des mots de n lettres commençant par start et finissant par stop
    :rtype: set

    >>> mots = ensemble_mots(FILENAME)
    >>> m_z = cherche1(mots, 'z', 'z', 7)
    >>> isinstance(m_z, set)
    True
    >>> len(m_z)
    10
    >>> sorted(list(m_z))[4:7]
    ['zinguez', 'zippiez', 'zonerez']
    """
    return {mot for mot in mots if len(mot) == n and mot.startswith(start) and mot.endswith(stop)}


def cherche2(mots: Set[str], lstart: List[str], lmid: List[str], lstop: List[str], nmin: int, nmax: int) -> Set[str]:
    """effectue une recherche complexe dans un ensemble de mots

    :param mots: ensemble de mots
    :type mots: set
    :param lstart: liste des préfixes
    :type lstart: list
    :param lmid: liste des chaines de caractères intermédiaires
    :type lmid: list
    :param lstop: liste des suffixes
    :type lstop: list
    :param nmin: nombre de lettres minimum
    :type nmin: int
    :param nmax: nombre de lettres maximum
    :type nmax: int
    :returns: retourne le sous ensemble des mots commençant par une chaine présente dans lstart, contenant une chaine présente dans lmid et finissant par une chaine présente dans lstop, avec un nombre de lettres entre nmin et nmax
    :rtype: set

    >>> mots = ensemble_mots(FILENAME)
    >>> mab17ez = cherche2(mots, 'a', 'b', 'z', 16, 16)
    >>> isinstance(mab17ez, set)
    True
    >>> len(mab17ez)
    1
    >>> mab17ez
    {'alphabétisassiez'}
    """
    tstart = tuple(lstart)
    tstop = tuple(lstop)


    return {mot
            for mot in mots
            if nmin <= len(mot) <= nmax
            and mot.startswith(tstart)
            and mot.endswith(tstop)
            for mid in (mot[1:-1],)
            if all(s in mid for s in lmid)}


def main():
    pass
    mots = read_data(FILENAME)
    ens = ensemble_mots(FILENAME)
    print( [ mot for mot in ["chronophage", "procrastinateur", "dangerosité", "gratifiant"] if mot in ens ] )
    m17 = mots_de_n_lettres(ens, 17)
    print(len(m17))
    print( random.sample(list(m17), 10) )
    mk = mots_avec(ens, 'k')
    print(len(mk))
    print( random.sample(list(mk), 5) )
    moo = mots_avec(ens, 'oo')
    print(len(moo))
    print( random.sample(list(moo), 5) )
    mz14 = cherche1(ens, 'z', '', 14)
    print(mz14)
    m21z = cherche1(ens, '', 'z', 18)
    print(m21z)
    m_z = cherche1(mots, 'z', 'z', 7)
    print(m_z)
    mab17ez = mots_avec(cherche1(ens, 'sur', 'ons', 17), 'x')
    print(mab17ez)
    mab17ez = cherche2(mots, 'a', 'b', 'z', 16, 16)
    print(mab17ez)


if __name__ == "__main__":
    main()