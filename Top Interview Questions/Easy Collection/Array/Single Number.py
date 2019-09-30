"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
Ref : http://laker.me/blog/2019/04/10/19_0410_leetcode136/
"""
class Solution:
    def singleNumber(self, nums) -> int:
        res = nums[0]

        for i in range(1, len(nums)):
            res = res ^ nums[i]

        return res