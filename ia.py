import random
import time

class IA:
    def __init__(self):
        self.name = "IA"

    def random_move(self, board):
        legal_moves = list(board.legal_moves)
        return random.choice(legal_moves)