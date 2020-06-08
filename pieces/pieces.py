import copy

#pieces classes
class Piece:
        
    def move (self,nrow,ncol):
        self.row = nrow
        self.col = ncol

    def get_col_letter (self):
        letters[8] = ['A','B','C','D','E','F','G','H']
        return letters[self.col];

    def get_col (self):
        return self.col
    
    def get_row (self):
        return self.row
    
    def get_color (self):
        return self.color

    def get_image_path (self):
        return self.image

    def get_val (self):
        return self.val

    #method to get moves for pieces which moves on a path
    def get_moves_path (self,row_func,col_func,board):
        moves = []
        for i in range(1,9):
            if (self.can_move(row_func(self.row,i),col_func(self.col,i))):
                if (board.get_piece(row_func(self.row,i),col_func(self.col,i)) == None):
                    moves.append((row_func(self.row,i),col_func(self.col,i)))
                elif (board.get_piece(row_func(self.row,i),col_func(self.col,i)) != None and board.get_piece(row_func(self.row,i),col_func(self.col,i)).get_color() != self.get_color()):
                    moves.append((row_func(self.row,i),col_func(self.col,i)))
                    break
                else:
                    break
            else:
                break
        return moves

    def __init__ (self,row,col,id,val,color):
        self.row = row
        self.col = col
        self.id = id
        self.val = val
        self.color = color
    
class Pawn (Piece):
    
    def type (self): 
        return 'pawn'

    def short_type (self):
        return 'p'

    def can_move (self,nrow,ncol,board):
        if (nrow <= 8 and ncol <= 8 and nrow >= 1 and ncol >= 1):
            if ((self.get_color() == 'w' and
                ((self.get_row() == 2 and nrow - self.get_row() == 2 and nrow - self.get_row() > 0 and ncol == self.get_col() and board.get_piece(nrow,ncol) == None and board.get_piece(nrow-1,ncol) == None) or (self.get_row() == 2 and nrow - self.get_row() == 1 and nrow - self.get_row() > 0 and ncol == self.get_col() and board.get_piece(nrow,ncol) == None) or (self.get_row() != 2 and nrow - self.get_row() == 1 and ncol == self.get_col() and board.get_piece(nrow,ncol) == None) or (nrow - self.get_row() == 1 and abs(ncol - self.get_col()) == 1 and board.get_piece(nrow,ncol) != None and board.get_piece(nrow,ncol).get_color() != 'w' ) ) ) 
                or (self.get_color() == 'b' and 
                ((self.get_row() == 7 and nrow - self.get_row() == -2 and nrow - self.get_row() < 0 and ncol == self.get_col() and board.get_piece(nrow,ncol) == None and board.get_piece(nrow+1,ncol) == None) or (self.get_row() == 7 and nrow - self.get_row() == -1 and nrow - self.get_row() < 0 and ncol == self.get_col() and board.get_piece(nrow,ncol) == None) or (self.get_row() != 7 and nrow - self.get_row() == -1 and ncol == self.get_col() and board.get_piece(nrow,ncol) == None) or (nrow - self.get_row() == -1 and abs(ncol - self.get_col()) == 1 and board.get_piece(nrow,ncol) != None and board.get_piece(nrow,ncol).get_color() != 'b' ) ) ) ):
                return True
        return False

    def get_moves (self,board,king = None):
        temp_moves = []
        moves = []
        if (self.color == 'w'):
            if (self.can_move(self.get_row()+1,self.get_col(),board)):
                temp_moves.append((self.get_row()+1,self.get_col()))
            if (self.can_move(self.get_row()+2,self.get_col(),board)):
                temp_moves.append((self.get_row()+2,self.get_col()))
            if (self.can_move(self.get_row()+1,self.get_col()+1,board)):
                temp_moves.append((self.get_row()+1,self.get_col()+1))
            if (self.can_move(self.get_row()+1,self.get_col()-1,board)):
                temp_moves.append((self.get_row()+1,self.get_col()-1))
        else:
            if (self.can_move(self.get_row()-1,self.get_col(),board)):
                temp_moves.append((self.get_row()-1,self.get_col()))
            if (self.can_move(self.get_row()-2,self.get_col(),board)):
                temp_moves.append((self.get_row()-2,self.get_col()))
            if (self.can_move(self.get_row()-1,self.get_col()+1,board)):
                temp_moves.append((self.get_row()-1,self.get_col()+1))
            if (self.can_move(self.get_row()-1,self.get_col()-1,board)):
                temp_moves.append((self.get_row()-1,self.get_col()-1))
        #if king is passed as argument, always check that the move doesn't put the king in check
        if king != None:
            for move in temp_moves:
                temp_board = copy.deepcopy(board)
                temp_board.move(self.get_row(),self.get_col(),move[0],move[1])
                if (not(king.is_in_check(temp_board))):
                    moves.append(move)
            return moves
        return temp_moves

    def get_eating_moves (self,board,king = None):
        #with pawn the eating moves are different than normal moves
        if (self.get_color == 'w'): 
            moves = []
            move_1 = (self.get_row()+1,self.get_col()+1)
            move_2 = (self.get_row()+1,self.get_col()-1)
            if (move_1[0] <= 8 and move_1[1] <= 8 and move_1[0] >= 0 and move_1[1] >= 0):
                moves.append(move_1)
            if (move_2[0] <= 8 and move_2[1] <= 8 and move_2[0] >= 0 and move_2[1] >= 0):
                moves.append(move_2)
        else:
            moves = []
            move_1 = (self.get_row()-1,self.get_col()-1)
            move_2 = (self.get_row()-1,self.get_col()+1)
            if (move_1[0] <= 8 and move_1[1] <= 8 and move_1[0] >= 0 and move_1[1] >= 0):
                moves.append(move_1)
            if (move_2[0] <= 8 and move_2[1] <= 8 and move_2[0] >= 0 and move_2[1] >= 0):
                moves.append(move_2)
        return moves

    def __init__ (self,row,col,id,color):
        super().__init__(row,col,id,1,color)
        if (self.color == 'b'):
            self.image = 'img/blackp.png'
        else:
            self.image = 'img/whitep.png'

