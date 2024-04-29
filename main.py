import numpy as np


from vecteur import Vecteur
from scene import Scene
from point import Point
from camera import Camera


def main():
    WIDTH = 3
    HEIGHT = 2
    fichier_image = "image.ppm"
    camera = Camera(Point((0,0,5)))

    imag_scen = Scene(WIDTH, HEIGHT,camera, fichier_image)

    rouge = np.array([1, 0, 0])
    vert = np.array([0, 1, 0])
    bleu = np.array([0, 0, 1])

    imag_scen.modf_pixel(0,0, rouge)
    imag_scen.modf_pixel(1,0,vert)
    imag_scen.modf_pixel(2,0,bleu)

    imag_scen.modf_pixel(0,1,rouge + vert)
    imag_scen.modf_pixel(1,1,vert +bleu)
    imag_scen.modf_pixel(2,1,bleu +rouge)

    imag_scen.image_ppm()


if __name__ == "__main__":
    main()
