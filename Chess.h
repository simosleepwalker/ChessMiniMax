#include "pieces/Pieces.h"

class Chess {
private:
    char turn;
    Piece** chess_grid;
public:
    Chess ();
    int get_index;
    Piece** get_grid ();
    Piece* get_piece (int index);
};