class Knight (Piece):
    
    def type (self): 
        return 'knight'

    def short_type (self):
        return 'n'

    def can_move (self,nrow,ncol,board):
        if ((nrow <= 8 and ncol <= 8 and nrow >= 1 and ncol >= 1) and (((abs(self.get_row() - nrow) == 2 and abs(self.get_col() - ncol) == 1 and (board.get_piece(nrow,ncol) == None or board.get_piece(nrow,ncol).get_color() != self.get_color())) or (abs(self.get_col() - ncol) == 2 and abs(self.get_row() - nrow) == 1 and (board.get_piece(nrow,ncol) == None or board.get_piece(nrow,ncol).get_color() != self.get_color())))) ):
            return True
        return False

    def get_moves (self,board,king = None):
        temp_moves = []
        moves = []
        if (self.can_move(self.get_row()+2,self.get_col()+1,board)):
            temp_moves.append((self.get_row()+2,self.get_col()+1))
        if (self.can_move(self.get_row()-2,self.get_col()+1,board)):
            temp_moves.append((self.get_row()-2,self.get_col()+1))
        if (self.can_move(self.get_row()+2,self.get_col()-1,board)):
            temp_moves.append((self.get_row()+2,self.get_col()-1))
        if (self.can_move(self.get_row()-2,self.get_col()-1,board)):
            temp_moves.append((self.get_row()-2,self.get_col()-1))
        if (self.can_move(self.get_row()+1,self.get_col()+2,board)):
            temp_moves.append((self.get_row()+1,self.get_col()+2))
        if (self.can_move(self.get_row()+1,self.get_col()-2,board)):
            temp_moves.append((self.get_row()+1,self.get_col()-2))
        if (self.can_move(self.get_row()-1,self.get_col()+2,board)):
            temp_moves.append((self.get_row()-1,self.get_col()+2))
        if (self.can_move(self.get_row()-1,self.get_col()-2,board)):
            temp_moves.append((self.get_row()-1,self.get_col()-2))
        if king != None:
            for move in temp_moves:
                temp_board = copy.deepcopy(board)
                temp_board.move(self.get_row(),self.get_col(),move[0],move[1])
                if (not(king.is_in_check(temp_board))):
                    moves.append(move)
            return moves
        return temp_moves
    
    def get_eating_moves (self,board,king = None):
        return self.get_moves (board,king)

    def __init__ (self,row,col,id,color):
        super().__init__(row,col,id,3,color)
        if (self.color == 'b'):
            self.image = "img/blackn.png"
        else:
            self.image = "img/whiten.png"

