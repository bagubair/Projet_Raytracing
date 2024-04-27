import numpy as np
from math import sqrt


from vecteur import Vecteur
from scene import Scene
from objet import Objet
from sphere import  Sphere
from position import Position
from couleur import Couleur
from camera import Camera
from lumiere import Lumiere



def main():
    WIDTH = 500
    HEIGHT = 500
    fichier_image = "image.ppm"

    # cam = Camera(Position((0, 0, -1)) )
    
    # lis_obj = [Sphere(Position((-.9, 0, 3)), Couleur(1, 0, 0),.5)]
    # lumiere = [Lumiere(Position((0, 0, -10)))]
    # imag_scen = Scene(WIDTH, HEIGHT, cam, lis_obj,lumiere, fichier_image)


    cam = Camera(Position((0, 0, 0)) )
    # lis_obj = [Sphere(Position((0, 9-(1/sqrt(2)),-4-(1/sqrt(2)))), Couleur(1, 1, 0),.5)]


    lis_obj = [Sphere(Position((0, -.5,-5-.5)), Couleur(1, 1, 0),1/sqrt(2)),Sphere(Position((0, 0,-8)), Couleur(0, 1, 0),0.4)]

    lumiere = [Lumiere(Position((0, 0,2)))]
    # lumiere = []
    imag_scen = Scene(WIDTH, HEIGHT, cam, lis_obj,lumiere, fichier_image)

    imag_scen.rendre_3D_in_2D()

    imag_scen.image_ppm()


if __name__ == "__main__":
    main()
