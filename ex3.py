import numpy as np
from math import sqrt
from vecteur import Vecteur
from scene import Scene
from objet import Objet
from sphere import Sphere
from PIL import Image
# from sphere import CheckeredSphere

from plant import Plan
from point import Point
from couleur import Couleur
from camera import Camera
from lumiere import Lumiere




def main(WIDTH, HEIGHT ,fichier_image):
    
    cam = Camera(WIDTH, HEIGHT,Point(0, 0, 5) )
    # Définition de la classe  pour la couleur
    



    
    lis_obj = [

         #class Sphere(position, couleur, rayon, texture_path=None, diffuse=1, specular=1, reflexion=0.5, ombre=True, ambiant=.5, translucide=0)
        Sphere(Point(1, 0, -4), Couleur(1,1, 1),.5,"texteur/t4.jpg",.1,.9,0,0,.9,0),
        Sphere(Point(-1, 0, -4), Couleur.from_hex("#800000"),.5,None,.1,.9,0,0,.9,0),

        
        Sphere(Point(0, -.2, -1), Couleur(0,1,0),.3),
        Plan(Point(0, -.5, 0), Couleur(.75, .75, .75), Point(0, 1, 0),"texteur/t.jpg",.5,1,0,.9,1,0)


    ]



    # Création des lumières
    lumiere_1 = Lumiere(Point(1,10, 5))
    
    lumiere = [ lumiere_1 ]

    

    # Création de la scène
    imag_scen = Scene( cam, lis_obj, lumiere, fichier_image)

    imag_scen.rendre_3D_in_2D()
    imag_scen.image_ppm()

if __name__ == "__main__":
    WIDTH = 2000
    HEIGHT = 2000
    fichier_image = "image.ppm"
    main(WIDTH, HEIGHT, fichier_image)
