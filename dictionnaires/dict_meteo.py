# vos imports ici
from csv import DictReader
from typing import List, Dict, Any

FILENAME = "meteo-france-synop.2015110112.csv"


def read_data_to_dicts(filename: str) -> List[Dict[str | Any, Any | str]]:
    """puts structured csv data in a list of dicts

    :param filename: csv data filename
    :type filename: str
    :returns: csv data in dicts
    :rtype: list

    >>> data = read_data_to_dicts(FILENAME)
    >>> isinstance(data, list)
    True
    >>> isinstance(data[0], dict)
    True
    >>> len(data)
    51
    >>> data[11]['numer_sta']
    '07168'
    >>> data[11]['date']
    '20151101120000'
    >>> data[11]['pmer']
    '102940'
    >>> data[11]['t']
    '290.050000'
    >>> data[11]['td']
    '283.850000'
    >>> data[11]['tminsol']
    '275.850000'
    >>> data[21]['numer_sta']
    '07335'
    >>> data[21]['date']
    '20151101120000'
    >>> data[21]['pmer']
    '102720'
    >>> data[21]['t']
    '293.450000'
    >>> data[21]['td']
    '279.050000'
    >>> data[21]['tminsol']
    '273.950000'
    >>> data[31]['numer_sta']
    '07607'
    >>> data[31]['date']
    '20151101120000'
    >>> data[31]['pmer']
    '102400'
    >>> data[31]['t']
    '292.950000'
    >>> data[31]['td']
    '284.950000'
    >>> data[31]['tminsol']
    'mq'
    >>> data[41]['numer_sta']
    '07790'
    >>> data[41]['date']
    '20151101120000'
    >>> data[41]['pmer']
    '102830'
    >>> data[41]['t']
    '291.850000'
    >>> data[41]['td']
    '282.850000'
    >>> data[41]['tminsol']
    '284.750000'
    """
    l = []
    with open(filename, mode='r', encoding='utf8') as f:
        l = [row for row in DictReader(f, delimiter=';')]
    return l


def filter_data(d):
    """Filter full data dict

    :param d: full meteo data
    :type d: dict
    :returns: filtered meteo data (numer_sta, date, t)
    :rtype: dict

    >>> d = {'numer_sta': '07005', 'date': '20151101120000', 'pmer': '102910', 'tend': '-80', 'cod_tend': '8', \
        'dd': '150', 'ff': '2.600000', 't': '287.750000', 'td': '283.950000', 'u': '78', 'vv': '8000', \
        'ww': '0', 'w1': '0', 'w2': '0', 'n': '0', 'nbas': '0', 'hbas': 'mq', 'cl': '30', 'cm': '20', \
        'ch': '10', 'pres': '102040', 'niv_bar': 'mq', 'geop': 'mq', 'tend24': '590', 'tn12': 'mq', \
        'tn24': 'mq', 'tx12': 'mq', 'tx24': 'mq', 'tminsol': '278.950000', 'sw': 'mq', 'tw': 'mq', \
        'raf10': '3.500000', 'rafper': '4.600000', 'per': '-10', 'etat_sol': '0', 'ht_neige': '0.000000', \
        'ssfrai': '0.000000', 'perssfrai': 'mq', 'rr1': '0.000000', 'rr3': '0.000000', 'rr6': '0.200000', \
        'rr12': '0.400000', 'rr24': '0.400000', 'phenspe1': 'mq', 'phenspe2': 'mq', 'phenspe3': 'mq', \
        'phenspe4': 'mq', 'nnuage1': 'mq', 'ctype1': 'mq', 'hnuage1': 'mq', 'nnuage2': 'mq', 'ctype2': 'mq', \
        'hnuage2': 'mq', 'nnuage3': 'mq', 'ctype3': 'mq', 'hnuage3': 'mq', 'nnuage4': 'mq', 'ctype4': 'mq', 'hnuage4': 'mq', '': ''}

    >>> fd = filter_data(d)
    >>> isinstance(fd, dict)
    True
    >>> len(fd)
    3
    >>> fd['numer_sta']
    '07005'
    >>> fd['date']
    '20151101120000'
    >>> fd['t']
    '287.750000'
    >>> fd.get('ww')

    """
    fd = dict([(k,v) for k,v in d.items() if k in ["numer_sta", "date", "t"]])
    return fd


def main():
    # data = read_data_to_dicts(FILENAME)
    # print(data)
    # print(filter_data(d[9]))
    pass


if __name__ == "__main__":
    main()