from ai.ai import Ai
from board.chess import Chess

chess = Chess()
ai = Ai(chess)
move = ai.choose_move()
print(move.move_from[0],move.move_from[1],move.move_to[0],move.move_to[1])