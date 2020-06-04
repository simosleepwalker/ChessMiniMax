from ai.move import Move
import threading
import copy

class GetMovesThread (threading.Thread):

    def run (self):
        self.moves = []
        for move in self.piece.get_moves(self.chess,self.chess.get_king(self.piece.get_color())):
            self.moves.append(Move(self.piece.get_row(),self.piece.get_col(),move[0],move[1],self.chess.move_eval((self.piece.get_row(),self.piece.get_col()),(move[0],move[1]))))

    def __init__ (self,name,piece,chess):
      threading.Thread.__init__(self)
      self.name = name
      self.piece = piece
      self.chess = chess

class MinimaxThread (threading.Thread):

    def run (self):
        self.result = self.minimax(1,self.chess,self.move,self.color)

    def minimax (self,depth,chess,move,color):
        temp_chess = copy.deepcopy(chess)
        temp_chess.move(move.move_from[0],move.move_from[1],move.move_to[0],move.move_to[1])
        if (depth == 0): return move.val
        else:
            if (color == 'b'):
                moves = temp_chess.get_possible_moves('b')
                if (len(moves) == 0):
                    return move.val
                moves_values = map(self.minimax,[depth-1]*len(moves),[temp_chess]*len(moves),moves,['w']*len(moves))
                return max(moves_values)
            else:
                moves = temp_chess.get_possible_moves('w')
                if (len(moves) == 0):
                    return move.val
                moves_values = map(self.minimax,[depth-1]*len(moves),[temp_chess]*len(moves),moves,['w']*len(moves))
                return min(moves_values)

    def __init__ (self,name,chess,move,color):
      threading.Thread.__init__(self)
      self.name = name
      self.chess = chess
      self.move = move
      self.color = color