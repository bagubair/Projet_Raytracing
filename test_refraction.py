def calcul_refraction(self, V, N, n1, n2, point_intersection, depth):
    # Calcul de la direction du rayon réfracté
    refract_dir = self.refract(V, N, n1, n2)
    
    # Point d'origine du rayon réfracté légèrement décalé pour éviter les erreurs de précision
    refract_orig = point_intersection - N * 0.001 if refract_dir.dot_product(N) > 0 else point_intersection + N * 0.001
    
    # Calcul de la couleur réfractée en lançant un rayon depuis le point d'origine réfracté
    refract_color = self.lancer_rayon(refract_orig, refract_dir, depth + 1) * obj_int.transparence
    
    return refract_color
from point import Point
from math import sqrt
def refract( V, N, n1, n2):
    # Calcul de l'indice de réfraction relatif
    n = n1 / n2
    
    # Calcul de l'angle d'incidence
    cosI = (N*-1).dot_product(V)
    
    # Calcul de la sinus carrée de l'angle de transmission
    sinT2 = n ** 2 * (1.0 - cosI ** 2)
    
    # Vérification de la réflexion totale interne
    if sinT2 > 1.0:
        return None  # Réflexion totale interne

    # Calcul de l'angle de transmission
    cosT = (1.0 - sinT2) ** 0.5
    
    # Calcul de la direction du rayon réfracté
    refract_dir = V * n + N * (n * cosI - cosT)
    
    return refract_dir

#example 

V = Point(0,0,-1) 
N = Point(0,1/sqrt(2),1/sqrt(2))
ref =refract( V, N, 1, 1.52)
print(ref.components())