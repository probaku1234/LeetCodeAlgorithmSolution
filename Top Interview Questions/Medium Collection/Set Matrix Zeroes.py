"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/
"""
class Solution(object):
    def helper(self, matrix, i, j):
        for x in range(len(matrix[0])):
            matrix[i][x] = 0

        for x in range(len(matrix)):
            matrix[x][j] = 0

    # space complexity O(m+n)
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) != 0:
            indice = []
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == 0:
                        indice.append((i, j))

            for i, j in indice:
                self.helper(matrix, i, j)