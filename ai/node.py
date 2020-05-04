class Node:

    def __init__ (self,parent,move,children = []):
        self.parent = parent
        self.move = move
        self.children = children
        self.best_move = None