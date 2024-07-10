import unittest
from models.carte import Carte
from models.position import Position
from models.ressource import Ressource
from models.zombie import Zombie

class TestCarte(unittest.TestCase):
    def setUp(self):
        self.carte = Carte(10, 10)

    def test_ajouter_ressource(self):
        ressource = Ressource("nourriture", Position(3, 4))
        self.carte.ajouter_ressource(ressource)
        self.assertIn(ressource, self.carte.ressources)

    def test_ajouter_zombie(self):
        zombie = Zombie(Position(4, 4))
        self.carte.ajouter_zombie(zombie)
        self.assertIn(zombie, self.carte.zombies)

    def test_est_position_valide(self):
        self.assertTrue(self.carte.est_position_valide(Position(5, 5)))
        self.assertFalse(self.carte.est_position_valide(Position(11, 11)))

    def test_obtenir_ressource(self):
        ressource = Ressource("nourriture", Position(3, 4))
        self.carte.ajouter_ressource(ressource)
        self.assertEqual(self.carte.obtenir_ressource(Position(3, 4)), ressource)

    def test_obtenir_zombies(self):
        zombie = Zombie(Position(4, 4))
        self.carte.ajouter_zombie(zombie)
        self.assertIn(zombie, self.carte.obtenir_zombies(Position(4, 4)))

if __name__ == '__main__':
    unittest.main()