class Bishop (Piece):

    def type (self): 
        return 'bishop'

    def short_type (self):
        return 'b'

    def can_move(self,nrow,ncol):
        if (nrow <= 8 and ncol <= 8 and nrow >= 1 and ncol >= 1 and abs(self.get_row() - nrow) == abs(self.get_col() - ncol)):
            return True
        return False

    def get_moves (self,board,king = None):
        temp_moves = []
        moves = []
        for x in self.get_moves_path(lambda row, i: row + i,lambda col, i: col + i,board):
            temp_moves.append(x)
        for x in self.get_moves_path(lambda row, i: row + i,lambda col, i: col - i,board):
            temp_moves.append(x)
        for x in self.get_moves_path(lambda row, i: row - i,lambda col, i: col + i,board):
            temp_moves.append(x)
        for x in self.get_moves_path(lambda row, i: row - i,lambda col, i: col - i,board):
            temp_moves.append(x)
        if king != None:
            for move in temp_moves:
                temp_board = copy.deepcopy(board)
                temp_board.move(self.get_row(),self.get_col(),move[0],move[1])
                if (not(king.is_in_check(temp_board))):
                    moves.append(move)
            return moves
        return temp_moves

    def get_eating_moves (self,board,king = None):
        return self.get_moves (board,king)

    def __init__ (self,row,col,id,color):
        super().__init__(row,col,id,3,color)
        if (self.color == 'b'):
            self.image = "img/blackb.png"
        else:
            self.image = "img/whiteb.png"

class Rook (Piece):

    def type (self): 
        return 'rook'
    
    def short_type (self):
        return 'r'

    def can_move(self,nrow,ncol):
        if ((nrow <= 8 and ncol <= 8 and nrow >= 1 and ncol >= 1) and ((self.get_col() == ncol) or (self.get_row() == nrow))):
            return True
        return False

    def get_moves (self,board,king = None):
        temp_moves = []
        moves = []
        for x in self.get_moves_path(lambda row, i: row + i,lambda col, i: col,board):
            temp_moves.append(x)
        for x in self.get_moves_path(lambda row, i: row,lambda col, i: col + i,board):
            temp_moves.append(x)
        for x in self.get_moves_path(lambda row, i: row - i,lambda col, i: col,board):
            temp_moves.append(x)
        for x in self.get_moves_path(lambda row, i: row,lambda col, i: col - i,board):
            temp_moves.append(x)
        if king != None:
            for move in temp_moves:
                temp_board = copy.deepcopy(board)
                temp_board.move(self.get_row(),self.get_col(),move[0],move[1])
                if (not(king.is_in_check(temp_board))):
                    moves.append(move)
            return moves
        return temp_moves
    
    def get_eating_moves (self,board,king = None):
        return self.get_moves (board,king)

    def __init__ (self,row,col,id,color):
        super().__init__(row,col,id,5,color)
        if (self.color == 'b'):
            self.image = "img/blackr.png"
        else:
            self.image = "img/whiter.png"

class Queen (Piece):
    
    def type (self): 
        return 'queen'

    def short_type (self):
        return 'q'

    def can_move(self,nrow,ncol): 
        if ((nrow <= 8 and ncol <= 8 and nrow >= 1 and ncol >= 1) and ((self.get_col() == ncol) or (self.get_row() == nrow) or (abs(self.get_row() - nrow) == abs(self.get_col() - ncol)))):
            return True
        return False

    def get_moves (self,board,king = None):
        temp_moves = []
        moves = []
        for x in self.get_moves_path(lambda row, i: row + i,lambda col, i: col,board):
            temp_moves.append(x)
        for x in self.get_moves_path(lambda row, i: row,lambda col, i: col + i,board):
            temp_moves.append(x)
        for x in self.get_moves_path(lambda row, i: row - i,lambda col, i: col,board):
            temp_moves.append(x)
        for x in self.get_moves_path(lambda row, i: row,lambda col, i: col - i,board):
            temp_moves.append(x)
        for x in self.get_moves_path(lambda row, i: row + i,lambda col, i: col + i,board):
            temp_moves.append(x)
        for x in self.get_moves_path(lambda row, i: row + i,lambda col, i: col - i,board):
            temp_moves.append(x)
        for x in self.get_moves_path(lambda row, i: row - i,lambda col, i: col + i,board):
            temp_moves.append(x)
        for x in self.get_moves_path(lambda row, i: row - i,lambda col, i: col - i,board):
            temp_moves.append(x)
        if king != None:
            for move in temp_moves:
                temp_board = copy.deepcopy(board)
                temp_board.move(self.get_row(),self.get_col(),move[0],move[1])
                if (not(king.is_in_check(temp_board))):
                    moves.append(move)
            return moves
        return temp_moves
    
    def get_eating_moves (self,board,king = None):
        return self.get_moves (board,king)

    def __init__ (self,row,col,id,color):
        super().__init__(row,col,id,9,color)
        if (self.color == 'b'):
            self.image = "img/blackq.png"
        else:
            self.image = "img/whiteq.png"

