from models.position import Position
from models.ressource import Ressource

class Survivant:
    def __init__(self, position, orientation, sante):
        self.position = position
        self.orientation = orientation
        self.sante = sante
        self.inventaire = []

    def avancer(self):
        if self.orientation == 'nord':
            self.position.y -= 1
        elif self.orientation == 'sud':
            self.position.y += 1
        elif self.orientation == 'est':
            self.position.x += 1
        elif self.orientation == 'ouest':
            self.position.x -= 1

    def tourner_a_gauche(self):
        orientations = ['nord', 'ouest', 'sud', 'est']
        self.orientation = orientations[(orientations.index(self.orientation) + 1) % 4]

    def tourner_a_droite(self):
        orientations = ['nord', 'est', 'sud', 'ouest']
        self.orientation = orientations[(orientations.index(self.orientation) + 1) % 4]

    def ramasser_ressource(self, ressource):
        self.inventaire.append(ressource)

    def perdre_sante(self, quantite):
        self.sante -= quantite
