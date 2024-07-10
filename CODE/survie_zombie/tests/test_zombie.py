import unittest
from models.position import Position
from models.zombie import Zombie

class TestZombie(unittest.TestCase):
    def test_deplacer_aleatoirement(self):
        zombie = Zombie(Position(4, 4))
        zombie.deplacer_aleatoirement(10, 10)
        self.assertTrue(0 <= zombie.position.x < 10)
        self.assertTrue(0 <= zombie.position.y < 10)

if __name__ == '__main__':
    unittest.main()
