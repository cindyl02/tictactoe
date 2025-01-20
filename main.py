def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    display_board(board)
    while True:
        x_row = int(input("Player X: Enter row (0-2): "))
        x_col = int(input("Player X: Enter col (0-2): "))

        if board[x_row][x_col] == " ":
            board[x_row][x_col] = "X"

        display_board(board)

        if is_winner_found(board):
            print("Game over")
            return

        if is_board_full(board):
            print("Game over")
            return

        o_row = int(input("Player O: Enter row (0-2): "))
        o_col = int(input("Player O: Enter col (0-2): "))

        if board[o_row][o_col] == " ":
            board[o_row][o_col] = "O"

        display_board(board)

        if is_winner_found(board):
            print("Game over")
            return

        if is_board_full(board):
            print("Game over")
            return


def display_board(board):
    for index, row in enumerate(board):
        print("|".join(row))
        if index < 2:
            print("\n---------")


def is_winner_found(board):
    for i in range(3):
        if board[i][0] == "X" and board[i][1] == "X" and board[i][2] == "X":
            print("Player X is the winner")
            return True
        elif board[i][0] == "O" and board[i][1] == "O" and board[i][2] == "O":
            print("Player O is the winner")
            return True
    for j in range(3):
        if board[0][j] == "X" and board[1][j] == "X" and board[2][j] == "X":
            print("Player X is the winner")
            return True
        elif board[0][j] == "O" and board[1][j] == "O" and board[2][j] == "O":
            print("Player O is the winner")
            return True
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        print("Player X is the winner")
        return True
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        print("Player X is the winner")
        return True
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        print("Player O is the winner")
        return True
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        print("Player O is the winner")
        return True
    return False


def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True


if __name__ == '__main__':
    print("TIC TAC TOE\n")
    play_tic_tac_toe()
