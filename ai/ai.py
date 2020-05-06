from ai.move import Move
import copy
import threading
import random

class Ai:

    def choose_move (self):
        threads = []
        moves = get_moves(self.chess,'b')
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

class MinimaxThread (threading.Thread):

    def run (self):
        self.result = minimax(1,self.chess,self.move,self.color)

    def __init__ (self,name,chess,move,color):
      threading.Thread.__init__(self)
      self.name = name
      self.chess = chess
      self.move = move
      self.color = color

def minimax (depth,chess,move,color):
        temp_chess = copy.deepcopy(chess)
        temp_chess.move(move.move_from[0],move.move_from[1],move.move_to[0],move.move_to[1])
        if (move != None):
            if (depth == 0): return move.val
            else:
                if (color == 'b'):
                    best_move = Move(-1,-1,-1,-1,-1001)
                    for c_move in get_moves(temp_chess,'b'):
                        if (best_move == move or minimax(depth-1,temp_chess,c_move,'w') >= best_move.val):
                            best_move = c_move
                    return best_move.val
                else:
                    best_move = Move(-1,-1,-1,-1,1001)
                    for c_move in get_moves(temp_chess,'w'):
                        if (best_move == move or minimax(depth-1,temp_chess,c_move,'b') < best_move.val):
                            best_move = c_move
                    return best_move.val

def get_moves (chess,color):
    return chess.get_possible_moves(color)