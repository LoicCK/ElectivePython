DATA = [ '1', '0', 'H', '1', '0', 'H', '8', '6', '3', '2', '11', '8', '2',
            '7', '2', '1', '0', '0', '2.2', '3.2', '3.5', '2.25', '3.2', '3.4',
            '2.3', '3.1', '3.1', '2.2', '3', '3.3', '2.28', '3.17', '3.69', '2.3',
            '3.2', '3.2', '2.25', '3.2', '3.5', '41', '2.33', '2.25', '3.25', '3.14',
            '3.75', '3.41', '35', '2.5', '2.31', '1.67', '1.6', '20', '-0.25', '1.97',
            '1.91', '2.01', '1.96', '2.46', '3.23', '3.29' ]

def parse(value: str):
    """retourne la valeur typée de l'argument

    :param value: valeur à parser
    :type value: str
    :returns: selon le contenu de value
    :rtype: int, float or str

    >>> parse('1')
    1
    >>> parse('0')
    0
    >>> parse('-1')
    -1
    >>> parse('3.14')
    3.14
    >>> parse('0.0')
    0.0
    >>> parse('-0.0123456')
    -0.0123456
    >>> parse('ABC')
    'ABC'
    >>> parse('')
    ''
    >>> parse('3x2')
    '3x2'
    """
    parsed_value = value
    try:
        if '.' in value:
            parsed_value = float(value)
        else:
            parsed_value = int(value)
    except ValueError:
        pass
    except Exception:
        pass
    return parsed_value

def main():
    # votre code de test ici...
    # l = [ parse(value) for value in DATA]
    # print(l)
    pass

if __name__ == '__main__':
    main()