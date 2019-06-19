"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/
"""


class Solution:
    def reverse(self, x: int) -> int:
        toString = str(x)
        isNegative = False
        if x < 0:
            isNegative = True

        toString = toString.replace('-','')
        reversedString = toString[::-1]

        if isNegative:
            reversedString = '-' + reversedString

        reversedInt = int(reversedString)
        if reversedInt > 2 ** 31 - 1 or reversedInt < -2 ** 31:
            return 0

        return reversedInt

s = Solution()
print(s.reverse(-123))
