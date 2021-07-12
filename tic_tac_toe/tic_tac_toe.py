class Board:
    def __init__(self, board):
        self.board = board

    def get_vertical(self):
        vertical = [[], [], []]

        for i in range(3):
            vertical[0].append(self.board[i][0])
            vertical[1].append(self.board[i][1])
            vertical[2].append(self.board[i][2])

        return vertical

    def get_diagonal(self):
        return (
            [row[i] for i, row in enumerate(self.board)],  # gets the diagonal from top-left to bottom-right
            [row[::-1][i] for i, row in enumerate(self.board)],  # gets the diagonal from top-right to bottom-left
        )

    def get_horizontal(self):
        return self.board

    def board_is_finished(self):
        for row in self.board:
            if 0 in row:
                return False
        else:
            return True


class Checker(Board):
    def check(self):
        board_forms = self.get_diagonal(), self.get_vertical(), self.get_horizontal()

        for rows in board_forms:
            winner = self.check_board(rows)
            if winner:
                return winner
        else:
            if self.board_is_finished():
                return 0
            else:
                return -1

    def check_board(self, rows):
        for row in rows:
            winner = self.check_row(row)

            if winner:
                return winner

        return 0

    @staticmethod
    def check_row(row):
        if row == [1, 1, 1]:
            return 1
        elif row == [2, 2, 2]:
            return 2
        else:
            return 0
