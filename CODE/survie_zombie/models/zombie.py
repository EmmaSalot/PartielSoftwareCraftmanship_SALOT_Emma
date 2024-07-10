import random
from models.position import Position

class Zombie:
    def __init__(self, position):
        self.position = position

    def deplacer_aleatoirement(self, max_x, max_y):
        mouvements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        mouvement = random.choice(mouvements)
        self.position.x = min(max(0, self.position.x + mouvement[0]), max_x - 1)
        self.position.y = min(max(0, self.position.y + mouvement[1]), max_y - 1)
