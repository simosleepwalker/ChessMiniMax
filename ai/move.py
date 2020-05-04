class Move:

    def __init__ (self,from_row,from_col,to_row,to_col,val):
        self.move_from = (from_row,from_col)
        self.move_to = (to_row,to_col)
        self.val = val