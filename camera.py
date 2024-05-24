from point import Point
from vecteur import Vecteur

class Camera():
    def __init__(self, width, height, position, direction=Point(0, 0, 0), orientation=0, focale=3):
        self.width = width
        self.height = height
        self.position = position
        self.direction = direction
        self.orientation = orientation
        self.f = self.direction+Point(0,0,focale)  # Il semble que "focale" devrait être "f" et être de type Point.

    def rayon(self, x, y):
        x0, x1 = -1.0, 1.0
        y0, y1 = -1.0, 1.0

        D = Point(1, 0, 0)
        H = Point(0, 1, 0)
        C = self.direction
        F = self.f

        h = self.height
        l = self.width

        # Calcul des dimensions des pixels dans l'espace 3D projeté sur le plan 2D de l'image.
        # dx représente la largeur d'un pixel dans la direction horizontale.
        # dy représente la hauteur d'un pixel dans la direction verticale.
        dx = (x1 - x0) / (h - 1)
        dy = (y1 - y0) / (l - 1)
        
        # Calcul du point p0 qaund x ,y =0.
        p0 = C + H * ((h / 2 - dy / 2) / (h / 2)) - D * ((l / 2 - dx / 2) / (l / 2))

        # Calcul du point correspondant au pixel (x, y) sur l'écran en coordonnées 3D.
        pxy = p0 - H * (y * dy) + D * (x * dx)

        # Le vecteur directeur du rayon partant de pxy et allant vers F avec trasiontion au point origin.
        rayon_direction = Vecteur(F.normalize(), (pxy-F).normalize())

        return rayon_direction


# Test
if __name__ == "__main__":
    cam = Camera(200, 200, Point(0, 0, 0))

    rayon_vue = cam.rayon(0, 0)
    print(rayon_vue.extremite.components())  
