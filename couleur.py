import numpy as np
from point import Point

class Couleur:
    def __init__(self, R, V, B):
        """Écrire la couleur sous forme de np.array [R V B]"""
        ""
        self.form_couleur = Point((R, V, B))

    def __add__(self, other):
        """
        Addition de deux couleurs.
        """
        return Couleur(*(self.form_couleur.pos + other.form_couleur.pos))

    def __sub__(self, other):
        """
        Soustraction de deux couleurs.
        """
        return Couleur(*(self.form_couleur.pos - other.form_couleur.pos))

    def __mul__(self, other):
        """
        Multiplication d'une couleur par une autre couleur (composante par composante).
        """
        if isinstance(other, Couleur):
            return Couleur(*(self.form_couleur.pos * other.form_couleur.pos))
        elif isinstance(other, (int, float)):
            return Couleur(*(self.form_couleur.pos * other))
        else:
            raise TypeError("Unsupported operand type(s) for *: '{}' and '{}'".format(type(self), type(other)))

    def __rmul__(self, scalar):
        """
        Multiplication d'une couleur par un scalaire (composante par composante).
        """
        return Couleur(*((self.form_couleur.pos * scalar )))


# # Création de deux couleurs
# couleur1 = Couleur(0.5, 0.3, 0.1)
# couleur2 = Couleur(0.2, 0.7, 0.4)

# # Addition de deux couleurs
# resultat_addition = couleur1 + couleur2
# print("Résultat de l'addition :", resultat_addition.form_couleur)  # Affiche [0.7 1.  0.5]

# # Soustraction de deux couleurs
# resultat_soustraction = couleur1 - couleur2
# print("Résultat de la soustraction :", resultat_soustraction.form_couleur)  # Affiche [ 0.3 -0.4 -0.3]

# # Multiplication d'une couleur par un scalaire
# scalaire = 2.5
# resultat_multiplication_scalaire = couleur1 * scalaire
# print("Résultat de la multiplication par un scalaire :", resultat_multiplication_scalaire.form_couleur)  # Affiche [1.25 0.75 0.25]

# # Multiplication de deux couleurs (composante par composante)
# resultat_multiplication_couleur = couleur1 * couleur2
# print("Résultat de la multiplication de deux couleurs :", resultat_multiplication_couleur.form_couleur)  # Affiche [0.1 0.21 0.04]
