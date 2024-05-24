import numpy as np

class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __mul__(self, other):
        return Point(self.x * other, self.y * other, self.z * other)
    def __truediv__(self, other):
        return Point(self.x / other, self.y / other, self.z / other)
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def dot_product(self, other):
        """Produit scalaire de deux points."""
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def cross_product(self, other):
       
        return Point(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
    )
    def magnitude(self):
        """Calcule la magnitude (ou norme) du point."""
        return np.sqrt(self.dot_product(self))
        
    def normalize(self):
        
        mag = self.magnitude()
        return self * (1.0 / np.where(mag == 0, 1, mag))
    
    def components(self):
        return (self.x, self.y, self.z)
    def distance(self, other):
        """
        Calcule la distance entre deux points.
        Retourne la distance entre self et other.
        """
        diff = self - other
        return diff.magnitude()






# Test
if __name__ == "__main__":
    # Création de quelques points pour les tests
    point1 = Point(0, .5, .5)
    point2 = Point(4, 5, 6)

    # Test des opérations de base
    resultat_mul = point1 * 2
    resultat_add = point1 + point2
    resultat_sub = point2 - point1

    print("Résultat de la multiplication :", resultat_mul.components())  # Devrait imprimer (2, 4, 6)
    print("Résultat de l'addition :", resultat_add.components())          # Devrait imprimer (5, 7, 9)
    print("Résultat de la soustraction :", resultat_sub.components())    # Devrait imprimer (3, 3, 3)

    # Test du produit scalaire
    produit_scalaire = point1.dot_product(point2)
    print("Produit scalaire :", produit_scalaire)  # Devrait imprimer 32

    # Test du produit vectoriel
    produit_vectoriel = point1.cross_product(point2)
    print("Produit vectoriel :", produit_vectoriel.components())  # Devrait imprimer (-3, 6, -3)

    # Test de la magnitude et de la normalisation
    magnitude = point1.magnitude()
    point_normalise = point1.normalize()

    print("Magnitude de point1 :", magnitude)               # Devrait imprimer environ 3.74
    print("Point1 normalisé :", point_normalise.components())  # Devrait imprimer environ (0.27, 0.53, 0.80)
