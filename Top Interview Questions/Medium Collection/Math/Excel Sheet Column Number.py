"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/817/
"""
import math


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        count = 0

        for index in range(len(s) - 1, -1, -1):
            n = ord(s[index]) - ord('A') + 1
            if count > 0:
                x = int(math.pow(26, count))
                ans += x * n
            else:
                ans += n

            count += 1

        return ans

