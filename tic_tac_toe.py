import random


def board_draw(board):
    # draws the board
    print("    |" + "     |"), print(board[6] + "   |" + "  " + board[7] + "  |" + " " + board[8])
    print("    |" + "     |"), print("------------------"), print("    |" + "     |")
    print(board[3] + "   |" + "  " + board[4] + "  |" + " " + board[5]), print("    |" + "     |")
    print("------------------"), print("    |" + "     |")
    print(board[0] + "   |" + "  " + board[1] + "  |" + " " + board[2]), print("    |" + "     |")


def player_type():
    # player selection
    player_marker = " "
    while player_marker not in ["X", "O"]:
        player_marker = input('Player 1: Do you want to be X or O? ').upper()
    if player_marker == "X":
        return "X", "O"
    else:
        return "O", 'X'


def player_selection(player):
    # assign players their marker
    player1 = player[0]
    player2 = player[1]
    return player1, player2


def first_player():
    # randomly selects which player gets to go first
    if random.randint(0, 1) == 0:
        return "Player 1"
    else:
        return "Player 2"


def get_position():
    # gets where the marker will be place
    position = 0
    while position not in range(1, 10):
        position = int(input("Choose a position between 1-9: "))
    return position


def input_board(position, player, board):
    board[position - 1] = player


def check_space(position, board):
    # checks if the specified position is occupied
    if board[position - 1] != " ":
        return True
    else:
        return False


def game_won(board, marker):
    # checks the board if anyone won
    return (board[6] == marker and board[3] == marker and board[0] == marker) or \
           (board[7] == marker and board[4] == marker and board[1] == marker) or \
           (board[8] == marker and board[5] == marker and board[2] == marker) or \
           (board[6] == marker and board[7] == marker and board[8] == marker) or \
           (board[3] == marker and board[4] == marker and board[5] == marker) or \
           (board[0] == marker and board[1] == marker and board[2] == marker) or \
           (board[6] == marker and board[4] == marker and board[2] == marker) or \
           (board[0] == marker and board[4] == marker and board[8] == marker)


def draw(board):
    if " " not in board:
        return True
    else:
        return False


def replay():
    play = input('Do you want to play again? Enter Yes or No: ').capitalize()
    while play not in ["Yes", "No"]:
        play = input('Do you want to play again? Enter Yes or No: ').capitalize()
    return play


def main():
    print("Welcome to Tic Tac Toe")
    play_game = True

    while play_game:
        board = [' '] * 9
        player = player_type()
        player1, player2 = player_selection(player)
        board_draw(board)
        turn = first_player()
        keep_playing = True

        while keep_playing:
            if turn == "Player 1":
                print("Player 1 Turn")
                position = get_position()

                while check_space(position, board):
                    position = get_position()

                input_board(position, player1, board)
                board_draw(board)

                if game_won(board, player1):
                    print("Player 1 won the game!")
                    keep_playing = False
                else:
                    # return true only when board is full of X or O values else skip
                    if draw(board):
                        board_draw(board)
                        print('The game is a draw!')
                        keep_playing = False
                        break
                    else:
                        turn = "Player 2"
            else:
                print("Player 2 Turn")
                position = get_position()

                while check_space(position, board):
                    position = get_position()

                input_board(position, player2, board)
                board_draw(board)

                if game_won(board, player2):
                    print("Player 2 won the game!")
                    keep_playing = False
                else:
                    if draw(board):
                        board_draw(board)
                        print('The game is a draw!')
                        keep_playing = False
                        break
                    else:
                        turn = "Player 1"
        if replay() != "Yes":
            play_game = False


main()
