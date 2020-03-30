#include "Pieces.h"
#include <iostream>

Pawn::Pawn (int r, int c, int i, char x) : Piece (r, c, i, 0, x) { }
bool Pawn::can_move (int r, int c, Piece** p) {
    Piece* piece_to_eat = p[(r-1)*8+(c-1)];
    if ((r <= 8 && c <= 8 && r >= 1 && c >= 1) && 
        ((get_color() == 'W' && ((get_row() == 2 && (r - get_row() <= 2 && r - get_row() > 0)) || ( get_row() != 2 && r - get_row() == 1 ) || ( r - get_row() == 1 && abs(c - get_col()) == 1 && piece_to_eat != nullptr ) ) ) || 
         (get_color() == 'B' && ((get_row() == 7 && (r - get_row() >= -2 && r - get_row() < 0)) || ( get_row() != 2 && r - get_row() == -1) || ( r - get_row() == -1 && abs(c - get_col()) == 1 && piece_to_eat != nullptr ) ) ) ) ) { return true; }
    return false;
}
string Pawn::type() { return "Pawn"; }

Knight::Knight (int r, int c, int i, char x) : Piece (r, c, i, 0, x) { }
bool Knight::can_move (int r, int c) {
    if ((r <= 8 && c <= 8 && r >= 1 && c >= 1) && (((abs(get_row() - r) == 2) && (abs(get_col() - c) == 1)) || ((abs(get_col() - c) == 2) && (abs(get_row() - r) == 1))))
        return true;
    return false;
}
string Knight::type() { return "Knight"; }

Bishop::Bishop (int r, int c, int i, char x) : Piece (r, c, i, 0, x) { }
bool Bishop::can_move (int r, int c) {
    if ((r <= 8 && c <= 8 && r >= 1 && c >= 1) && (abs(get_row() - r) == abs(get_col() - c)))
        return true;
    return false;
}
string Bishop::type() { return "Bishop"; }


Rook::Rook (int r, int c, int i, char x) : Piece (r, c, i, 0, x) { }
bool Rook::can_move (int r, int c) { 
    if ((r <= 8 && c <= 8 && r >= 1 && c >= 1) && ((get_col() == c) || (get_row() == r)))
        return true;
    return false;
}
string Rook::type() { return "Rook"; }

Queen::Queen (int r, int c, int i, char x) : Piece (r, c, i, 0, x) { }
bool Queen::can_move (int r, int c) { 
    if ((r <= 8 && c <= 8 && r >= 1 && c >= 1) && ((get_col() == c) || (get_row() == r) || (abs(get_row() - r) == abs(get_col() - c))))
        return true;
    return false;
}
string Queen::type() { return "Queen"; }

King::King (int r, int c, int i, char x) : Piece (r, c, i, 0, x) { }
bool King::can_move (int r, int c) {
    if ((r <= 8 && c <= 8 && r >= 1 && c >= 1) && ((abs(get_row() - r) <= 1) && (abs(get_col() - c) <= 1))) //TODO: AND NOT IN CHECK
        return true;
    return false;
}
string King::type() { return "King"; }