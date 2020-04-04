import Piece

class Pawn (Piece):
    
    def __init__ (self,row,col,id,color):
        super().__init__(row,col,id,0,color)
        if (self.color == 'b'):
            self.image = 'img/bp.png'
        else:
            self.image = 'img/wp.png'
    
    def type (self): 
        return 'pawn'

    def short_type (self):
        return 'p'

    def can_move (self,nrow,ncol,board):
        if ((nrow <= 8 and ncol <= 8 and nrow >= 1 and ncol >= 1) and
            ((self.get_color() == 'w' and ((self.get_row() == 2 and (nrow - self.get_row() <= 2 and nrow - self.get_row() > 0)) or (self.get_row() != 2 and nrow - self.get_row() == 1 ) or (nrow - self.get_row() == 1 and abs(ncol - self.get_col()) == 1 and piece_to_eat != None and self.get_color() != 'b' ) ) ) or
             (self.get_color() == 'b' and ((self.get_row() == 7 and (nrow - self.get_row() >= -2 and nrow - self.get_row() < 0)) or (self.get_row() != 2 and nrow - self.get_row() == -1) or (nrow - self.get_row() == -1 and abs(ncol - self.get_col()) == 1 and piece_to_eat != None and self.get_color() != 'b' ) ) ) ) ):
            return true
        return false

class Knight (Piece):
    
    def __init__ (self,row,col,id,color):
        super().__init__(row,col,id,0,color)
        if (self.color == 'b'):
            self.image = "img/bn.png"
        else:
            self.image = "img/wn.png"
    
    def type (self): 
        return 'knight'

    def short_type (self):
        return 'n'

    def can_move (self,nrow,ncol,board):
        if ((nrow <= 8 and ncol <= 8 and nrow >= 1 and ncol >= 1) and (((abs(self.get_row() - nrow) == 2) and (abs(self.get_col() - ncol) == 1)) or ((abs(self.get_col() - ncol) == 2) and (abs(self.get_row() - nrow) == 1)))):
            return true
        return false

class Bishop (Piece):
    
    def __init__ (self,row,col,id,color):
        super().__init__(row,col,id,0,color)
        if (self.color == 'b'):
            self.image = "img/bb.png"
        else:
            self.image = "img/wb.png"

    def type (self): 
        return 'bishop'

    def short_type (self):
        return 'b'

    def can_move(self,nrow,ncol,board):
        if ((nrow <= 8 and ncol <= 8 and nrow >= 1 and ncol >= 1) and (abs(self.get_row() - nrow) == abs(self.get_col() - ncol))):
            return true
        return false

class Rook (Piece):
    
    def __init__ (self,row,col,id,color):
        super().__init__(row,col,id,0,color)
        if (self.color == 'b'):
            self.image = "img/br.png"
        else:
            self.image = "img/wr.png"

    def type (self): 
        return 'rook'
    
    def short_type (self):
        return 'r'

    def can_move(self,nrow,ncol,board):
        if ((nrow <= 8 and ncol <= 8 and nrow >= 1 and ncol >= 1) and ((self.get_col() == ncol) or (self.get_row() == nrow))):
            return true
        return false

class Queen (Piece):
    
    def __init__ (self,row,col,id,color):
        super().__init__(row,col,id,0,color)
        if (self.color == 'b'):
            self.image = "img/bq.png"
        else:
            self.image = "img/wq.png"
    
    def type (self): 
        return 'queen'

    def short_type (self):
        return 'q'

    def can_move(self,nrow,ncol,board): 
        if ((nrow <= 8 and ncol <= 8 and nrow >= 1 and ncol >= 1) and ((self.get_col() == ncol) or (self.get_row() == nrow) or (abs(self.get_row() - nrow) == abs(self.get_col() - ncol)))):
            return true
        return false

class King (Piece):
    
    def __init__ (self,row,col,id,color):
        super().__init__(row,col,id,0,color)
        if (self.color == 'b'):
            self.image = "img/bk.png"
        else:
            self.image = "img/wk.png"

    def type (self): 
        return 'king'

    def short_type (self):
        return 'k'

    def can_move (self,nrow,ncol,board):
        if ((nrow <= 8 and ncol <= 8 and nrow >= 1 and ncol >= 1) and ((abs(self.get_row() - nrow) <= 1) and (abs(self.get_col() - ncol) <= 1))): #TODO: AND NOT IN CHECK
            return true
        return false