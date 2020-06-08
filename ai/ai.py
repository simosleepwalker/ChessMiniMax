from ai.move import Move
from threads import MinimaxThread
import copy
import random

class Ai:

    def choose_move (self):
        threads = []
        #get moves and shuffle them in order to choose a random move when there are more moves with the same values
        moves = self.chess.get_possible_moves('b')
        random.shuffle(moves)
        #start a minimax thread for each move with depth 1 because summing up this call and the ones in the minimax i get a 3-depth prediction
        for move in moves:
            thread = MinimaxThread("Thread minimax",copy.deepcopy(self.chess),move,'w',1)
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