# vos imports ici
from math import sqrt

from classes.point2d import Point2D


class Vector2D(object):
    """
    Vecteur dans un plan

    >>> O = Point2D()
    >>> A = Point2D(1, 0)
    >>> B = Point2D(1, 1)
    >>> C = Point2D(0, 1)
    >>> v1 = Vector2D(O,A)
    >>> v2 = Vector2D(O,B)
    >>> v3 = Vector2D(O,C)
    >>> print(v1)
    Vector2D(1,0)
    >>> print(v2)
    Vector2D(1,1)
    >>> print(v3)
    Vector2D(0,1)
    >>> print(abs(v1))
    1.0
    >>> print(abs(v2))
    1.4142135623730951
    >>> print(-v1)
    Vector2D(-1,0)
    >>> print(v1+v2)
    Vector2D(2,1)
    >>> print(v1+v3)
    Vector2D(1,1)
    >>> print(v1-v3)
    Vector2D(1,-1)
    >>> print(v1+v3 == v2)
    True
    """

    # attributs et méthodes ici...
    def __init__(self, origin: Point2D, dest: Point2D):
        """Constructeur

        :param origin: Point de départ
        :type origin: Point2D
        :param dest: Point d'arrivée
        :type dest: Point2D
        """
        self.x = origin.x-dest.x
        self.y = origin.y-dest.y

    def __abs__(self):
        """Retourne la norme du vecteur

        :returns: Norme du vecteur
        :rtype: float
        """
        return sqrt(self.x**2 + self.y**2)

    def __str__(self):
        """Représentation textuelle du vecteur

        :returns: Chaîne de caractères 'Vector2D(x,y)'
        :rtype: str
        """
        return f"Vector2D({self.x},{self.y})"

    def __eq__(self, other: Vector2D):
        """Test d'égalité entre deux vecteurs

        :param other: Vecteur à comparer
        :type other: Vector2D
        :returns: True si les vecteurs sont égaux, False sinon
        :rtype: bool
        """
        return self.x == other.x and self.y == other.y

    def __neg__(self):
        """Retourne l'opposé du vecteur

        :returns: Nouveau vecteur opposé
        :rtype: Vector2D
        """
        return Vector2D(Point2D(-self.x), Point2D(y=-self.y))

    def __add__(self, other: Vector2D):
        """Somme de deux vecteurs

        :param other: Vecteur à ajouter
        :type other: Vector2D
        :returns: Nouveau vecteur somme
        :rtype: Vector2D
        """
        return Vector2D(Point2D(self.x + other.x), Point2D(y=self.y + other.y))

    def __sub__(self, other: Vector2D):
        """Différence de deux vecteurs

        :param other: Vecteur à soustraire
        :type other: Vector2D
        :returns: Nouveau vecteur différence
        :rtype: Vector2D
        """
        return self + (-other)


def main():
    O = Point2D()
    A = Point2D(1, 0)
    B = Point2D(1, 1)
    v1 = Vector2D(O,A)
    v2 = Vector2D(O,B)
    print(v1)
    print(v2)
    print(abs(v1))
    print(abs(v2))
    print(-v1)
    print(v1+v2)


if __name__ == "__main__":
    main()