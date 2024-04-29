
from point import Point
from vecteur import Vecteur
class Camera():
    def __init__(self, width, height, position ,direction = (0,0,0),orientation = 0 ,focale = (0,0,5)):
        self.width = width
        self.height = height
        self.position = position
        self.direction= direction
        self.orientation =orientation
        self.f = Point(focale)


    def rayon(self,x,y) :
        x0, x1 = -1.0, 1.0
        y0, y1 = -1.0, 1.0

        D = Point((1, 0, 0))
        H = Point((0, 1, 0))
        C = Point((0, 0, 0))
        F = self.f
        

        h = self.height
        l = self.width


        # Calcul des dimensions des pixels dans l'espace 3D projeté sur le plan 2D de l'image.
        # dx représente la largeur d'un pixel dans la direction horizontale.
        # dy représente la hauteur d'un pixel dans la direction verticale.

        dx = (x1 - x0) / (self.width - 1)  
        dy = (y1 - y0) / (self.height - 1)

        
        p0 = Point((-1,1,0))
        pxy = p0 - H * (y * dy) + D * (x * dx)

        return Vecteur(F, pxy)




"""
class Camera:
    def __init__(self, largeur, hauteur, position, regarder, vecteur_haut, distance_focale):
        self.largeur = largeur
        self.hauteur = hauteur
        self.position = position
        self.regarder = regarder
        self.vecteur_haut = vecteur_haut
        self.distance_focale = distance_focale

        # Calculer le système de coordonnées de la caméra
        self.devant = (regarder - position).normaliser()
        self.droite = self.devant.produit_vectoriel(vecteur_haut).normaliser()
        self.haut = self.droite.produit_vectoriel(self.devant)

    def rayon(self, x, y):
        rapport_aspect = self.largeur / self.hauteur
        champ_vision = 60  # Champ de vision en degrés
        angle = np.tan(np.deg2rad(champ_vision / 2))
        pixel_x = (2 * ((x + 0.5) / self.largeur) - 1) * rapport_aspect * angle
        pixel_y = (1 - 2 * ((y + 0.5) / self.hauteur)) * angle

        direction = (self.devant + pixel_x * self.droite + pixel_y * self.haut).normaliser()

        origine = self.position
        point_fin = self.position + direction * self.distance_focale

        return Rayon(origine, direction)

# Exemple d'utilisation
camera = Camera(largeur=800, hauteur=600, position=Vector3(0, 0, -5), regarder=Vector3(0, 0, 0), vecteur_haut=Vector3(0, 1, 0), distance_focale=1)
rayon = camera.rayon(400, 300)
print("Origine du rayon:", rayon.origine)
print("Direction du rayon:", rayon.direction)
"""