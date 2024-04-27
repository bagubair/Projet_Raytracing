from objet import Objet
from math import sqrt
from position import Position

def intersection_sphere_rayon(Sx, Sy, Sz, R, Fx, Fy, Fz, Px, Py, Pz):
    """Calcul de l'intersection entre un rayon et une sphère."""
    Dx = Px - Fx  # Vecteur directeur du rayon
    Dy = Py - Fy
    Dz = Pz - Fz

    S_Fx = Sx - Fx  # Vecteur entre le centre de la sphère et le point de départ du rayon
    S_Fy = Sy - Fy
    S_Fz = Sz - Fz

    d = sqrt(S_Fx**2 + S_Fy**2 + S_Fz**2)  # Distance entre le point de départ du rayon et le centre de la sphère

    discriminant = (S_Fx * Dx + S_Fy * Dy + S_Fz * Dz)**2 - (Dx**2 + Dy**2 + Dz**2) * (d**2 - R**2)

    if discriminant < 0:
        return None, None

    t1 = (- (S_Fx * Dx + S_Fy * Dy + S_Fz * Dz) + sqrt(discriminant)) / (Dx**2 + Dy**2 + Dz**2)
    t2 = (- (S_Fx * Dx + S_Fy * Dy + S_Fz * Dz) - sqrt(discriminant)) / (Dx**2 + Dy**2 + Dz**2)

    x1 = Fx + t1 * Dx  # Coordonnées des points d'intersection
    y1 = Fy + t1 * Dy
    z1 = Fz + t1 * Dz

    x2 = Fx + t2 * Dx
    y2 = Fy + t2 * Dy
    z2 = Fz + t2 * Dz

    distance1 = sqrt((x1 - Fx)**2 + (y1 - Fy)**2 + (z1 - Fz)**2)  # Distance entre le point de départ du rayon et le point d'intersection
    distance2 = sqrt((x2 - Fx)**2 + (y2 - Fy)**2 + (z2 - Fz)**2)

    return min(distance1, distance2), Position((x1, y1, z1))

class Sphere(Objet):
    """Représente une sphère dans la scène."""
    def __init__(self, position, couleur, rayon):
        super().__init__(position, couleur)
        self.rayon = rayon

    def intersection_distance(self, rayon_vue):
        """Calcule la distance entre le point de départ du rayon et le point d'intersection avec la sphère."""
        Px, Py, Pz = rayon_vue.extremite.pos
        Fx, Fy, Fz = rayon_vue.origine.pos
        Sx, Sy, Sz = self.position.pos
        R = self.rayon

        return intersection_sphere_rayon(Sx, Sy, Sz, R, Fx, Fy, Fz, Px, Py, Pz)[0]
        
    def intersection_point(self, rayon_vue):
        """Calcule le point d'intersection entre le rayon donné et la sphère."""
        Px, Py, Pz = rayon_vue.extremite.pos
        Fx, Fy, Fz = rayon_vue.origine.pos
        Sx, Sy, Sz = self.position.pos
        R = self.rayon

        return intersection_sphere_rayon(Sx, Sy, Sz, R, Fx, Fy, Fz, Px, Py, Pz)[1]

    def normal(self, surface_point):
        """Calcule la normale à la surface de la sphère au point donné."""
        return (surface_point -self.position   ).normalize()
