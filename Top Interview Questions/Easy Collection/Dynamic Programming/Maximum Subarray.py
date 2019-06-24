"""
URL : https://www.cnblogs.com/zuoyuan/p/3781988.html
"""
import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = 0
        maxSum = -sys.maxsize - 1

        for i in range(len(nums)):
            if currentSum < 0:
                currentSum = 0

            currentSum += nums[i]
            maxSum = max(currentSum, maxSum)

        return maxSum