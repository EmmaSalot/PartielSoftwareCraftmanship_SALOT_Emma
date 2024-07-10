from models.position import Position
from models.ressource import Ressource
from models.zombie import Zombie

class Carte:
    def __init__(self, taille_x, taille_y):
        self.taille_x = taille_x
        self.taille_y = taille_y
        self.ressources = []
        self.zombies = []

    def ajouter_ressource(self, ressource):
        self.ressources.append(ressource)

    def ajouter_zombie(self, zombie):
        self.zombies.append(zombie)

    def est_position_valide(self, position):
        return 0 <= position.x < self.taille_x and 0 <= position.y < self.taille_y

    def obtenir_ressource(self, position):
        for ressource in self.ressources:
            if ressource.position == position:
                return ressource
        return None

    def obtenir_zombies(self, position):
        return [zombie for zombie in self.zombies if zombie.position == position]

    def deplacer_zombies(self):
        for zombie in self.zombies:
            zombie.deplacer_aleatoirement(self.taille_x, self.taille_y)
