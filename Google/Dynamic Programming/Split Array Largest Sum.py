"""
URL : https://leetcode.com/explore/interview/card/google/64/dynamic-programming-4/3089/
"""
import sys
import math


class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        if len(nums) == m:
            return max(nums)

        n = len(nums)
        f = [[sys.maxsize for i in range(m+1)] for j in range(n+1)]
        sub = [0] * (n+1)

        for i in range(n):
            sub[i+1] = sub[i] + nums[i]

        f[0][0] = 0

        for i in range(1, n+1):
            for j in range(1, m+1):
                for k in range(i):
                    f[i][j] = min(f[i][j], max(f[k][j-1], sub[i]-sub[k]))

        return f[n][m]

print(Solution().splitArray([7,2,5,10,8], 2))