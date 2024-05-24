import numpy as np
from vecteur import Vecteur
from point import Point
from couleur import Couleur
from plant import Plan
from sphere import Sphere

class Scene:
    """La classe scène contient une référence à la caméra, une liste d'objets, une liste de lumières,
    une lumière ambiante et le fichier image."""

    def __init__(self, camera, list_objets,list_lumiere,fichier_image,ambient= Point(0.5,0.5,.5)):
        
        self.camera = camera
        self.list_lumiere  = list_lumiere
        self.list_objets = list_objets
        self.couleur_ambient =ambient
        self.pixels = np.zeros((self.camera.height, self.camera.width, 3))
        self.fichier_image = fichier_image

    def rendre_3D_in_2D(self):
        """Convertit les coordonnées 3D des objets en coordonnées 2D pour le rendu."""

        for y in range(self.camera.height):
            for x in range(self.camera.width):
                rayon_vue = self.camera.rayon(x,y)
                
                self.modf_pixel(x, y, self.lancer_rayon(rayon_vue))
            print("{:3.0f}%".format(float(y) / float(self.camera.height) * 100), end="\r")  # Affiche la progression du rendu



        # # test 
        # y = int((self.camera.width/2)) 
        # x =int( self.camera.height/2 )
        # print(x)
        # print(y)
        
        # rayon_vue = self.camera.rayon(x,y)
        

        # print("rayon_vue.origine.pos" ,rayon_vue.origine.components()) 
        # print("rayon_vue.extremitee.pos" ,rayon_vue.extremite.components()) 
        # print("rayon_vue" , (rayon_vue.extremite-rayon_vue.origine).normalize().components())
       

        # self.modf_pixel(x, y, self.lancer_rayon(rayon_vue))

    def lancer_rayon(self, rayon_vue,bounce=0):
        """Lance un rayon et calcule la couleur du pixel correspondant."""
        couler = Couleur(0,0,0) # couleur par défaut pour le pixel est noir

        # le plus proche qui intersecte avec le rayon vue
        dist_obj, obj_int ,point_intersection = self.objet_proche(rayon_vue)
        
       
        
        if obj_int is None  :
            return couler # s'il n'y a pas d'intersection, la couleur du pixel reste noire
        
        int_normal = obj_int.normal(point_intersection)  # Calcule la normale à la surface touchée
        vecteur_rayon_vue = rayon_vue.extremite
        # if bounce == 1 : 
        #     print(rayon_vue.origine.components())
        #     print("rayon_vue.origine.components()",rayon_vue.extremite.components())
        #     print(obj_int)
        couler += self.couleur_objet( obj_int ,point_intersection,int_normal,vecteur_rayon_vue,bounce)
        return couler

    


       
      
    def couleur_objet(self, obj_int, point_intersection, int_obj_normal, vecteur_rayon_vue, bounce):
        I_o = self.couleur_objet_base(obj_int, point_intersection) 
        
        N = int_obj_normal.normalize()  
        V = vecteur_rayon_vue  

        n1 = 1  #(indice de réfraction de l'air)
        n2 = 1   #à 1.70 (indice de réfraction typique du verre)

        # I_a = Point(0.5, 0.5, 0.5)  # Intensité de la lumière ambiante
        # I_i = Point(0.9, 0.1, 0.1)  # Intensité de la lumière incidente

        # Coefficients
        Ka = obj_int.ambiant   
        Kd = obj_int.diffuse  
        Ks = obj_int.specular  
        Kt = obj_int.translucide 
        Kr = obj_int.reflexion
        Ko = obj_int.ombre
        
        n = 38  # Exposant de spécularité
        
        Ca = I_o*Ka 
        Cr = self.calcul_reflexion(V, N, bounce,point_intersection,obj_int) 
        Cd, Cs ,ombre= self.calcul_diffusion_speculaire(point_intersection, N, V, obj_int,I_o,n, bounce)
        Ct = self.calcul_refraction( V, N, n1, n2, point_intersection,bounce,obj_int)

        I = Ca*Ka + Cd*Kd + Cs*Ks +Cr*Kr # +Ct*Kt
        return I*(ombre)
    
    def couleur_objet_base(self, obj_int, point_intersection):
        I_o = obj_int.couleur
        if obj_int.texture_path:
            I_o = obj_int.couleur_texture(point_intersection)
        return I_o

    def calcul_reflexion(self, V, N, bounce, point_intersection,obj_int):
        Cr = Point(0, 0, 0)
        
        if bounce <1:
            # Formule de réflexion :
            #  R_r = (N * (2 * ((V*-1).dot_product(N)))) + V
            N = obj_int.normal(point_intersection).normalize()
            reflexion_dir = (((N * (2*(V*-1).dot_product(N)))+ V))
            
            
            reflexion_orig = point_intersection +(reflexion_dir)  # Point d'intersection légèrement décalé
            #R_r = R_r.normalize() #vecteur de réflexion 
            # if isinstance(obj_int,Sphere) :0mm
            #     print("reflexion_dir" ,reflexion_dir.components())
               
            #     print("point_intersection",point_intersection.components())
            #     print("reflexion_orig",reflexion_orig.components())
            #     print("N",N.components())
            #     print("V",V.components())
            #     print("obj_int",obj_int)
            #     # print("reflexion_dir" ,reflexion_dir.components())
            
            
            V_R_r = Vecteur(reflexion_orig,reflexion_dir)
            Cr = self.lancer_rayon(V_R_r, bounce + 1) 

        return Cr
    def calcul_diffusion_speculaire(self, point_intersection, N, V, obj_int,I_o,n, bounce):
        Cd = Point(0,0,0)
        Cs= Point(0,0,0)
        for lum in self.list_lumiere:
            L = (point_intersection-lum.position ).normalize()  # Vecteur de point intr a  la source de lumière 
            R = (N * (2 * ((L*(-1)).dot_product(N)))) + L  # Vecteur de réflexion de lumiere
            R = R.normalize()
            # Calcul de l'ombrage lambertien (diffus)
            Cd = lum.couleur * ( (L*(-1)).dot_product(N)) 
            ombre = self.non_ombre_portee(point_intersection, lum, L, obj_int)

            # Calcul de la speculer 
            m = max(0, ((R).dot_product(V *-1)))
            Cs = lum.couleur * (m ** n) 
        return Cd, Cs ,ombre

        
    def calcul_refraction(self, V, N, n1, n2, point_intersection,bounce,obj_int):
        Ct = Point(0, 0, 0)

        refract_dir = self.refract(V, N, n1, n2)
        
        #refract_orig = point_intersection - N*2.001
        refract_orig = point_intersection + refract_dir*10
        rayon_vue = Vecteur(point_intersection ,refract_dir)
        dist, obj ,point = self.objet_proche( rayon_vue)
        
        if point :
                
            refract_orig = point +refract_dir*10

                
        if bounce < 1 :
            Ct += self.lancer_rayon(Vecteur(refract_orig,refract_dir), bounce + 1) 
 
        return Ct

    def refract(self, V, N, n1, n2):
        """ n2.R =n1.I +(n1cosI - n2cosT).N   # n =n1/n2
            > R = n.I + (n*cosI- cosT).N

       """
        n = n1 / n2
        cosI = (N).dot_product(V*-1) 
        """ n1 sinI = n2sinT
            >sinT = nsinI
            >sinT² = n²sinI²   #sin(i)² +cos(i)² = 1
            >sinT² = n²(1-cosI²)
        """

        sinT2 = n ** 2 * (1.0 - cosI ** 2) 
        
        cosT = (1.0 - sinT2) ** 0.5
        
        return V * n + N * (n * cosI - cosT)
        

    def non_ombre_portee(self, point_intersection, lumiere,L,obj_int):
        liste_objets = self.list_objets
        for objet in liste_objets:
            
            if objet is not obj_int:
                
                
                distance_to_obj,point = objet.intersection(Vecteur(point_intersection,lumiere.position))
                
                if distance_to_obj is not None and distance_to_obj < lumiere.position.distance(point_intersection):
                    return False # si il y a de ombre 
        return True #oui pas de ombre
        
    def objet_proche(self, rayon_vue):
        """Trouve l'objet le plus proche intersectant avec le rayon donné."""
        dist_min = None
        obj_intersect = None
        point_intersection = None
        point_min =None

        for obj in self.list_objets:
            dist,point_intersection = obj.intersection(rayon_vue)

            if dist is not None and (obj_intersect is None or dist < dist_min) :
                dist_min = dist
                obj_intersect = obj
                point_min = point_intersection


        # #test 
        # print("point_intersection ",point_min.pos)
        # print("dist",dist)
        # #return 
        # point_intersection  [ 0.00502016 -0.00502016 -4.9950547 ]
        # dist 4.995059749768852

        return (dist_min, obj_intersect ,point_min)


    def modf_pixel(self, x, y, couleur):
        """Modifie le pixel de l'image avec la couleur donnée."""
        
        
        self.pixels[y, x] = couleur.components()
        

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
