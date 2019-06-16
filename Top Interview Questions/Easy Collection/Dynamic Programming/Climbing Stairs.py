"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/569/
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        m = [1] * (n + 1)

        if n > 1:
            for i in range(2, n + 1):
                m[i] = m[i - 1] + m[i - 2]

        return m[n]