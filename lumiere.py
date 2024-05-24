from couleur import Couleur
from point import Point
from math import sqrt

class Lumiere:
    """Light represents a point light source of a certain color"""

    def __init__(self, position, couleur=Couleur(1,1,1)):
        self.position = position
        self.couleur = couleur

    
        