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
    
    def old_minimax (self,depth,chess,move,color):
        temp_chess = copy.deepcopy(chess)
        temp_chess.move(move.move_from[0],move.move_from[1],move.move_to[0],move.move_to[1])
        if (move != None):
            if (depth == 0): return move.val
            else:
                if (color == 'b'):
                    best_move = Move(-1,-1,-1,-1,-1001)
                    for c_move in temp_chess.get_possible_moves('b'):
                        if (best_move == move or self.old_minimax(depth-1,temp_chess,c_move,'w') >= best_move.val):
                            best_move = c_move
                    return best_move.val
                else:
                    best_move = Move(-1,-1,-1,-1,1001)
                    for c_move in temp_chess.get_possible_moves('w'):
                        if (best_move == move or self.old_minimax(depth-1,temp_chess,c_move,'b') < best_move.val):
                            best_move = c_move
                    return best_move.val

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