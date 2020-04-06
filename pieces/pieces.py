class Piece:

    def __init__ (self,row,col,id,val,color):
        self.row = row
        self.col = col
        self.id = id
        self.val = val
        self.color = color
        
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
    
class Pawn (Piece):
    
    def __init__ (self,row,col,id,color):
        super().__init__(row,col,id,0,color)
        if (self.color == 'b'):
            self.image = 'img/blackp.png'
        else:
            self.image = 'img/whitep.png'
    
    def type (self): 
        return 'pawn'

    def short_type (self):
        return 'p'

    def can_move (self,nrow,ncol,board):
        if (nrow <= 8 and ncol <= 8 and nrow >= 1 and ncol >= 1):
            if ((self.get_color() == 'w' and
                ((self.get_row() == 2 and nrow - self.get_row() <= 2 and nrow - self.get_row() > 0 and ncol == self.get_col() and board.get_piece(nrow,ncol) == None) or (self.get_row() != 2 and nrow - self.get_row() == 1 and ncol == self.get_col() and board.get_piece(nrow,ncol) == None) or (nrow - self.get_row() == 1 and abs(ncol - self.get_col()) == 1 and board.get_piece(nrow,ncol) != None and board.get_piece(nrow,ncol).get_color() != 'w' ) ) ) 
                or (self.get_color() == 'b' and 
                ((self.get_row() == 7 and nrow - self.get_row() >= -2 and nrow - self.get_row() < 0 and ncol == self.get_col() and board.get_piece(nrow,ncol) == None) or (self.get_row() != 7 and nrow - self.get_row() == -1 and ncol == self.get_col() and board.get_piece(nrow,ncol) == None) or (nrow - self.get_row() == -1 and abs(ncol - self.get_col()) == 1 and board.get_piece(nrow,ncol) != None and board.get_piece(nrow,ncol).get_color() != 'b' ) ) ) ):
                return True
        return False

    def get_moves (self,board):
        moves = []
        if (self.color == 'w'):
            if (self.can_move(self.get_row()+1,self.get_col(),board)):
                moves.append((self.get_row()+1,self.get_col()))
            if (self.can_move(self.get_row()+2,self.get_col(),board)):
                moves.append((self.get_row()+2,self.get_col()))
            if (self.can_move(self.get_row()+1,self.get_col()+1,board)):
                moves.append((self.get_row()+1,self.get_col()+1))
            if (self.can_move(self.get_row()+1,self.get_col()-1,board)):
                moves.append((self.get_row()+1,self.get_col()-1))
        else:
            if (self.can_move(self.get_row()-1,self.get_col(),board)):
                moves.append((self.get_row()-1,self.get_col()))
            if (self.can_move(self.get_row()-2,self.get_col(),board)):
                moves.append((self.get_row()-2,self.get_col()))
            if (self.can_move(self.get_row()-1,self.get_col()+1,board)):
                moves.append((self.get_row()-1,self.get_col()+1))
            if (self.can_move(self.get_row()-1,self.get_col()-1,board)):
                moves.append((self.get_row()-1,self.get_col()-1))
        print(moves)
        return moves

class Knight (Piece):
    
    def __init__ (self,row,col,id,color):
        super().__init__(row,col,id,0,color)
        if (self.color == 'b'):
            self.image = "img/blackn.png"
        else:
            self.image = "img/whiten.png"
    
    def type (self): 
        return 'knight'

    def short_type (self):
        return 'n'

    def can_move (self,nrow,ncol,board):
        if ((nrow <= 8 and ncol <= 8 and nrow >= 1 and ncol >= 1) and (((abs(self.get_row() - nrow) == 2) and (abs(self.get_col() - ncol) == 1)) or ((abs(self.get_col() - ncol) == 2) and (abs(self.get_row() - nrow) == 1)))):
            return True
        return False

class Bishop (Piece):
    
    def __init__ (self,row,col,id,color):
        super().__init__(row,col,id,0,color)
        if (self.color == 'b'):
            self.image = "img/blackb.png"
        else:
            self.image = "img/whiteb.png"

    def type (self): 
        return 'bishop'

    def short_type (self):
        return 'b'

    def can_move(self,nrow,ncol,board):
        if ((nrow <= 8 and ncol <= 8 and nrow >= 1 and ncol >= 1) and (abs(self.get_row() - nrow) == abs(self.get_col() - ncol))):
            return True
        return False

class Rook (Piece):
    
    def __init__ (self,row,col,id,color):
        super().__init__(row,col,id,0,color)
        if (self.color == 'b'):
            self.image = "img/blackr.png"
        else:
            self.image = "img/whiter.png"

    def type (self): 
        return 'rook'
    
    def short_type (self):
        return 'r'

    def can_move(self,nrow,ncol,board):
        if ((nrow <= 8 and ncol <= 8 and nrow >= 1 and ncol >= 1) and ((self.get_col() == ncol) or (self.get_row() == nrow))):
            return True
        return False

class Queen (Piece):
    
    def __init__ (self,row,col,id,color):
        super().__init__(row,col,id,0,color)
        if (self.color == 'b'):
            self.image = "img/blackq.png"
        else:
            self.image = "img/whiteq.png"
    
    def type (self): 
        return 'queen'

    def short_type (self):
        return 'q'

    def can_move(self,nrow,ncol,board): 
        if ((nrow <= 8 and ncol <= 8 and nrow >= 1 and ncol >= 1) and ((self.get_col() == ncol) or (self.get_row() == nrow) or (abs(self.get_row() - nrow) == abs(self.get_col() - ncol)))):
            return True
        return False

class King (Piece):
    
    def __init__ (self,row,col,id,color):
        super().__init__(row,col,id,0,color)
        if (self.color == 'b'):
            self.image = "img/blackk.png"
        else:
            self.image = "img/whitek.png"

    def type (self): 
        return 'king'

    def short_type (self):
        return 'k'

    def can_move (self,nrow,ncol,board):
        if ((nrow <= 8 and ncol <= 8 and nrow >= 1 and ncol >= 1) and ((abs(self.get_row() - nrow) <= 1) and (abs(self.get_col() - ncol) <= 1))): #TODO: AND NOT IN CHECK
            return True
        return False