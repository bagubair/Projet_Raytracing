import numpy as np
from point import Point

class Couleur(Point):
    """Classe représentant une couleur RGB.

    Hérite de la classe Point pour faciliter les opérations mathématiques
    telles que la multiplication...., car il n'y a pas de différence fondamentale
    entre les couleurs et les points dans cet contexte .

    """
    def __init__(self, r, g, b):
        super().__init__(r, g, b)

    @classmethod
    def from_hex(cls, hex_code):
        """Crée une couleur à partir du code hexadécimal."""
        hex_code = hex_code.lstrip("#")
        r = int(hex_code[0:2], 16) / 255.0
        g = int(hex_code[2:4], 16) / 255.0
        b = int(hex_code[4:6], 16) / 255.0
        return cls(r, g, b)
