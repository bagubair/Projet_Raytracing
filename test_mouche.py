import numpy as np


from vecteur import Vecteur
from scene import Scene
from objet import Objet
from sphere import  Sphere
from position import Position
from couleur import Couleur
from camera import Camera


def main():
    WIDTH = 30
    HEIGHT = 20
    fichier_image = "image.ppm"

    cam = Camera(Position((0, 0, -1)) )
    lis_obj = [Sphere(Position((0,0,0)), Couleur(1, 0, 0),0.5)]

    imag_scen = Scene(WIDTH, HEIGHT, cam, lis_obj, fichier_image)

    imag_scen.rendre_3D_in_2D()

    imag_scen.image_ppm()


if __name__ == "__main__":
    main()
