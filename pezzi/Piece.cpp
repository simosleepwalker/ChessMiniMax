#include <iostream>
using namespace std;

class Piece {
    private:
        int row, col, id, val;
    public:
        Piece (int r, int c, int i, int v) {
            row = r;
            col = c;
            id = i;
            val = v;
        }
        char get_col () {
            char letters[8] = {'A','B','C','D','E','F','G','H'};
            return letters[col];
        }
        int get_row () {
            return row + 1;
        }
        virtual bool can_move (int r, int c) = 0;
};