from ai.node import Node
from ai.move import Move
import copy

class Ai:

    def choose_move (self):
        best_move = None
        for move in self.get_moves(self.chess,'b'):
            if (best_move == None or self.minimax(3,self.chess,move) > best_move.value):
                best_move = move
        return best_move

    def minimax (self,depth,chess,move,color):
        temp_chess = copy.deepcopy(chess)
        temp_chess.move(move.move_from[0],move.move_from[1],move.move_to[0],move.move_to[1])
        if (depth == 0): return move.value
        else:
            if (color == 'b'):
                best_move = None
                for move in self.get_moves(temp_chess,'b'):
                    if (best_move == None or self.minimax(depth-1,temp_chess,move,'w') >= best_move):
                        best_move = move
                return best_move
            else:
                best_move = None
                for move in self.get_moves(temp_chess,'w'):
                    if (best_move == None or self.minimax(depth-1,temp_chess,move,'b') < best_move):
                        best_move = move
                return best_move

    def get_moves (self,chess,color):
        return chess.get_possible_moves(color)

    def __init__ (self,chess):
        self.chess = chess