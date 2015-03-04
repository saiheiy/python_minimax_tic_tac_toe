
class GameRunner(object):
    def __init__(self, playerA, playerB, board):
        self.playerA = playerA
        self.playerB = playerB
        if self.playerA.marker() == self.playerB.marker():
            raise RuntimeError("player A and B's markers have to be different.  Change it in constructor instatiation")
        self.board = board
        return

    def run(self):
        win_flag = False
        draw_flag = False
        playerA_turn = True
        while not (win_flag or draw_flag):
            self.board.print_board()
            if playerA_turn:
                playerA_turn = False
                move = self.playerA.make_move(self.board)
            else:
                playerA_turn = True
                move = self.playerB.make_move(self.board)
        
            if self.board.check_winner():
                win_flag = True
            elif self.board.check_full():
                draw_flag = True


        if win_flag:
            print 'player %s wins'%self.board.winner['marker']
        
        elif draw_flag:
            print 'game ends in draw'

        return


