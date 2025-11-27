# vos import ici
from math import sqrt


class Point2D(object):
    """Point du plan cartésien

    >>> p1 = Point2D(3, 4)
    >>> p1.x
    3
    >>> p1.y
    4
    >>> print(p1)
    Point2D(3,4)
    >>> p2 = Point2D()
    >>> p2.x
    0
    >>> p2.y
    0
    >>> print(p2)
    Point2D(0,0)
    >>> p1.move(1,1)
    >>> p1.x
    4
    >>> p1.y
    5
    >>> print(p1)
    Point2D(4,5)
    >>> p1.distance(p2)
    6.4031242374328485
    """

    # attributs et méthodes ici...
    def __init__(self, x=0, y=0):
        """Constructeur

        :param x: Defaults to 0.
        :type x: int, optional
        :param y: Defaults to 0.
        :type y: int, optional
        """
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        """déplace le point

        :param dx: incrément de translation. Defaults to 0.
        :type dx: int, optional
        :param dy: incrément de translation. Defaults to 0.
        :type dy: int, optional
        """
        self.x = self.x + dx
        self.y = self.y + dy

    def __str__(self):
        """description string

        :returns: description
        :rtype: str
        """
        return f"({self.x},{self.y})"

    def distance(self, point: Point2D):
        """Distance entre 2 points

        :param point: point de référence
        :type point: Point2D
        :returns: distance au point de référence
        :rtype: float
        """
        return sqrt((self.x - point.x)**2 + (self.y - point.y)**2)


def main():
    a = Point2D(3,4)
    a.move(2,-2)
    b = Point2D(5,-4)
    print(a.distance(b))


if __name__ == "__main__":
    main()