class King (Piece):

    def set_check_image (self):
        if (self.color == 'b'):
            self.image = "img/blackk_check.png"
        else:
            self.image = "img/whitek_check.png"
    
    def type (self): 
        return 'king'

    def short_type (self):
        return 'k'

    def can_move (self,nrow,ncol,board,verify_check = True):
        if ((nrow <= 8 and ncol <= 8 and nrow >= 1 and ncol >= 1) and (abs(self.get_row() - nrow) <= 1 and abs(self.get_col() - ncol) <= 1) and (board.get_piece(nrow,ncol) == None or board.get_piece(nrow,ncol).get_color() != self.get_color()) and (not(verify_check) or not(self.is_in_check(board,nrow,ncol)))):
            return True
        return False

    def get_moves (self,board,verify_check = True,king = None):
        moves = []
        if (self.can_move(self.get_row()-1,self.get_col(),board,verify_check=verify_check)):
            moves.append((self.get_row()-1,self.get_col()))
        if (self.can_move(self.get_row()+1,self.get_col(),board,verify_check=verify_check)):
            moves.append((self.get_row()+1,self.get_col()))
        if (self.can_move(self.get_row(),self.get_col()+1,board,verify_check=verify_check)):
            moves.append((self.get_row(),self.get_col()+1))
        if (self.can_move(self.get_row(),self.get_col()-1,board,verify_check=verify_check)):
            moves.append((self.get_row(),self.get_col()-1))
        if (self.can_move(self.get_row()+1,self.get_col()+1,board,verify_check=verify_check)):
            moves.append((self.get_row()+1,self.get_col()+1))
        if (self.can_move(self.get_row()+1,self.get_col()-1,board,verify_check=verify_check)):
            moves.append((self.get_row()+1,self.get_col()-1))
        if (self.can_move(self.get_row()-1,self.get_col()+1,board,verify_check=verify_check)):
            moves.append((self.get_row()-1,self.get_col()+1))
        if (self.can_move(self.get_row()-1,self.get_col()-1,board,verify_check=verify_check)):
            moves.append((self.get_row()-1,self.get_col()-1))
        return moves

    def is_in_check (self,board,row=None,col=None):
        if (row == None and col == None):
            row = self.get_row()
            col = self.get_col()
            temp_board = board
        else:
            temp_board = copy.deepcopy(board)
            temp_board.move(self.get_row(),self.get_col(),row,col)
        for piece in temp_board.get_grid():
            if (piece != None and piece.get_color() != self.get_color()):
                if (piece.short_type() == 'k'):
                    for move in piece.get_moves(temp_board,verify_check=False):
                        if (move[0] == row and move[1] == col):
                            return True
                else:
                    for move in piece.get_eating_moves(temp_board):
                        if (move[0] == row and move[1] == col):
                            return True
        return False

    def is_in_check_mate (self,board):
        if (self.is_in_check(board)):
            for piece in board.get_grid():
                if (piece != None and piece.get_color() == self.get_color()):
                    if (piece.short_type() == 'k'):
                        for move in piece.get_moves(board):
                            if (not(self.is_in_check(board,move[0],move[1]))):
                                return False
                    else:
                        for move in piece.get_moves(board):
                            temp_board = copy.deepcopy(board)
                            temp_board.move(piece.get_row(),piece.get_col(),move[0],move[1])
                            if (not(self.is_in_check(temp_board))):
                                return False
            return True
        return False

    def __init__ (self,row,col,id,color):
        super().__init__(row,col,id,-50,color)
        if (self.color == 'b'):
            self.image = "img/blackk.png"
        else:
            self.image = "img/whitek.png"