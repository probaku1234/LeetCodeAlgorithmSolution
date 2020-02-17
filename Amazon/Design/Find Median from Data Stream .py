"""
URL : https://leetcode.com/explore/interview/card/amazon/81/design/495/
"""
from bisect import bisect_left


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.int_list = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.int_list) == 0:
            self.int_list.append(num)
        else:
            i = bisect_left(self.int_list, num)
            self.int_list.insert(i, num)

    def findMedian(self):
        """
        :rtype: float
        """
        n = len(self.int_list)
        if n % 2 == 1:
            return self.int_list[n//2]
        else:
            return (self.int_list[n//2] + self.int_list[n // 2 - 1])/2
