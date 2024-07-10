import unittest
from models.position import Position
from models.survivant import Survivant
from models.ressource import Ressource

class TestSurvivant(unittest.TestCase):
    def setUp(self):
        self.survivant = Survivant(Position(5, 5), 'nord', 100)

    def test_avancer(self):
        self.survivant.avancer()
        self.assertEqual(self.survivant.position, Position(5, 4))

    def test_tourner_a_gauche(self):
        self.survivant.tourner_a_gauche()
        self.assertEqual(self.survivant.orientation, 'ouest')

    def test_tourner_a_droite(self):
        self.survivant.tourner_a_droite()
        self.assertEqual(self.survivant.orientation, 'est')

    def test_ramasser_ressource(self):
        ressource = Ressource("nourriture", Position(5, 5))
        self.survivant.ramasser_ressource(ressource)
        self.assertIn(ressource, self.survivant.inventaire)

    def test_perdre_sante(self):
        self.survivant.perdre_sante(10)
        self.assertEqual(self.survivant.sante, 90)

if __name__ == '__main__':
    unittest.main()
