import numpy as np

class Point:
    def __init__(self, pos):
        
        self.pos = np.array(pos)

    def __add__(self, other):
        """Addition de deux points."""
        return Point(np.add(self.pos, other.pos))
    
    def __sub__(self, other):
        """Soustraction de deux points."""
        return Point(np.subtract(self.pos, other.pos))
        
    def __mul__(self, scalar):
        """Multiplication d'un point par un scalaire."""
        return Point(np.multiply(self.pos, scalar))
        
    def dot_product(self, other):
        """Produit scalaire de deux points."""
        return np.dot(self.pos, other.pos)

    def cross_product(self, other):
        """Produit vectoriel de deux points."""
        return Point(np.cross(self.pos, other.pos))
   
    def magnitude(self):
        """Calcule la magnitude (ou norme) du point."""
        return np.linalg.norm(self.pos)
        
    def normalize(self):
        """
        Normalise le point.
        Retourne le point normalisé.
        """
        mag = self.magnitude()
        if mag == 0:
            return self  # Évite la division par zéro
        return Point(self.pos / mag)
