"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

This problem can be viewed as finding all ascending sequences.
"""
class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0

        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            if diff > 0:
                profit += diff

        return profit