

class Objet:
    def __init__(self, position, couleur, diffuse= .7, specular=.8 ,reflexion= 1,ombre=2):
        self.position = position
        self.couleur = couleur
        
        self.diffuse = diffuse
        self.specular = specular
        self.reflexion =reflexion
        self.ombre  =ombre 
    def normal(self, surface_point):
        """Calcule la normale à la surface de la sphère au point donné."""
        return (surface_point -self.position   ).normalize()


    