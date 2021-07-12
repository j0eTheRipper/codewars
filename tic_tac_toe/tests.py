from tic_tac_toe import Checker


def test_horizontal_win():
    board = [
        [1, 2, 1],
        [1, 1, 1],
        [2, 1, 0]
    ]

    checker = Checker(board)

    assert checker.check() == 1


def test_diagonal_win():
    board = [
        [2, 1, 1],
        [1, 2, 1],
        [0, 1, 2]
    ]

    checker = Checker(board)

    assert checker.check() == 2


def test_vertical_win():
    board = [
        [1, 2, 2],
        [2, 1, 2],
        [1, 1, 2]
    ]

    checker = Checker(board)

    assert checker.check() == 2


def test_draw():
    board = [
        [1, 2, 1],
        [1, 2, 1],
        [2, 1, 2],
    ]

    checker = Checker(board)

    assert checker.check() == 0


def test_unfinished():
    board = [
        [1, 2, 2],
        [1, 2, 1],
        [0, 1, 2],
    ]

    checker = Checker(board)

    assert checker.check() == -1
