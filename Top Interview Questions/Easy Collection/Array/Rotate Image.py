"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/
"""
class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                print(matrix)

        for i in range(n):
            matrix[i].reverse()


matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]

s = Solution()
s.rotate(matrix)

