from . import utils
from pieces.pieces import *
from ai.move import Move
from ai.ai import Ai
from threads import GetMovesThread

class Chess:
    
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

    def move_eval (self,move_from,move_to):
        val = 0
        temp_chess = copy.deepcopy(self)
        temp_chess.move(move_from[0],move_from[1],move_to[0],move_to[1])
        if (self.get_turn() == 'b'):
            if (self.get_piece(move_to[0],move_to[1]) != None):
                val += self.get_piece(move_to[0],move_to[1]).get_val()*2 - self.get_piece(move_from[0],move_from[1]).get_val()
            if (temp_chess.kingw.is_in_check(temp_chess)):
                val += 10
            if (temp_chess.kingw.is_in_check_mate(temp_chess)):
                val += 1000
        else:
            if (self.get_piece(move_to[0],move_to[1]) != None):
                val -= self.get_piece(move_to[0],move_to[1]).get_val()*2 - self.get_piece(move_from[0],move_from[1]).get_val()
            if (temp_chess.kingb.is_in_check(temp_chess)):
                val -= 10
            if (temp_chess.kingb.is_in_check_mate(temp_chess)):
                val -= 1000
        return val

    def get_possible_moves (self,color):
        moves = []
        threads = []
        for cell in self.chess_grid:
            if (cell != None and cell.color == color):
                thread = GetMovesThread("Thread minimax",cell,self)
                thread.start()
                threads.append(thread)
        for thread in threads:
            thread.join()
        for thread in threads:
            for move in thread.moves:
                moves.append(move)
        return moves

    def change_turn (self):
        if (self.turn == 'b'):
            self.turn = 'w'
        else:
            self.turn = 'b'
            move = self.ai.choose_move()
            if (move != None):
                self.move(move.move_from[0],move.move_from[1],move.move_to[0],move.move_to[1])
                self.turn = 'w'
    
    def get_turn (self):
        return self.turn

    def get_winner (self):
        if self.kingw.is_in_check_mate(self):
            return 'b'
        elif self.kingw.is_in_check_mate(self):
            return 'w'
        return None

    def move (self,row,col,nrow,ncol):
        self.get_grid()[utils.get_index(row,col)].move(nrow,ncol)
        self.get_grid()[utils.get_index(nrow,ncol)] = self.get_grid()[utils.get_index(row,col)]
        self.get_grid()[utils.get_index(row,col)] = None

    def print_grid (self):
        for i in range(1,9):
            for j in range(1,9):
                if (self.get_grid()[utils.get_index(i,j)] != None):
                    print("| " + self.get_grid()[utils.get_index(i,j)].short_type() + " |", end="")
                else:
                    print("|   |", end="")
            print("")
        print("")

    def __init__ (self):
        self.chess_grid = [ None ] * 64
        self.chess_grid[utils.get_index(1,1)] = King(1,1,1,'w')
        self.chess_grid[utils.get_index(8,8)] = King(8,8,5,'b')
        self.chess_grid[utils.get_index(8,2)] = Rook(8,2,2,'b')
        self.chess_grid[utils.get_index(1,8)] = Rook(1,8,3,'b')
        self.chess_grid[utils.get_index(2,1)] = Pawn(2,1,6,'w')
        self.chess_grid[utils.get_index(1,3)] = Pawn(1,3,7,'b')
        self.chess_grid[utils.get_index(6,7)] = Queen(6,7,4,'b')
        self.kingw = self.get_piece(1,1)
        self.kingb = self.get_piece(8,8)
        self.ai = Ai(self)
        self.turn = 'w'

    def prova3 (self):
        self.chess_grid = [ None ] * 64
        self.chess_grid[utils.get_index(7,5)] = King(7,5,1,'b')
        self.chess_grid[utils.get_index(5,3)] = King(5,3,5,'w')
        self.kingw = self.get_piece(7,5)
        self.kingb = self.get_piece(5,3)
        self.ai = Ai(self)
        self.turn = 'w'

    def prova2 (self):
        self.chess_grid = [ None ] * 64
        self.chess_grid[utils.get_index(8,8)] = King(8,8,1,'b')
        self.chess_grid[utils.get_index(4,8)] = Rook(4,8,2,'w')
        self.chess_grid[utils.get_index(6,6)] = Queen(6,6,3,'w')
        self.chess_grid[utils.get_index(7,5)] = Rook(7,5,4,'w')
        self.chess_grid[utils.get_index(1,1)] = King(1,1,5,'w')
        self.kingw = self.get_piece(1,1)
        self.kingb = self.get_piece(8,8)
        self.ai = Ai(self)
        self.turn = 'w'

    def prova (self):
        self.chess_grid = [ None ] * 64
        self.chess_grid[utils.get_index(5,8)] = King(5,8,1,'b')
        self.chess_grid[utils.get_index(4,1)] = Queen(4,1,2,'w')
        self.chess_grid[utils.get_index(4,6)] = Pawn(4,6,3,'w')
        self.chess_grid[utils.get_index(4,7)] = Bishop(4,7,4,'w')
        self.chess_grid[utils.get_index(6,8)] = Bishop(6,8,5,'b')
        self.chess_grid[utils.get_index(1,1)] = King(1,1,5,'w')
        self.kingw = self.get_piece(1,1)
        self.kingb = self.get_piece(5,8)
        self.ai = Ai(self)
        self.turn = 'w'

    def prova4 (self):
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
        self.ai = Ai(self)
        self.turn = 'w'