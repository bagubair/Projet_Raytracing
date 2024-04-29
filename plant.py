import numpy as np
from objet import Objet
from math import sqrt
from point import Point
from vecteur import Vecteur
from couleur import Couleur


class Plant(Objet):
    """Représente une sphère dans la scène."""
    def __init__(self, position, couleur, normal):
        super().__init__(position, couleur)
        self.normals = normal


    def intersection_point(self, rayon_vue):
        # Calcule le dénominateur de l'équation paramétrique du rayon, en calculant le produit scalair entre la deriction du rayon et la normal de plan
        d = rayon_vue.extremite.dot_product(self.normals)

        if (abs(d) < 1e-6):
            return None  # Pas d'intersection, le rayon est parallèle au plan

        #calcule un vecteur qui part de l'origine du rayon
        vect_vue = self.position - rayon_vue.origine

        t = (vect_vue.dot_product(self.normals))/ d

        if t < 0:
            return None  # Pas d'intersection 
 
        # Calcule le point d'intersection
        point_intersect = rayon_vue.origine + ( rayon_vue.extremite * t )

        return point_intersect

    def intersection_distance(self, rayon_vue):
        point = self.intersection_point(rayon_vue)

        
        # print(type(point))
        if point : 
        # print(type(rayon_vue.origine.pos))
            distance = np.linalg.norm((rayon_vue.origine.pos - point.pos))
            return float(distance)
        #distance = (rayon_vue.origine.pos - point.pos).magnitude()

        
    

#test 

if __name__ == "__main__":
    # Définir le rayon de vue
    ray = Vecteur(Point((0,0,5)), Point((0,5,-5)))
    
    # Définir le plan
    plan = Plant(Point((0,0,-10)), Couleur(1,1,1), Point((0,-1,1)))
    
    # Calculer l'intersection
    intersection = plan.intersection_point(ray)
    
    if intersection is not None:
        print("Le rayon intersecte le plan au point :", intersection.pos)
        dist = plan.intersection_distance(ray)
        print("Distance entre l'origine du rayon et le point d'intersection :", type(float(dist)))
    else:
        print("Le rayon est parallèle au plan ou ne traverse pas le plan.")