from models.carte import Carte
from models.survivant import Survivant

class Simulation:
    def __init__(self, carte, survivant):
        self.carte = carte
        self.survivant = survivant

    def explorer(self, commandes):
        for commande in commandes:
            if commande == "avancer":
                self.survivant.avancer()
            elif commande == "tourner à gauche":
                self.survivant.tourner_a_gauche()
            elif commande == "tourner à droite":
                self.survivant.tourner_a_droite()

            if not self.carte.est_position_valide(self.survivant.position):
                raise Exception("Le survivant est sorti de la carte et est mort.")

            ressource = self.carte.obtenir_ressource(self.survivant.position)
            if ressource:
                self.survivant.ramasser_ressource(ressource)
                self.carte.ressources.remove(ressource)

            zombies = self.carte.obtenir_zombies(self.survivant.position)
            if zombies:
                self.rencontrer_zombie(len(zombies))

            self.carte.deplacer_zombies()

    def rencontrer_zombie(self, nombre_de_zombies):
        self.survivant.perdre_sante(nombre_de_zombies * 10)
