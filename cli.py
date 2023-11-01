# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board


# Reminder to check all the tests

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    while winner == None:
        print("TODO: take a turn!")
        # TODO: Show the board to the user.
        def draw_board():
        board=""
        for i in range(5):
          if i%2 == 0:
                    board += "|    " * 4
          else:
                     board += " --- " * 3
          board += "\n"

        return board
    
        # TODO: Input a move from the player.
        def player_setup()
             symbol_1 = input("Player 1, do you want to be X or O? ")
            if symbol_1 == "X":
                symbol_2 = "O"
                print("Player 2, you are O. ")
            else:
                symbol_2 = "X"
        print("Player 2, you are X. ")
    input("Press enter to continue.")
    print("\n")
    return (symbol_1, symbol_2)
        # TODO: Update who's turn it is.
        def startGamming(board, symbol_1, symbol_2, count):
                if count % 2 == 0:
                   player = symbol_1
                elif count % 2 == 1:
                    player = symbol_2
                print("Player "+ player + ", it is your turn. ")
        # TODO: Update the board.
                row = int(input("Pick a row:"
                    "[upper row: enter 0, middle row: enter 1, bottom row: enter 2]:"))
                column = int(input("Pick a column:"
                       "[left column: enter 0, middle column: enter 1, right column enter 2]"))
                while (row > 2 or row < 0) or (column > 2 or column < 0):
                    outOfBoard(row, column)
                    row = int(input("Pick a row[upper row:"
                                    "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
                    column = int(input("Pick a column:"
                                    "[left column: enter 0, middle column: enter 1, right column enter 2]"))

                # Check if the square is already filled
                while (board[row][column] == symbol_1)or (board[row][column] == symbol_2):
                    filled = illegal(board, symbol_1, symbol_2, row, column)
                    row = int(input("Pick a row[upper row:"
                                    "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
                    column = int(input("Pick a column:"
                                        "[left column: enter 0, middle column: enter 1, right column enter 2]"))
                if player == symbol_1:
                    board[row][column] = symbol_1
                        
                else:
                    board[row][column] = symbol_2
                
                return (board)
        
        
        winner = 'X'  # FIXME
