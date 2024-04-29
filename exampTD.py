import numpy as np
from math import sqrt
from vecteur import Vecteur
from scene import Scene
from objet import Objet
from sphere import Sphere
from plant import Plant
from point import Point
from couleur import Couleur
from camera import Camera
from lumiere import Lumiere




def main(WIDTH, HEIGHT ,fichier_image):
    cam = Camera(WIDTH, HEIGHT,Point((0, 0, 5)) )


    
    # Création des objets de la scène
    sphere_1 = Sphere(Point((1, 0, -5)), Couleur(1, 0, 1), 1/sqrt(2))
    sphere_2 = Sphere(Point((-.9, 0, 3)), Couleur(1, 0, 0),.5)


    # Création des plans
    plan_1 = Plant(Point((0, 0, -10)), Couleur(0.5, 0.5, 0.5), Point((0, -3, 1)))
    plan_2 = Plant(Point((0, -15, 0)), Couleur(0.5, 0.5, 0.5), Point((0, 1, 0)))

    lis_obj = [sphere_1]



    # Création des lumières
    lumiere_1 = Lumiere(Point((0, 1, 20)))
    lumiere_ind = Lumiere(Point((1.5, -0.5, 5)))
    lumiere = [lumiere_1, lumiere_ind]

    

    # Création de la scène
    imag_scen = Scene( cam, lis_obj, lumiere, fichier_image)

    imag_scen.rendre_3D_in_2D()
    imag_scen.image_ppm()

if __name__ == "__main__":
    WIDTH = 200
    HEIGHT = 200
    fichier_image = "image.ppm"
    main(WIDTH, HEIGHT, fichier_image)
