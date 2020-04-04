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
        return col
    
    def get_row (self):
        return row
    
    def get_color (self):
        return color