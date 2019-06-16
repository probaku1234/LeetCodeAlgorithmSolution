"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/572/
"""
import sys

class Solution:
    def maxProfit(self, prices) -> int:
        minPrice = sys.maxsize
        maxProfit = 0

        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice

        return maxProfit



