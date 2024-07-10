import unittest
from models.position import Position
from models.ressource import Ressource

class TestRessource(unittest.TestCase):
    def test_ressource_creation(self):
        ressource = Ressource("nourriture", Position(3, 4))
        self.assertEqual(ressource.type, "nourriture")
        self.assertEqual(ressource.position, Position(3, 4))

if __name__ == '__main__':
    unittest.main()
