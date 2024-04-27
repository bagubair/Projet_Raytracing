import numpy as np

class Couleur:
    def __init__(self, R, V, B):
        """Écrire la couleur sous forme de np.array [R V B]"""
        self.form_couleur = np.array((R, V, B))

    def __add__(self, other):
        """
        Addition de deux couleurs.
        """
        return Couleur(*(self.form_couleur + other.form_couleur))

    def __sub__(self, other):
        """
        Soustraction de deux couleurs.
        """
        return Couleur(*(self.form_couleur - other.form_couleur))

    def __mul__(self, other):
        """
        Multiplication d'une couleur par une autre couleur (composante par composante).
        """
        return Couleur(*(self.form_couleur * other.form_couleur))
