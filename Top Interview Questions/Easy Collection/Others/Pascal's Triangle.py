"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/601/
"""
class Solution:
    def generate(self, numRows: int):
        result = []

        for i in range(1, numRows + 1):
            m = []
            for j in range(i):
                if j == 0 or j == i - 1:
                    m.append(1)
                else:
                    m.append(result[i - 2][j - 1] + result[i - 2][j])

            result.append(m)
        return result
