"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/818/
"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x==0 or x==1 or n==1:
            return x # We have the problem of 0^0 (that is not
                     # well-defined), we choose to return 0
        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        if n<0:
            return 1/self.myPow(x,-n)
        val = self.myPow(x,n//2)
        if n%2 ==0:
            return val*val
        return val*val*x