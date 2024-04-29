import numpy as np
from vecteur import Vecteur
from point import Point
from couleur import Couleur

class Scene:
    """La classe scène contient une référence à la caméra, une liste d'objets, une liste de lumières,
    une lumière ambiante et le fichier image."""

    def __init__(self, camera, list_objets,list_lumiere, fichier_image):
        
        self.camera = camera
        self.list_lumiere  = list_lumiere
        self.list_objets = list_objets
        self.pixels = np.zeros((self.camera.height, self.camera.width, 3))
        self.fichier_image = fichier_image

    def rendre_3D_in_2D(self):
        """Convertit les coordonnées 3D des objets en coordonnées 2D pour le rendu."""

        for y in range(self.camera.height):
            for x in range(self.camera.width):
                
                rayon_vue = self.camera.rayon(x,y) 
                self.modf_pixel(x, y, self.lancer_rayon(rayon_vue))
            print("{:3.0f}%".format(float(y) / float(self.camera.height) * 100), end="\r")  # Affiche la progression du rendu

    def lancer_rayon(self, rayon_vue):
        """Lance un rayon et calcule la couleur du pixel correspondant."""
        couler = Couleur(0,0,0) # couleur par défaut pour le pixel est noir

        # on cherche l'objet le plus proche qui intersecte avec le rayon vue
        dist_obj, obj_int = self.objet_proche(rayon_vue)
    
       
        
        if obj_int is None  :
            return couler # s'il n'y a pas d'intersection, la couleur du pixel reste noire
        
         
        obje_a_camera = dist_obj - self.camera.f.pos[2]
        if  obje_a_camera <= 0 :
            return couler # s'il n'y a pas d'intersection, la couleur du pixel reste noire
        
        point_intersection = obj_int.intersection_point(rayon_vue)  # Calcule la position du point d'impact
        # print("point_intersection" ,point_intersection.pos)
        int_normal = obj_int.normal(point_intersection)  # Calcule la normale à la surface touchée

        # sinon, on calcule la couleur du pixel
        # couler += self.couleur_objet(rayon_vue, obj_int ,int_normal)
        couler += self.couleur_objet( obj_int ,point_intersection,int_normal)
        return couler



    def couleur_objet(self, obj_int ,point_intersection,int_obj_normal):
    #    obj_color = material.color_at(hit_pos)  # Récupère la couleur de l'objet à la position du point d'impact
       obj_color =obj_int.couleur
       """
       cof_amb = obj_int.ambient
       brillance_speculaire = 50
       a_cam = (point_intersection - self.camera.position ).normalize()   # Vecteur du point d'impact à la caméra
       couleur_final  = Couleur(0,0,0)
    #  couleur_final = 
       cof_dif = obj_int.diffuse
       coef_spec = obj_int.specular



    #    couleur_final =  obj_color 
       # Calcul de l'éclairage pour chaque source lumineuse de la scène
       for lum in self.list_lumiere:
            # colour_lum = lum.couleur  
            # norma_lum = lum.position - point_intersection 
            # norma_lum = norma_lum.normalize()
            # couleur_final+=self.Lumiere_diffuse (obj_color,cof_amb ,colour_lum ,cof_dif,norma_lum ,int_obj_normal  )
            # a_lum = Vecteur(point_intersection, lum.position - point_intersection)  # Vecteur du point d'impact à la source lumineuse
            a_lum = (point_intersection -lum.position).normalize() 
            diff = lum.couleur*(int_obj_normal.dot_product(a_lum)) * cof_dif
            
            rayan_reflech =  int_obj_normal *( 2*(((a_lum)*-1).dot_product(int_obj_normal)))  + a_lum
            sepecul = ( (rayan_reflech.dot_product(a_cam) ) ** brillance_speculaire ) * coef_spec
            
            couleur_final += obj_color *( cof_amb + diff) # + lum.couleur * sepecul
            #print(couleur_final.form_couleur.pos)
           
            
            a_lum =point_intersection -lum.position  # Vecteur du point d'impact à la source lumineuse
            # Ombrage diffus (Lambert)
            couleur_final += (
                obj_color *
                cof_amb *
                Couleur(0,0,0)              
            )
            couleur_final += (
                obj_color*
                obj_int.diffuse
                * max(int_obj_normal.dot_product(a_lum), 0)    
            )
            # print(int_obj_normal.dot_product(a_lum))
            # Ombrage spéculaire (Blinn-Phong)
            # mi_distance = (a_lum  a_cam).normalize()  # Vecteur de mi-distance
            couleur_final += (
                obj_int.specular
                * max(a_lum.dot_product(a_cam), 0) ** brillance_speculaire   
            )
            print(max(int_obj_normal.dot_product(mi_distance), 0) ** brillance_speculaire)
            """




       
       return  obj_color

    def Lumiere_diffuse (self ,color_objet,cof_amb ,colour_lum ,cof_dif,norma_lum ,norma_obj  ) :
        # return l_d = None 
        l_o= color_objet.form_couleur.pos # colour de objet 
        l_a = Couleur(0,0,0).form_couleur.pos # coulour ambient 

        K_a = cof_amb   # coif de ambient 
        l_i = colour_lum.form_couleur.pos  # coulor de lumer 
        k_d = cof_dif  #cof diffuse 
        L = norma_lum.pos  # normal de lumire 
        N = norma_obj.pos # norma de objet 

        l_d =(l_o*((l_a*K_a)+(l_i*k_d*np.dot(L,N)))) 
        print(l_d)
       # Conversion des valeurs de couleur pour s'assurer qu'elles sont dans la plage [0, 1]
        R = min(1.0, max(0.0, l_d[0]))
        V = min(1.0, max(0.0, (l_d[1])))
        B = min(1.0, max(0.0, l_d[2])) 

        return Couleur(R,V,B)




        



    def objet_proche(self, rayon_vue):
        """Trouve l'objet le plus proche intersectant avec le rayon donné."""
        dist_min = None
        obj_intersect = None

        for obj in self.list_objets:
            dist = obj.intersection_distance(rayon_vue)
            if dist is not None :# and (obj_intersect is None or dist < dist_min):
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
            img_final.write("P3 {} {}\n255\n".format(self.camera.width, self.camera.height))
            for ligne in self.pixels:
                for pixel in ligne:
                    # Utilisation de trans_en_octet pour convertir chaque composante de couleur
                    
                    
                    red = self.trans_en_octet(pixel[0])
                    green = self.trans_en_octet(pixel[1])
                    blue = self.trans_en_octet(pixel[2])
                    # Écriture des valeurs RGB dans le fichier
                    img_final.write("{} {} {} ".format(red, green, blue))

                img_final.write("\n")
