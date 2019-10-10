"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/808/
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        d = [[0 for i in range(m)] for j in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0:
                    d[i][j] = 1
                elif j == 0:
                    d[i][j] = 1
                else:
                    d[i][j] = d[i-1][j] + d[i][j-1]

        return d[-1][-1]