from ai.node import Node
from ai.move import Move
import copy
import threading

class Ai:

    def choose_move (self):
        threads = []
        for move in get_moves(self.chess,'b'):
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
        #best_move = None
        #for move in self.get_moves(self.chess,'b'):
        #    print(move.values)
        #    if (best_move == None or self.minimax(2,copy.deepcopy(self.chess),move,'w') > best_move.val):
        #        best_move = move

    def __init__ (self,chess):
        self.chess = chess

class MinimaxThread (threading.Thread):

    def run (self):
        print ("Starting " + self.name)
        self.result = minimax(2,self.chess,self.move,self.color)
        print ("Exiting " + self.name)

    def __init__ (self,name,chess,move,color):
      threading.Thread.__init__(self)
      self.name = name
      self.chess = chess
      self.move = move
      self.color = color

def minimax (depth,chess,move,color):
        temp_chess = copy.deepcopy(chess)
        temp_chess.move(move.move_from[0],move.move_from[1],move.move_to[0],move.move_to[1])
        if (depth == 0): return move.val
        else:
            if (color == 'b'):
                best_move = None
                for move in get_moves(temp_chess,'b'):
                    if (best_move == None or minimax(depth-1,temp_chess,move,'w') >= best_move.val):
                        best_move = move
                return best_move.val
            else:
                best_move = None
                for move in get_moves(temp_chess,'w'):
                    if (best_move == None or minimax(depth-1,temp_chess,move,'b') < best_move.val):
                        best_move = move
                return best_move.val

def get_moves (chess,color):
    return chess.get_possible_moves(color)