"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/815/
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1:
            return True

        sum_list = [n]
        number = n
        while True:
            sum = 0
            for a in str(number):
                sum += pow(int(a), 2)

            if sum == 1:
                return True

            if sum in sum_list:
                return False
            sum_list.append(sum)
            number = sum
