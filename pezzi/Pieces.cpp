#include "Piece.cpp"

class Pawn : public Piece {
    public:
        Pawn (int r, int c, int i) : Piece (r, c, i, 0) { }
        bool can_move(int r, int c) {
            //TODO
            return true;
        }
};

class Knight : public Piece {
    public:
        Knight (int r, int c, int i) : Piece (r, c, i, 0) { }
        bool can_move(int r, int c) {
            //TODO
            return true;
        }
};

class Bishop : public Piece {
    public:
        Bishop (int r, int c, int i) : Piece (r, c, i, 0) { }
        bool can_move(int r, int c) {
            //TODO
            return true;
        }
};

class Rook : public Piece {
    public:
        Rook (int r, int c, int i) : Piece (r, c, i, 0) { }
        bool can_move(int r, int c) { 
            //TODO
            return true; 
        }
};

class Queen : public Piece {
    public:
        Queen (int r, int c, int i) : Piece (r, c, i, 0) { }
        bool can_move(int r, int c) { 
            //TODO
            return true; 
        }
};

class King : public Piece {
    public:
        King (int r, int c, int i) : Piece (r, c, i, 0) { }
        bool can_move(int r, int c) {
            //TODO
            return true;
        }
};