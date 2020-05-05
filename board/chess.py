from . import utils
from pieces.pieces import *
from ai.move import Move

class Chess:

    def __init__ (self):
        self.chess_grid = [ None ] * 64
        self.chess_grid[0] = Rook(1,1,0,'w')
        self.chess_grid[1] = Knight(1,2,1,'w')
        self.chess_grid[2] = Bishop(1,3,2,'w')
        self.chess_grid[3] = Queen(1,4,3,'w')
        self.chess_grid[4] = King(1,5,4,'w')
        self.chess_grid[5] = Bishop(1,6,5,'w')
        self.chess_grid[6] = Knight(1,7,6,'w')
        self.chess_grid[7] = Rook(1,8,7,'w')
        self.chess_grid[8] = Pawn(2,1,8,'w')
        self.chess_grid[9] = Pawn(2,2,9,'w')
        self.chess_grid[10] = Pawn(2,3,10,'w')
        self.chess_grid[11] = Pawn(2,4,11,'w')
        self.chess_grid[12] = Pawn(2,5,12,'w')
        self.chess_grid[13] = Pawn(2,6,13,'w')
        self.chess_grid[14] = Pawn(2,7,14,'w')
        self.chess_grid[15] = Pawn(2,8,15,'w')
        self.chess_grid[48] = Pawn(7,1,16,'b')
        self.chess_grid[49] = Pawn(7,2,17,'b')
        self.chess_grid[50] = Pawn(7,3,18,'b')
        self.chess_grid[51] = Pawn(7,4,19,'b')
        self.chess_grid[52] = Pawn(7,5,20,'b')
        self.chess_grid[53] = Pawn(7,6,21,'b')
        self.chess_grid[54] = Pawn(7,7,22,'b')
        self.chess_grid[55] = Pawn(7,8,23,'b')
        self.chess_grid[56] = Rook(8,1,24,'b')
        self.chess_grid[57] = Knight(8,2,25,'b')
        self.chess_grid[58] = Bishop(8,3,26,'b')
        self.chess_grid[59] = Queen(8,4,27,'b')
        self.chess_grid[60] = King(8,5,28,'b')
        self.chess_grid[61] = Bishop(8,6,29,'b')
        self.chess_grid[62] = Knight(8,7,30,'b')
        self.chess_grid[63] = Rook(8,8,31,'b')
        self.kingw = self.get_piece(1,5)
        self.kingb = self.get_piece(8,5)
        self.turn = 'w'
    
    def get_black_king (self):
        return self.kingb

    def get_white_king (self):
        return self.kingw

    def get_king (self,color):
        if (color == 'b'):
            return self.get_black_king()
        return self.get_white_king()

    def get_grid (self):
        return self.chess_grid

    def get_piece (self,row,col):
        return self.chess_grid[utils.get_index(row,col)]

    def move_eval (self,move):
        if (self.get_piece(move[0],move[1]) != None):
            if (self.get_piece(move[0],move[1]).get_color() == 'w'):
                return self.get_piece(move[0],move[1]).get_val()
            else:
                return - (self.get_piece(move[0],move[1]).get_val())
        return 0

    def get_possible_moves (self,color):
        moves = []
        for cell in self.chess_grid:
            if (cell != None and cell.color == color):
                if (color == 'b'):
                    for move in cell.get_moves(self,self.kingb):
                        moves.append(Move(cell.get_row(),cell.get_col(),move[0],move[1],self.move_eval(move)))
                else:
                    for move in cell.get_moves(self,self.kingw):
                        moves.append(Move(cell.get_row(),cell.get_col(),move[0],move[1],self.move_eval(move)))
        return moves

    def change_turn (self):
        if (self.turn == 'b'):
            self.turn = 'w'
        else:
            self.turn = 'b'
    
    def get_turn (self):
        return self.turn

    def move (self,row,col,nrow,ncol):
        self.get_grid()[utils.get_index(row,col)].move(nrow,ncol)
        self.get_grid()[utils.get_index(nrow,ncol)] = self.get_grid()[utils.get_index(row,col)]
        self.get_grid()[utils.get_index(row,col)] = None
        self.change_turn()

    def print_grid (self):
        for i in range(1,9):
            for j in range(1,9):
                if (self.get_grid()[utils.get_index(i,j)] != None):
                    print("| " + self.get_grid()[utils.get_index(i,j)].short_type() + " |", end="")
                else:
                    print("|   |", end="")
            print("")
        print("")