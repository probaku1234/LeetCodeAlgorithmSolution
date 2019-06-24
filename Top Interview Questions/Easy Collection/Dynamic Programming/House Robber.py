"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/576/
"""


class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        max_money = [0] * len(nums)
        max_money[0] = nums[0]
        max_money[1] = max(nums[0], nums[1])
        for house in range(2, len(nums)):
            max_money[house] = max(max_money[house - 1], max_money[house - 2] + nums[house])

        return max_money[-1]