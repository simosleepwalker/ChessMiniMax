import tkinter as tk
import os
from . import utils,chess
from PIL import ImageTk, Image

COLOR1 = "brown"
COLOR2 = "white"
COLOR3 = "blue"

class Cell (tk.Frame):
    
    def set_chess (self, chess):
        self.chess = chess

    def set_board (self, board):
        self.board = board

    def set_row (self, row):
        self.row = row

    def set_col (self, col):
        self.col = col

    def set_piece_from (self, piece_from):
        self.piece_from = piece_from

    def set_piece (self, piece):
        self.piece = piece

    def get_piece (self):
        return self.piece

    def get_moves_callback (self, event):
        if (self.chess.get_turn() == self.get_piece().get_color()):
            moves = self.get_piece().get_moves(self.chess,self.chess.get_king(self.chess.get_turn()))
            self.board.highlit_moves(moves,self.get_piece())

    def set_moves_callback (self, event):
        self.chess.move(self.piece_from.get_row(),self.piece_from.get_col(),self.row,self.col)
        self.piece_from = None
        self.board.draw_pieces()
        self.ai_turn()

    def ai_turn (self):
        self.chess.change_turn()
        self.board.draw_pieces()        

    def __init__ (self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.piece = None

class Board (tk.Frame):

    def build_grid (self):
        root = tk.Tk()
        root.title('Chess')
        root.geometry('{}x{}'.format(700, 700))

        top_frame = tk.Frame(root, bg='cyan', width=700, height=700)

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        top_frame.grid(row=0, sticky="ew")
        top_frame.grid_rowconfigure(8, weight=1)
        top_frame.grid_columnconfigure(8, weight=1)

        self.cells = []

        for i in range(1,9):
            for j in range(1,9):
                if (i % 2 == 0 and j % 2 == 0):
                    cell = Cell(top_frame, bg=COLOR1, width=80, height=80)
                    cell.color = COLOR1
                elif (i % 2 == 0 and j % 2 != 0):
                    cell = Cell(top_frame, bg=COLOR2, width=80, height=80)
                    cell.color = COLOR2
                elif (i % 2 != 0 and j % 2 == 0):
                    cell = Cell(top_frame, bg=COLOR2, width=80, height=80)
                    cell.color = COLOR2
                else:
                    cell = Cell(top_frame, bg=COLOR1, width=80, height=80)
                    cell.color = COLOR1
                cell.grid(row=i, column=j, sticky="ns")
                cell.set_row(i)
                cell.set_col(j)
                cell.set_piece(None)
                cell.set_piece_from(None)
                cell.set_board(self)
                cell.set_chess(self.chess)
                self.cells.append(cell)
                
        return root

    def draw_pieces (self):
        for x,piece in enumerate(self.chess.get_grid()):
            for child in self.cells[x].winfo_children():
                child.destroy()
            self.cells[x].set_chess(self.chess)
            self.cells[x]['bg'] = self.cells[x].color
            if piece != None:
                self.cells[x].set_piece(piece)
                image = Image.open(os.path.dirname(__file__)+"/../pieces/"+piece.get_image_path())
                photo = ImageTk.PhotoImage(image.resize((64, 64), Image.ANTIALIAS))
                label = tk.Label(self.cells[x], image=photo, bg=self.cells[x]['bg'], width=80, height=80)
                label.image = photo
                label.bind("<Button-1>",self.cells[x].get_moves_callback)
                label.pack()
    
    def highlit_moves (self,moves,piece):
        if len(moves) > 0:
            for cell in self.cells:
                cell.unbind("<Button-1>")
                for child in cell.winfo_children():
                    child.unbind("<Button-1>")
        for move in moves:
            self.cells[utils.get_index(move[0],move[1])]['bg'] = COLOR3
            for child in self.cells[utils.get_index(move[0],move[1])].winfo_children():
                child['bg'] = COLOR3
                child.bind("<Button-1>",self.cells[utils.get_index(move[0],move[1])].set_moves_callback)
            self.cells[utils.get_index(move[0],move[1])].set_piece_from(piece)
            self.cells[utils.get_index(move[0],move[1])].bind("<Button-1>",self.cells[utils.get_index(move[0],move[1])].set_moves_callback)

    def __init__ (self):
        self.chess = chess.Chess()
        root = self.build_grid()
        self.draw_pieces()
        root.mainloop()