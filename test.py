from math import sqrt

def intersection_sphere_rayon(Sx, Sy, Sz, R, Fx, Fy, Fz, Px, Py, Pz):
    # Vecteur directeur du rayon
    Dx = Px - Fx
    Dy = Py - Fy
    Dz = Pz - Fz

    # Vecteur entre le centre de la sphère et le point de départ du rayon
    S_Fx = Sx - Fx
    S_Fy = Sy - Fy
    S_Fz = Sz - Fz

    # Calcul de la distance entre le point de départ du rayon et le centre de la sphère
    d = sqrt(S_Fx**2 + S_Fy**2 + S_Fz**2)

    # Calcul du discriminant de l'équation quadratique
    discriminant = (S_Fx * Dx + S_Fy * Dy + S_Fz * Dz)**2 - (Dx**2 + Dy**2 + Dz**2) * (d**2 - R**2)

    # Vérifier s'il y a une intersection entre le rayon et la sphère
    if discriminant >= 0:
        # Calcul des solutions de l'équation quadratique
        t1 = (- (S_Fx * Dx + S_Fy * Dy + S_Fz * Dz) + sqrt(discriminant)) / (Dx**2 + Dy**2 + Dz**2)
        t2 = (- (S_Fx * Dx + S_Fy * Dy + S_Fz * Dz) - sqrt(discriminant)) / (Dx**2 + Dy**2 + Dz**2)

        # Calcul des coordonnées des points d'intersection
        x1 = Fx + t1 * Dx
        y1 = Fy + t1 * Dy
        z1 = Fz + t1 * Dz

        x2 = Fx + t2 * Dx
        y2 = Fy + t2 * Dy
        z2 = Fz + t2 * Dz

        # Calcul de la distance entre le centre de la sphère et le point d'intersection
        distance1 = sqrt((x1 - Sx)**2 + (y1 - Sy)**2 + (z1 - Sz)**2)
        distance2 = sqrt((x2 - Sx)**2 + (y2 - Sy)**2 + (z2 - Sz)**2)

        return (x1, y1, z1), (x2, y2, z2), distance1, distance2
    else:
        return None



# Exemple d'utilisation
Sx, Sy, Sz = 0, 8.29, -4.7  # Centre de la sphère
R = 1  # Rayon de la sphère
Fx, Fy, Fz = 0, 0, 5  # Point de départ du rayon
Px, Py, Pz = 0, 5, 0  # Point d'arrivée du rayon

intersection = intersection_sphere_rayon(Sx, Sy, Sz, R, Fx, Fy, Fz, Px, Py, Pz)
print(intersection)