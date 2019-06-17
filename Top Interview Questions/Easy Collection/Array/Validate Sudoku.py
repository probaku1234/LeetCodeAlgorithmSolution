"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/
"""
class Solution:
    def isValidSudoku(self, board) -> bool:
            if board is None or len(board) != 9 or len(board[0]) != 9:
                return False

            for i in range(9):
                m = [False] * 9
                for j in range(9):
                    if board[i][j] != '.':
                        if m[int(board[i][j]) -1]:
                            return False
                        m[int(board[i][j]) -1] = True

            for j in range(9):
                m = [False] * 9
                for i in range(9):
                    if board[i][j] != '.':
                        if m[int(board[i][j]) - 1]:
                            return False
                        m[int(board[i][j]) - 1] = True

            for block in range(9):
                m = [False] * 9
                for i in range(block // 3 * 3, block // 3 * 3  + 3):
                    for j in range(block % 3 * 3, block % 3 * 3 + 3):
                        if board[i][j] != '.':
                            if m[int(board[i][j]) - 1]:
                                return False
                            m[int(board[i][j]) - 1] = True

            return True