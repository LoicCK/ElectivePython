from collections import namedtuple
from csv import DictReader
from typing import Dict, NamedTuple

FILENAME = 'meteo-france-stations.csv'


def build_stations_dict(csvfile: str) -> Dict[NamedTuple]:
    """
    retourne un dictionnaire des stations météo du fichier passé en argument

    :param csvfile: un fichier au format csv contenant une liste de stations météo
    :type csvfile: str
    :returns: dictionnaire de namedtuple des informations relatives aux stations météo
    :rtype: dict

    >>> d = build_stations_dict(FILENAME)
    >>> print(d['NICE'])
    Station(ID='07690', Latitude=43.648833, Longitude=7.209, Altitude=2)
    >>> print(d['BELLE ILE-LE TALUT'])
    Station(ID='07207', Latitude=47.294333, Longitude=-3.218333, Altitude=34)
    >>> print(d['CAYENNE-MATOURY'])
    Station(ID='81405', Latitude=4.822333, Longitude=-52.365333, Altitude=4)
    >>> print(d['NICE'].Latitude)
    43.648833
    """
    Station = namedtuple('Station',['ID','Latitude','Longitude','Altitude'])
    with open(csvfile, mode='r', encoding='utf8') as f:
        l = [row for row in DictReader(f, delimiter=';')]
    d = dict()
    for station in l:
        d[station["Nom"]] = Station(station['ID'],
                                    float(station['Latitude']),
                                    float(station['Longitude']),
                                    int(station['Altitude']))
    return d


def main():
    d = build_stations_dict(FILENAME)
    print(d['NICE'])


if __name__ == '__main__':
    main()