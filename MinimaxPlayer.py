import copy

class MinimaxPlayer(object):
    def __init__(self, marker, opp_marker):
        self._marker = marker
        self._opponent_marker = opp_marker
        
    def marker(self):
        return self._marker

    def make_move(self, board):
        best_move = None
        best_val = -2
        for squarei in board.remaining_squares():
            val = self.eval_minimax(board.copy(), squarei, self.marker())
            print 'square %i: val: %i'%(squarei, val)
            if val > best_val:
                best_move = squarei
                best_val = val
        
        if not board.mark_square(best_move, self.marker()):
            raise RuntimeError("")
        return

    def eval_minimax(self, board, squarei, cur_player_marker):
        board.mark_square(squarei, cur_player_marker)
        if board.check_winner():
            return 1
        elif board.check_full():
            return 0
        else:
            if cur_player_marker == self.marker():
                next_player_marker = self._opponent_marker
            else:
                next_player_marker = self.marker() 
            return -max(self.eval_minimax(board.copy(), xi, next_player_marker) for xi in board.remaining_squares())

