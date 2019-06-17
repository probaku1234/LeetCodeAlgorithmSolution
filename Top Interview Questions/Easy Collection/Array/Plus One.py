"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
"""


class Solution:
    def plusOne(self, digits):
        carry = 0
        result = []
        digits[len(digits) - 1] += 1

        for index, number in reversed(list(enumerate(digits))):
            value = number + carry
            if (value >= 10):
                carry = 1
                result.insert(0, value - 10)
            else:
                carry = 0
                result.insert(0, value)
        if (carry == 1):
            result.insert(0, carry)

        return result
