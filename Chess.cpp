#include "Chess.h"
#include <iostream>

Chess::Chess () {
    turn = 'P';
    chess_grid = new Piece*[64];
    chess_grid[0] = new Pawn(0,0,0,'B');
    bool can_move = chess_grid[0]->can_move(0,0);
    std::cout << can_move;
}
Piece** Chess::get_grid () { return chess_grid; }
Piece* Chess::get_piece (int index) { return (Piece*)(&chess_grid[index]); }