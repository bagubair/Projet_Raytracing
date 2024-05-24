import numpy as np
from objet import Objet
from math import sqrt
from point import Point
from vecteur import Vecteur
from couleur import Couleur


class Plan(Objet):
    
    def __init__(self, position, couleur, normal, texture_path =None, diffuse=0, specular=0, reflexion=0, ombre=0,ambiant =.5,translucide=0):
        super().__init__(position, couleur, texture_path,diffuse, specular, reflexion, ombre,ambiant,translucide )

        self.normals = normal
    
    def normal(self, surface_point):
        """envoyer le normals de plan"""
        
        return self.normals

    def intersection(self, rayon_vue):
        # Calcule le dénominateur 
        d = rayon_vue.extremite.dot_product(self.normals)

        if abs(d) < 1e-6:
            return None, None  

        # Calcule un vecteur qui part de l'origine du rayon
        vect_vue = self.position - rayon_vue.origine

        t = vect_vue.dot_product(self.normals) / d

        if t < 0:
            return None, None  # Pas d'intersection

        
        point_intersect = rayon_vue.origine + (rayon_vue.extremite * t)
        
       
        distance = (rayon_vue.origine - point_intersect).magnitude()

        return distance, point_intersect
    
    def couleur_texture(self, M):
        """Retourne la couleur de texture pour les coordonnées M."""
        if self.texture:
            
            u, v = M.x, M.z
            # Convertir les coordonnées UV en pixels de l'image de texture
            tex_x = int(u * self.texture.width)%self.texture.width
            tex_y = int(v * self.texture.height)% self.texture.height
            couleur_tex = self.texture.getpixel((tex_x, tex_y))
            
            # Normaliser  dans la plage [0, 1]
            couleur_tex_normalisee = (int(couleur_tex[0]) / 255, int(couleur_tex[1]) / 255, int(couleur_tex[2]) / 255)

            return Couleur(*couleur_tex_normalisee)
        else:
            return self.couleur  


# Test Comme dans le cours
if __name__ == "__main__":
    
    ray = Vecteur(Point(0, 0, 5), Point(0, 5, -5))

    plan = Plan(Point(0, 0, -10), Couleur(1, 1, 1), Point(0, -1, 1))

    distance, intersection = plan.intersection(ray)

    if intersection is not None:
        # Les valeurs attendues pour l'intersection et la distance comme dans le cours
        intersection_attendue = (0.0, 7.5, -2.5)
        distance_attendue = 10.606601717798213
        
        # Vérification des résultats
        assert np.allclose(intersection.components(), intersection_attendue), "ne correspond pas à la valeur attendue."
        assert np.isclose(distance, distance_attendue), " valeur attendue."
        
        print("Le rayon intersecte le plan au point :", intersection_attendue)
        print("Distance entre l'origine du rayon et le point d'intersection :", distance_attendue)
    else:
        print("Le rayon est parallèle au plan ou ne traverse pas le plan.")
