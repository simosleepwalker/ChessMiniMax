#include "Piece.h"
using namespace std;

class Pawn : public Piece {
public:
    Pawn (int r, int c, int i, char x);
    bool can_move (int r, int c, Piece* p);
    string type();
};

class Knight : public Piece {
public:
    Knight (int r, int c, int i, char x);
    bool can_move (int r, int c);
    string type();
};

class Bishop : public Piece {
public:
    Bishop (int r, int c, int i, char x);
    bool can_move (int r, int c);
    string type();
};

class Rook : public Piece {
public:
    Rook (int r, int c, int i, char x);
    bool can_move (int r, int c);
    string type();
};

class Queen : public Piece {
public:
    Queen (int r, int c, int i, char x);
    bool can_move (int r, int c);
    string type();
};

class King : public Piece {
public:
    King (int r, int c, int i, char x);
    bool can_move (int r, int c);
    bool can_eat (int r, int c);
    string type();
};