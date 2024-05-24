from PIL import Image
from couleur import Couleur

class Objet:
    def __init__(self, position, couleur,  texture_path=None,diffuse= 1, specular=1 ,reflexion= 0.5,ombre=True,ambiant=.5,translucide=0):
        self.position = position
        self.couleur = couleur
        self.ambiant =ambiant 
        self.diffuse = diffuse
        self.specular = specular
        self.reflexion =reflexion
        self.ombre  =ombre
        self.texture_path = texture_path
        self.translucide = translucide
        if self.texture_path :
            self.texture = self.charger_texture(texture_path)


    def charger_texture(self, texture_path):
        """Charge l'image de texture à partir du chemin spécifié."""
        try:
            texture = Image.open(texture_path)
            return texture
        except Exception as e:
            raise RuntimeError("Erreur : Impossible de charger l'image de texture à partir du chemin spécifié.") 


    