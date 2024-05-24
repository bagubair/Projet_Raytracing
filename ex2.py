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
        Sphere(Point(0, 0, -2), Couleur(1,0 , 0), .6,None,.1,1,1,.5,.5,0),
        # Sphere(Point(.8, 0, -5), Couleur(0,0 , 1), .5,None,.1,.5,0,.5,.5,1),
        Plan(Point(0, -.6, 0), Couleur(.75, .75, .75), Point(0, 1, 0), "texteur/t.jpg",1,1,1,0,1,0) ,
        # Plan(Point(0, 0, -50), Couleur(1,1, 1), Point(0, 0, 1),None,1,1,0,0,0,1) ,
     ]
    #  lumières de la scène
    lumiere = [
      Lumiere(Point(-10, 5,10))
      ]

    # Création de la scène
    imag_scen = Scene(cam, lis_obj, lumiere, fichier_image)
    imag_scen.rendre_3D_in_2D()
    imag_scen.image_ppm()

if __name__ == "__main__":
    WIDTH = 200
    HEIGHT = 200    
    fichier_image = "image.ppm"
    main(WIDTH, HEIGHT, fichier_image)
