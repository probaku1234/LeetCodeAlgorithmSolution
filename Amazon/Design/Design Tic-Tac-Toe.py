"""
URL : https://leetcode.com/explore/interview/card/amazon/81/design/517/
"""


class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.row_count_1 = [0] * n
        self.row_count_2 = [0] * n
        self.col_count_1 = [0] * n
        self.col_count_2 = [0] * n
        self.main_diagonal_count1 = [0]
        self.main_diagonal_count2 = [0]
        self.anti_diagonal_count1 = [0]
        self.anti_diagonal_count2 = [0]

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        row_count_list = self.row_count_1 if player == 1 else self.row_count_2
        col_count_list = self.col_count_1 if player == 1 else self.col_count_2
        main_diagonal_count = self.main_diagonal_count1 if player == 1 else self.main_diagonal_count2
        anti_diagonal_count = self.anti_diagonal_count1 if player == 1 else self.anti_diagonal_count2

        row_count_list[row] += 1
        col_count_list[col] += 1

        if row == col:
            main_diagonal_count[0] += 1
        if row + col == self.n - 1:
            anti_diagonal_count[0] += 1

        if self.n in [row_count_list[row], col_count_list[col], main_diagonal_count[0], anti_diagonal_count[0]]:
            return player
        else:
            return 0
