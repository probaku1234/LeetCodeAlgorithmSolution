"""
URL : https://leetcode.com/explore/interview/card/google/66/others-4/3099/
"""


class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) == 0:
            return True

        strobogrammatic_numbers = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        left = 0
        right = len(num) - 1

        while left <= right:
            if strobogrammatic_numbers.get(num[left]) is None or strobogrammatic_numbers.get(num[right]) is None or \
                    strobogrammatic_numbers[num[left]] != num[right]:
                return False

            left += 1
            right -= 1

        return True

