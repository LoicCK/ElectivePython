from typing import List, Any

def flatten_list(l: List[Any]) -> List[Any]:
    """
    Renvoie la liste aplatie de la liste l de profondeur n

    :param l: La liste
    :type l: List
    :return: La liste aplatie
    :rtype: List

    >>> flatten_list([1, 2, 3])
    [1, 2, 3]
    >>> flatten_list([1, [2, 3], 4])
    [1, 2, 3, 4]
    >>> flatten_list([[1, 2], [3, [4, 5]], 6])
    [1, 2, 3, 4, 5, 6]
    >>> flatten_list([1, 'a', [2, True], [], [3.5, [None]]])
    [1, 'a', 2, True, 3.5, None]
    >>> flatten_list([])
    []
    """
    if not l:
        return l
    first_elt = l[0]
    if isinstance(first_elt, list):
        return flatten_list(first_elt) + flatten_list(l[1:])
    return [first_elt] + flatten_list(l[1:])


def main():
    pass

if __name__ == '__main__':
    main()