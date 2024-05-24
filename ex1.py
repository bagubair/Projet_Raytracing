import numpy as np
from math import sqrt
from PIL import Image

from vecteur import Vecteur
from scene import Scene
from objet import Objet
from sphere import Sphere
from plant import Plan
from point import Point
from couleur import Couleur
from camera import Camera
from lumiere import Lumiere

def main(WIDTH, HEIGHT, fichier_image):
    # la caméra
    cam = Camera(WIDTH, HEIGHT, Point(0, 1, 5))

    
    
    
    # objets de la scène
    lis_obj = [
      #class Sphere(position, couleur, rayon, texture_path=None, diffuse=1, specular=1, reflexion=0.5, ombre=True, ambiant=.5, translucide=0)
        Sphere(Point(.75, .1, -1.*4), Couleur(0, 0, 1), .6,"texteur/t4.jpg",.5,.8,0,0,.8,0),
        Sphere(Point(-.75, .1, -2.25*4), Couleur(.5, .223, .5), .6,None,.5,.5,0.5,2,.5,.5),
        Sphere(Point(-2.75, .1, -3.5*4), Couleur(1., .572, .184), .6,None,.5,.5,0.5,2,.5,.5),
        # Sphere(Point(0, 0, -2), Couleur(.5, .223, .5), .6),
        # Plan à l'arrière
      #   Plan(Point(0, 0, -50), Couleur(1, 1, 1), Point(0, 0, 1)),
        # Plan sur le sol avec texture
    # def __init__(self, position, couleur, normal, texture_path =None, diffuse=0, specular=0, reflexion=0, ombre=0,ambiant =.5,translucide=0):
      
        Plan(Point(0, -.5, 0), Couleur(.75, .75, .75), Point(0, 1, 0), "texteur/t.jpg",1,1,0,.9,1,0)
     ]

    #  lumières de la scène
    lumiere = [
      Lumiere(Point(10, 10, 30))
      ]

    # Création de la scène
    imag_scen = Scene(cam, lis_obj, lumiere, fichier_image)
    imag_scen.rendre_3D_in_2D()
    imag_scen.image_ppm()

if __name__ == "__main__":
    WIDTH = 1500
    HEIGHT = 1500    
    fichier_image = "image.ppm"
    main(WIDTH, HEIGHT, fichier_image)
