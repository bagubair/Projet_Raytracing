import numpy as np
from point import Point

class Vecteur:
    def __init__(self, origine:Point, extremite:Point):
        self.origine = origine 
        self.extremite = extremite   
        
    def __add__(self, other):
        
        return Vecteur((self.origine + other.origine), (self.extremite + other.extremite))
    
    def __sub__(self, other):
       
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
        
        """
        return np.dot(self.origine, other.origine) + np.dot(self.extremite, other.extremite)
    
    def cross_product(self, other):
        """
        Produit Vecteuriel de deux vecteurs.
        """
        return Vecteur(np.cross(self.origine, other.origine), np.cross(self.extremite, other.extremite))
    
   
    def magnitude(self):
        
        return np.linalg.norm(self.origine) + np.linalg.norm(self.extremite)
    def normalize(self):
  
        magnitude = self.magnitude()
        return Vecteur(np.divide(self.origine, magnitude), np.divide(self.extremite, magnitude))
