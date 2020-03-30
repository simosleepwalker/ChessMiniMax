#include "Chess.h"
#include <iostream>

Chess::Chess () {
    turn = 'P';
    chess_grid = new Piece*[64];
    chess_grid[1*8+0] = new Pawn(2,1,0,'W');
    chess_grid[2*8+1] = new Pawn(3,2,1,'B');
    bool so = chess_grid[8]->can_move(3,2,chess_grid);
}
Piece** Chess::get_grid () { return chess_grid; }
Piece* Chess::get_piece (int index) { return (Piece*)(&chess_grid[index]); }