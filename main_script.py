import HumanPlayer as hp
import MinimaxPlayer as mm
import GameRunner as gr
import Board as b

def main():
    board = b.Board()
    playerA = hp.HumanPlayer('X')
    #playerB = hp.HumanPlayer('O')
    playerB = mm.MinimaxPlayer('O', 'X')
    game_runner = gr.GameRunner(playerA, playerB, board)
    game_runner.run()
    return


if __name__ == '__main__':
    main()
