import tkinter as tk
import os
from PIL import ImageTk, Image
from chess import Chess

COLOR1 = "brown"
COLOR2 = "white"

class Cell (tk.Frame):

    def __init__ (self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.piece = None
    
    def set_chess (self, chess):
        self.chess = chess
    
    def set_piece (self, piece):
        self.piece = piece

    def get_piece (self):
        return self.piece

    def click_callback (self, event):
        self.get_piece().get_moves(self.chess)
        
class Board:

    def build_grid (self):
        root = tk.Tk()
        root.title("Simple Python Chess")

        root.title('Chess')
        root.geometry('{}x{}'.format(700, 700))

        top_frame = tk.Frame(root, bg='cyan', width=700, height=700)

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        top_frame.grid(row=0, sticky="ew")

        top_frame.grid_rowconfigure(8, weight=1)
        top_frame.grid_columnconfigure(8, weight=1)

        self.cells = []

        for i in range(8,0,-1):
            for j in range(0,8):
                if (i % 2 == 0 and j % 2 == 0):
                    cell = Cell(top_frame, bg=COLOR1, width=80, height=80)
                elif (i % 2 == 0 and j % 2 != 0):
                    cell = Cell(top_frame, bg=COLOR2, width=80, height=80)
                elif (i % 2 != 0 and j % 2 == 0):
                    cell = Cell(top_frame, bg=COLOR2, width=80, height=80)
                else:
                    cell = Cell(top_frame, bg=COLOR1, width=80, height=80)
                cell.grid(row=i, column=j, sticky="ns")
                cell.set_piece(None)
                cell.bind("<Button-1>",cell.click_callback)
                self.cells.append(cell)
                
        return root

    def draw_pieces (self):
        for x,piece in enumerate(self.chess.get_grid()):
            self.cells[x].set_chess(self.chess)
            if piece != None:
                self.cells[x].set_piece(piece)
                image = Image.open(os.path.dirname(__file__)+"/pieces/"+piece.get_image_path())
                photo = ImageTk.PhotoImage(image.resize((64, 64), Image.ANTIALIAS))
                label = tk.Label(self.cells[x], image=photo, bg=self.cells[x]['bg'], width=80, height=80)
                label.image = photo
                label.bind("<Button-1>",self.cells[x].click_callback)
                label.pack()

    def __init__ (self):
        self.chess = Chess()
        root = self.build_grid()
        self.draw_pieces()
        root.mainloop()