"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
"""


class Solution:
    def removeDuplicates(self, nums) -> int:
        if (len(nums) == 0):
            return 0
        else:
            temp = nums[0]
            length = 1
            index = 0

            for i in nums:
                if (i != temp):
                    length += 1
                    temp = i
                    index += 1
                    nums[index] = i

            return length