import numpy as np
from point import Point

class Vecteur:
    def __init__(self, origine:Point, extremite:Point):
        self.origine = origine 
        self.extremite = extremite   
        
    def __add__(self, other):
        """
        Addition de deux vecteurs.
        """
        return Vecteur((self.origine + other.origine), (self.extremite + other.extremite))
    
    def __sub__(self, other):
        """
        Soustraction de deux vecteurs.
        """
        return Vecteur( (self.origine - other.origine), (self.extremite - other.extremite))
    
    def __mul__(self, scalar):
        
        """
        Multiplication d'un vecteur par un scalaire.
        """
        assert not isinstance(scalar, Vecteur)
        return Vecteur(np.multiply(self.origine, scalar), np.multiply(self.extremite, scalar))

    def dot_product(self, other):
        """
        Produit scalaire de deux vecteurs.

        Le produit scalaire de deux vecteurs v1=[x1,y1]v1​=[x1​,y1​] 
        et v2=[x2,y2]v2=[x2,y2] en deux dimensions est calculé comme suit :
        v1⋅v2=x1×x2+y1×y2v1​⋅v2​=x1​×x2​+y1​*y2
        """
        return np.dot(self.origine, other.origine) + np.dot(self.extremite, other.extremite)
    
    def cross_product(self, other):
        """
        Produit Vecteuriel de deux vecteurs.
        """
        return Vecteur(np.cross(self.origine, other.origine), np.cross(self.extremite, other.extremite))
    
   
    def magnitude(self):
        """
        Calcul de la magnitude (ou norme) du vecteur.
        """
        return np.linalg.norm(self.origine) + np.linalg.norm(self.extremite)
    def normalize(self):
        """
    Normalise le vecteur.
    :return: Le vecteur normalisé.
        """
        magnitude = self.magnitude()
        return Vecteur(np.divide(self.origine, magnitude), np.divide(self.extremite, magnitude))
