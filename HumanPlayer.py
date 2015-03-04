
class HumanPlayer(object):
    def __init__(self, marker):
        self._marker = marker
        self.possible_squares = range(9)
        return

    def marker(self):
        return self._marker

    def make_move(self, board):
        board.print_board_custom(self.possible_squares)
        move = 10
        while True:
            chosen_str = raw_input("player %s enter square by coordinates (ie. 1):"%self.marker())
            chosen_square = int(chosen_str)
            if board.mark_square(chosen_square, self.marker()) :
                break
            else:
                print 'invalid move, try again'
        return

