import main


def test_full_board():
    board = [["X", "O", "X"], ["X", "O", "O"], ["X", "O", "X"]]
    assert main.is_board_full(board)


def test_empty_board():
    board = [[" " for _ in range(3)] for _ in range(3)]
    assert not main.is_board_full(board)


def test_half_full_board():
    board = [["X", "O", "X"], ["X", " ", "O"], ["O", " ", "X"]]
    assert not main.is_board_full(board)


def test_is_winner_found_x_win(capfd):
    board = [["X", "O", "X"], ["X", "O", "O"], ["X", " ", " "]]
    assert main.is_winner_found(board)
    out, err = capfd.readouterr()
    assert "Player X is the winner" in out

    board = [["O", "X", "X"], [" ", "X", "O"], ["O", "X", " "]]
    assert main.is_winner_found(board)
    out, err = capfd.readouterr()
    assert "Player X is the winner" in out

    board = [["O", "X", "X"], [" ", " ", "X"], ["O", "O", "X"]]
    assert main.is_winner_found(board)
    out, err = capfd.readouterr()
    assert "Player X is the winner" in out

    board = [["X", "X", "X"], [" ", "O", "O"], [" ", "O", " "]]
    assert main.is_winner_found(board)
    out, err = capfd.readouterr()
    assert "Player X is the winner" in out

    board = [[" ", " ", " "], ["X", "X", "X"], ["O", "O", " "]]
    assert main.is_winner_found(board)
    out, err = capfd.readouterr()
    assert "Player X is the winner" in out

    board = [[" ", "O", " "], [" ", "O", " "], ["X", "X", "X"]]
    assert main.is_winner_found(board)
    out, err = capfd.readouterr()
    assert "Player X is the winner" in out

    board = [["X", "O", "X"], [" ", "X", " "], ["O", "O", "X"]]
    assert main.is_winner_found(board)
    out, err = capfd.readouterr()
    assert "Player X is the winner" in out

    board = [["O", " ", "X"], [" ", "X", " "], ["X", "O", "O"]]
    assert main.is_winner_found(board)
    out, err = capfd.readouterr()
    assert "Player X is the winner" in out


def test_is_winner_found_o_win(capfd):
    board = [["O", "X", " "], ["O", "X", "X"], ["O", " ", " "]]
    assert main.is_winner_found(board)
    out, err = capfd.readouterr()
    assert "Player O is the winner" in out

    board = [["X", "O", "X"], [" ", "O", " "], ["X", "O", " "]]
    assert main.is_winner_found(board)
    out, err = capfd.readouterr()
    assert "Player O is the winner" in out

    board = [["X", " ", "O"], [" ", " ", "O"], ["X", "X", "O"]]
    assert main.is_winner_found(board)
    out, err = capfd.readouterr()
    assert "Player O is the winner" in out

    board = [["O", "O", "O"], [" ", "X", "X"], [" ", "X", " "]]
    assert main.is_winner_found(board)
    out, err = capfd.readouterr()
    assert "Player O is the winner" in out

    board = [[" ", " ", " "], ["O", "O", "O"], ["X", "X", " "]]
    assert main.is_winner_found(board)
    out, err = capfd.readouterr()
    assert "Player O is the winner" in out

    board = [[" ", "X", " "], [" ", "X", " "], ["O", "O", "O"]]
    assert main.is_winner_found(board)
    out, err = capfd.readouterr()
    assert "Player O is the winner" in out

    board = [["O", "X", " "], [" ", "O", " "], ["X", "X", "O"]]
    assert main.is_winner_found(board)
    out, err = capfd.readouterr()
    assert "Player O is the winner" in out

    board = [["X", " ", "O"], [" ", "O", " "], ["O", "X", "X"]]
    assert main.is_winner_found(board)
    out, err = capfd.readouterr()
    assert "Player O is the winner" in out
