#include <string>
using namespace std;

class Piece {
private:
    int row, col, id, val;
    char color;
public:
    Piece (int r, int c, int i, int v, char x);
    char get_col_let ();
    int get_col ();
    int get_row ();
    char get_color ();
    virtual string type ();
    virtual bool can_move (int r, int c);
    virtual bool can_move (int r, int c, Piece** p);  
};