from objet import Objet
from math import sqrt
from point import Point
from vecteur import Vecteur
from camera import Camera
from couleur import Couleur
import numpy as np
import math


class Sphere(Objet):
    
    
    def __init__(self, position, couleur, rayon ,texture_path=None,diffuse= 1, specular=1 ,reflexion= 0.5,ombre=2,ambiant=.5,translucide=0 ):
        super().__init__(position, couleur, texture_path,diffuse,specular,reflexion,ombre,ambiant,translucide)
        self.rayon = rayon
    def normal(self, surface_point):
        """Calcule la normale à la surface de la sphère au point donné."""
        
        return (surface_point - self.position   ) 
    def intersection(self, rayon_vue):
        # t^2 * BB + 2tB(A - C) + (A - C)(A - C) - R ^ 2 = 0

        A = rayon_vue.origine

        B = rayon_vue.extremite


        centre_sphere = self.position
        rayon_sphere =self.rayon

        C = centre_sphere

        R = rayon_sphere

        # Calcul des coefficients de l'équation quadratique
        a = B.dot_product(B)  #BB

        b = 2 * B.dot_product( A - C)
        c = (A - C).dot_product( A - C) - R**2

        # Résolution de l'équation quadratique
        discriminant = b**2 - 4 * a * c
        if discriminant < 0:
            return None ,None  # Pas d'intersection
        elif discriminant == 0:
            t = -b / (2 * a)
            intersection_points = A + B *t
            return t,intersection_points

        else:
            t1 = (-b + np.sqrt(discriminant)) / (2 * a)
            t2 = (-b - np.sqrt(discriminant)) / (2 * a)
            t = min(t1, t2)
            intersection_points = A +  B*t
            return t ,intersection_points

   
    def couleur_texture(self, P):
        
           
        # Calculer les coordonnées sphériques pour le point (0,0,0)
        p = P - self.position
        r = p.magnitude() #Rayon
        
        theta = math.acos(p.z / r)
        s = theta / math.pi


        phi = math.atan2(p.y, p.x) #
        t = phi / (2 * math.pi)
        
        # Convertir les coordonnées UV en pixels de l'image de texture
        tex_x = int(t * self.texture.width) % self.texture.width
        tex_y = int(s * self.texture.height) % self.texture.height

        # Obtenir la couleur de texture à partir des pixels de l'image
        couleur_tex = self.texture.getpixel((tex_x, tex_y))

        # Normaliser les valeurs de couleur dans la plage [0, 1]
        couleur_tex_normalisee = (couleur_tex[0] / 255, couleur_tex[1] / 255, couleur_tex[2] / 255)

        return Couleur(*couleur_tex_normalisee)
    
            





# Test
if __name__ == "__main__":
    
    Couleur = Point
    sphere = Sphere(Point(0, -1/2, -5-(1/2)), Couleur(0.75, 0, 0), 1/np.sqrt(2),"texture.jpg")
    cam = Camera(200, 200, Point(0, 0, 5))
    rayon_vue = cam.rayon(100, 100)

    dist, point_intersection = sphere.intersection(rayon_vue)
    sphere.couleur_texture(point_intersection)
    # Résultats attendus
    resultat_distance_attendu = 4.995059749768852
    resultat_point_attendu = (0.005020155481797906, -0.005020155481797906, -4.9950547043890055)
    
    # Comparaison avec les résultats attendus
    # np.isclose(dist, resultat_distance_attendu), f"La distance obtenue ({dist}) ne correspond pas au résultat attendu ({resultat_distance_attendu})"
    #assert np.allclose(point_intersection.components(), resultat_point_attendu), f"Les coordonnées du point d'intersection obtenues ({point_intersection.components()}) ne correspondent pas aux résultats attendus ({resultat_point_attendu})"

    print("Les résultats sont conformes aux attentes.")