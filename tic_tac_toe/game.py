class TicTacToe:
    def __init__(self):
        self.helper = [str(i+1) for i in range(9)]
        self.board = [" " for i in range(9)]
        self.available = [i for i in range(9)]
        self.winner = None

    def print_board(self):
        line = "-------------"
        space = "            "
        print(space, "  AVAILABLE  ", space, "    TAKEN    ")
        for i in range(3):
            print(space, line, space, line)
            helper_row = self.helper[i*3 : (i+1)*3]
            row = self.board[i*3 : (i+1)*3]
            print(
                space,
                f"| {' | '.join(helper_row)} |",
                space,
                f"| {' | '.join(row)} |",
            )
        print(space, line, space, line, '\n')

    def place_move(self, letter, square):
        self.helper[square] = " "
        self.board[square] = letter
        self.available.remove(square)
        if self.check_for_winner(letter, square): self.winner = letter
        return self

    def reverse_move(self, letter, square):
        self.helper[square] = str(square + 1)
        self.board[square] = " "
        self.available.append(square)
        self.winner = None
        return self

    def check_for_winner(self, letter, square):

        # check row
        row_idx = square // 3
        row = self.board[row_idx*3 : (row_idx + 1)*3]
        if all(spot == letter for spot in row): return True

        # check column
        col_idx = square % 3
        col = [self.board[col_idx + i*3] for i in range(3)]
        if all(spot == letter for spot in col): return True

        # check diagonals
        if square % 2 == 0:
            diag1 = [self.board[i] for i in [0,4,8]]
            if all(spot == letter for spot in diag1): return True
            diag2 = [self.board[i] for i in [6,4,2]]
            if all(spot == letter for spot in diag2): return True

        return False
