"""
URL : https://leetcode.com/explore/interview/card/google/66/others-4/477/
"""


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: None
        """
        self.matrix[row][col] = val

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        count = 0

        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                count += self.matrix[i][j]

        return count

