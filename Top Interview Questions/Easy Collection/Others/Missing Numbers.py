"""
URL :  https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/722/
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumOfAllNumbers = (n * (n + 1)) // 2

        for num in nums:
            sumOfAllNumbers -= num

        return sumOfAllNumbers