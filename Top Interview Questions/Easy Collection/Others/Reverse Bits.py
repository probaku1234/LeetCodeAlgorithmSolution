"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/648/
"""


class Solution:
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res <<= 1
            res |= ((n >> i) & 1)
        return res

if __name__ == "__main__":
    s = Solution()