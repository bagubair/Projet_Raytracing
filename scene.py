import numpy as np
from vecteur import Vecteur
from position import Position
from couleur import Couleur

class Scene:
    """ la clsse scène contien : référence à la caméra, liste des objets, liste des lumières,
    lumière ambiante, fichier image """ 


    def __init__(self, width, height, camera, list_objets, fichier_image):
        self.width = width
        self.height = height
        self.camera = camera
        self.list_objets = list_objets

        self.pixels = np.zeros((height, width, 3), dtype=np.uint8)
        self.fichier_image = fichier_image



    def rendre_3D_in_2D(self):
        x0,x1 = -1.0 , 1.0
        x_move = (x1 - x0) / (self.width -1)
        print("x_move = ", x_move)

        aspect = self.width / self.height
        y0,y1 = -1.0/aspect , 1.0/aspect
        y_move = (y1 - y0) / (self.height -1)
        print("y_move = ", y_move)

        cam = self.camera

        for j in range(self.height):
            y = int(y0 + j * y_move)
            #print('y =',y)
            for i in range(self.width):
                x = int(x0 + i * x_move)
                #print('x = ',x)
                rayon_vue = Vecteur(cam.position, Position((x,y,0)) - cam.position) #le rayon de vue c'est un vecteur son origin le camera et la distination le point(x,y)
                self.modf_pixel(x,y, self.lancer_rayon( rayon_vue))






    def lancer_rayon(self, rayon_vue):
        couler = Couleur(0,0,0) #la couleur par defut pour le pixel sera noir
        #on cherche l'objet plus proche qu'intersecte avec le rayon vue

        dist_obj , obj = self.objet_proche(rayon_vue)

        if obj == 0 :
            return couler #si l'obj == 0 , c'est a dire pas d'intersection donc le couleur de pixel reste noir

        #sinon on calcule le couleur de pixle 
        pos_intersesc = rayon_vue.origine + rayon_vue.extremite * dist_obj
        couler += self.ajoute_couler(obj, pos_intersesc)

        return couler

    def objet_proche(self, rayon_vue):
        dist_min = 0
        obj_intersect = 0

        for obj in self.list_objets:
            dist = obj.intersection(rayon_vue)
            if (dist != 0) and ( (obj_intersect == 0) or (dist < dist_min)):
                dist_min = dist
                obj_intersect = obj

        return (dist_min, obj_intersect)

    def ajoute_couler(self, objet, pos_intersescect):
        return objet.couleur

    #partie modiliser le fichier Image en PPM 
    def modf_pixel(self, x, y, couleur):
        print(couleur)
        #print(self.pixels[2,5])
        #self.pixels[y, x] = couleur

    def trans_en_octet(self,val):
        """ transmetre la valeur de couler qu'est [0.0 , 1.0] a la valeur en octet[0 , 255]"""
        return np.uint8(np.clip(val * 255, 0, 255))

    def image_ppm(self):
        with open(self.fichier_image, "w") as img_final:
            img_final.write("P3 {} {}\n255\n".format(self.width, self.height))
            for linge in self.pixels:
                for pixl in linge:
                    """chaque pixle definie par 3 valeurs qui sont son couleur RGB 
                        chaque valeur entre 0 et 1 , donc on la transmit en octet [0 , 255]
                    """

                    img_final.write("{} {} {} ".format(
                        self.trans_en_octet(pixl[0]), self.trans_en_octet(pixl[1]), self.trans_en_octet(pixl[2])) )

                img_final.write("\n")
