#include "Piece.h"
#include <iostream>

Piece::Piece (int r, int c, int i, int v, char x) {
    row = r;
    col = c;
    id = i;
    val = v;
    color = x;
}
char Piece::get_col_let () {
    char letters[8] = {'A','B','C','D','E','F','G','H'};
    return letters[col];
}
int Piece::get_col () { return col + 1; }
int Piece::get_row () { return row + 1; }
char Piece::get_color () { return color; }
string Piece::type () { return "None"; };
bool Piece::can_move (int r, int c) { return false; };
bool Piece::can_move (int r, int c, Piece* p) { return false; };