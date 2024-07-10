import unittest
from models.carte import Carte
from models.position import Position
from models.ressource import Ressource
from models.survivant import Survivant
from models.zombie import Zombie
from simulation.simulation import Simulation

class TestSimulation(unittest.TestCase):
    def setUp(self):
        self.carte = Carte(10, 10)
        self.survivant = Survivant(Position(5, 5), 'nord', 100)
        self.simulation = Simulation(self.carte, self.survivant)

    def test_survivant_ramasse_ressource(self):
        ressource = Ressource("nourriture", Position(5, 4))
        self.carte.ajouter_ressource(ressource)
        self.simulation.explorer(["avancer"])
        self.assertIn(ressource, self.survivant.inventaire)

    def test_survivant_rencontre_zombie(self):
        zombie = Zombie(Position(5, 4))
        self.carte.ajouter_zombie(zombie)
        self.simulation.explorer([ "avancer", "avancer"])
        self.assertEqual(self.survivant.sante, 90)

    def test_survivant_sort_de_la_carte(self):
        with self.assertRaises(Exception):
            self.simulation.explorer(["tourner à gauche", "avancer", "avancer","avancer","avancer","avancer","avancer"])

if __name__ == '__main__':
    unittest.main()
