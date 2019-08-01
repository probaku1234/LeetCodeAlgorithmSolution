"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/797/
"""


class Solution(object):
    def search(self, board, word, i, j, position):
        if position == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
            return False

        char = board[i][j]

        if char == word[position]:
            board[i][j] = '#'
            if self.search(board, word, i-1, j, position + 1):
                return True
            if self.search(board, word, i+1, j, position + 1):
                return True
            if self.search(board, word, i, j-1, position + 1):
                return True
            if self.search(board, word, i, j+1, position + 1):
                return True
            board[i][j] = char

        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(board) == 0:
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.search(board, word, i, j, 0):
                    return True

        return False
