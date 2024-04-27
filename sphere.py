from objet import Objet
from math import sqrt

class Sphere(Objet):
    def __init__(self, position, couleur, rayon):
        super().__init__(position, couleur)  # Appel du constructeur de la classe parente
        self.rayon = rayon


    def intersection(self, rayon_vue):
        """returner la distance entre le sphere et l'origin de la rayon_vue intersecté s'elle existe""" 

        sphere_droit = rayon_vue.origine - self.position

        a = 1
        b = 2 * rayon_vue.extremite.dot_product(sphere_droit)
        c = sphere_droit.dot_product(sphere_droit) - (self.rayon * self.rayon)

        delta = (b**2) - 4*a*c

        if delta >= 0:
            dist = (-b - sqrt(delta)) / 2
            if(dist > 0):
                return dist
            else:
                return None
        