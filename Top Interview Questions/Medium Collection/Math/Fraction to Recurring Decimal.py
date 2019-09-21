"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/821/
"""


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = '-' if numerator * denominator < 0 else ''
        quotient, remainder = divmod(abs(numerator), abs(denominator))
        result_list = [sign, str(quotient), '.']
        remainders = []
        while remainder not in remainders:
            remainders.append(remainder)
            quotient, remainder = divmod(remainder * 10, abs(denominator))
            result_list.append(str(quotient))

        idx = remainders.index(remainder)
        result_list.insert(idx + 3, '(')
        result_list.append(')')
        result = ''.join(result_list).replace('(0)', '').rstrip('.') # get rid of (0)
        return result


print(Solution().fractionToDecimal(1, 4))
