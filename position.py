import numpy as np

class Position:
    def __init__(self, pos):
        """la pos entre comme un triple(x,y,z)"""
        self.pos = np.array(pos)

    def __add__(self, other):
        """
        Addition de deux Positions.
        """
        return Position(np.add(self.pos, other.pos))
    
    def __sub__(self, other):
        """
        Soustraction de deux Positions.
        """
        return Position(np.subtract(self.pos, other.pos))
        
    def __mul__(self, scalar):
        """
        Multiplication d'un Position par un scalaire.
        """
        return Position(np.multiply(self.pos, scalar))
        
    def dot_product(self, other):
        """
        Produit scalaire de deux Positions.
        """
        return np.dot(self.pos, other.pos)

    def cross_product(self, other):
        """
        Produit vectoriel de deux Positions.
        """
        return Position(np.cross(self.pos, other.pos))
   
    def magnitude(self):
        """
        Calcul de la magnitude (ou norme) du Position.
        """
        return np.linalg.norm(self.pos)
        
    def normalize(self):
        """
        Normalise le Position.
        :return: Le Position normalisé.
        """
        mag = self.magnitude()
        if mag == 0:
            return self  # Évite la division par zéro
        return Position(self.pos / mag)
