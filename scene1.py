import numpy as np
from vecteur import Vecteur
from position import Position
from couleur import Couleur

class Scene:
    """La classe scène contient une référence à la caméra, une liste d'objets, une liste de lumières,
    une lumière ambiante et le fichier image."""

    def __init__(self, width, height, camera, list_objets,list_lumiere, fichier_image):
        self.width = width
        self.height = height
        self.camera = camera
        self.list_lumiere  = list_lumiere
        self.list_objets = list_objets
        self.pixels = np.zeros((height, width, 3))
        self.fichier_image = fichier_image

    def rendre_3D_in_2D(self):
        """Convertit les coordonnées 3D des objets en coordonnées 2D pour le rendu."""
        x0, x1 = -1.0, 1.0
        y0, y1 = -1.0, 1.0

        D = Position((1, 0, 0))
        H = Position((0, 1, 0))
        C = Position((0, 0, 0))
        F = Position((0,0,5))
        h = self.height
        l = self.width


        # Calcul des dimensions des pixels dans l'espace 3D projeté sur le plan 2D de l'image.
        # dx représente la largeur d'un pixel dans la direction horizontale.
        # dy représente la hauteur d'un pixel dans la direction verticale.

        dx = (x1 - x0) / (self.width - 1)  
        dy = (y1 - y0) / (self.height - 1)

        cam = self.camera
        p0 = Position((-1,1,0))

        #test 
        # pxy = p0 - H * (250 * dy) + D * (250 * dx)
        # print("pxy :", pxy.pos)
        # rayon_vue = Vecteur(F, pxy)
        # V = pxy -F
        # print ("V :" ,V.pos)
        # self.modf_pixel(0, 0, self.lancer_rayon(rayon_vue))

        for y in range(self.height):
            for x in range(self.width):
                pxy = p0 - H * (y * dy) + D * (x * dx)
                rayon_vue = Vecteur(F, pxy)
                self.modf_pixel(x, y, self.lancer_rayon(rayon_vue))
            print("{:3.0f}%".format(float(y) / float(h) * 100), end="\r")  # Affiche la progression du rendu

    def lancer_rayon(self, rayon_vue):
        """Lance un rayon et calcule la couleur du pixel correspondant."""
        couler = Couleur(0,0,0) # couleur par défaut pour le pixel est noir

        # on cherche l'objet le plus proche qui intersecte avec le rayon vue
        dist_obj, obj_int = self.objet_proche(rayon_vue)
    
       
        
        if obj_int is None  :
            return couler # s'il n'y a pas d'intersection, la couleur du pixel reste noire
        
         
        obje_a_camera =dist_obj- self.camera.f.pos[2]
        if  obje_a_camera <= 0 :
            return couler # s'il n'y a pas d'intersection, la couleur du pixel reste noire
        
        point_intersection = obj_int.intersection_point(rayon_vue)  # Calcule la position du point d'impact
        # print("point_intersection" ,point_intersection.pos)
        int_normal = obj_int.normal(point_intersection)  # Calcule la normale à la surface touchée

        # sinon, on calcule la couleur du pixel
        # couler += self.couleur_objet(rayon_vue, obj_int ,int_normal)
        couler += self.couleur_objet( obj_int ,point_intersection,int_normal)
        return couler



    def couleur_objet(self, obj_int, point_intersection, int_obj_normal):
        obj_color = obj_int.couleur
        cof_amb = obj_int.ambient
        brillance_speculaire = 50
        a_cam = self.camera.position - point_intersection  # Vecteur du point d'impact à la caméra
        couleur_final = obj_color

        for lum in self.list_lumiere:
            colour_lum = lum.couleur
            norma_lum = lum.position - point_intersection
            norma_lum = norma_lum.normalize()
            couleur_final += self.Lumiere_diffuse(obj_color, cof_amb, colour_lum, norma_lum, int_obj_normal)

        return couleur_final

    def Lumiere_diffuse(self, obj_color, cof_amb, colour_lum, norma_lum, norma_obj):
        l_a = Couleur(0, 0, 0).form_couleur  # couleur ambiante
        K_a = cof_amb   # coef. d'ambiante
        l_i = colour_lum.form_couleur  # couleur de la lumière
        L = norma_lum.pos  # vecteur normalisé de la lumière
        N = norma_obj.pos  # vecteur normalisé de l'objet

     l_d = obj_color * ((l_a * K_a) + (l_i * L.dot_product(N)))
    
    # Conversion des valeurs de couleur pour s'assurer qu'elles sont dans la plage [0, 1]
    R = min(1.0, max(0.0, l_d[0]))
    V = min(1.0, max(0.0, abs(l_d[1])))
    B = min(1.0, max(0.0, l_d[2])) 

    return Couleur(R, V, B)





        



    def objet_proche(self, rayon_vue):
        """Trouve l'objet le plus proche intersectant avec le rayon donné."""
        dist_min = None
        obj_intersect = None

        for obj in self.list_objets:
            dist = obj.intersection_distance(rayon_vue)
            if dist is not None and (obj_intersect is None or dist < dist_min):
                dist_min = dist
                obj_intersect = obj

        return (dist_min, obj_intersect)


    def modf_pixel(self, x, y, couleur):
        """Modifie le pixel de l'image avec la couleur donnée."""
        
        
        self.pixels[y, x] = couleur.form_couleur.pos
        

    def trans_en_octet(self, val):
        """
    Convertit une valeur de couleur de [0.0, 1.0] à [0, 255] (octet).

        """ 
        
        return max(min(int(val * 255), 255), 0)
    



    def image_ppm(self):
        """Génère un fichier image au format PPM."""
        with open(self.fichier_image, "w") as img_final:
            img_final.write("P3 {} {}\n255\n".format(self.width, self.height))
            for ligne in self.pixels:
                for pixel in ligne:
                    # Utilisation de trans_en_octet pour convertir chaque composante de couleur
                    
                    
                    red = self.trans_en_octet(pixel[0])
                    green = self.trans_en_octet(pixel[1])
                    blue = self.trans_en_octet(pixel[2])
                    # Écriture des valeurs RGB dans le fichier
                    img_final.write("{} {} {} ".format(red, green, blue))
                img_final.write("\n")
