import os
import copy

class Board(object):
    def __init__(self):
        self.winner = None
        self.empty_str = ' '
        self.board_vec = [self.empty_str]*9
        self.winning_patterns = [(0, 1, 2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,5,6)]
        self.board_string_patt = '\n| %s | %s | %s |\n| %s | %s | %s |\n| %s | %s | %s |\n'
        self.possible_squares = range(9)
        return

    def check_winner(self):
        def pattern_is_a_winner(patt):
            return (self.board_vec[patt[0]] != self.empty_str) and (self.board_vec[patt[0]] == self.board_vec[patt[1]]) and (self.board_vec[patt[0]] == self.board_vec[patt[2]]) 
        any(()) 
        for patt in self.winning_patterns:
            if pattern_is_a_winner(patt):
                self.winner = {'marker': self.board_vec[patt[0]], 'pattern': patt}
                return True
        return False

    def mark_square(self, square_ind, marker):
        """
        returns True if successful, False otherwise
        """
        if (0 <= square_ind <= 8) and (self.board_vec[square_ind] == self.empty_str):
            self.board_vec[square_ind] = marker
            return True
        else:
            return False


    def check_full(self):
        return not (self.empty_str in self.board_vec)
    

    def print_board(self):
        #os.system("clear")
        print self.board_string_patt%tuple(self.board_vec)
        return

    def print_board_custom(self, vec):
        print self.board_string_patt%tuple(vec)

    def remaining_squares(self):
        return [i for i in self.possible_squares if self.board_vec[i] == self.empty_str]

    def copy(self):
        board_copy = copy.copy(self)
        board_copy.board_vec = list(self.board_vec)
        board_copy.winner = None
        return board_copy
