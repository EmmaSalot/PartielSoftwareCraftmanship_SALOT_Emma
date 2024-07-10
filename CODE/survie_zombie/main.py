from models.carte import Carte
from models.position import Position
from models.ressource import Ressource
from models.survivant import Survivant
from models.zombie import Zombie
from simulation.simulation import Simulation

carte = Carte(10, 10)

carte.ajouter_ressource(Ressource("nourriture", Position(3, 4)))
carte.ajouter_ressource(Ressource("eau", Position(5, 7)))
carte.ajouter_ressource(Ressource("armes", Position(1, 2)))
carte.ajouter_zombie(Zombie(Position(4, 4)))
carte.ajouter_zombie(Zombie(Position(6, 7)))

survivant = Survivant(Position(5, 5), "nord", 100)

simulation = Simulation(carte, survivant)
try:
    simulation.explorer(commandes = ["avancer", "tourner à gauche", "avancer", "avancer"])
except Exception as e:
    print(e)

print(f"Position du survivant: ({survivant.position.x}, {survivant.position.y})")
print(f"Santé du survivant: {survivant.sante}")
print(f"Inventaire du survivant: {[r.type for r in survivant.inventaire]}")
