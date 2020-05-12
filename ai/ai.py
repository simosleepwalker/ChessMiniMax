from ai.move import Move
from threads import MinimaxThread
import copy
import random

class Ai:

    def choose_move (self):
        threads = []
        moves = self.chess.get_possible_moves('b')
        random.shuffle(moves)
        for move in moves:
            thread = MinimaxThread("Thread minimax",copy.deepcopy(self.chess),move,'w')
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
        best_move = None
        for thread in threads:
            if (best_move == None or thread.result >= best_move.val):
                best_move = thread.move
        return best_move

    def __init__ (self,chess):
        self.chess = chess