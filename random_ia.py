import random
import time

class RandomIA:
    def __init__(self):
        self.name = "RandomIA"

    def random_move(self, board):
        if len(list(board.legal_moves)) == 0:
            return None
        legal_moves = list(board.legal_moves)
        return random.choice(legal_moves)