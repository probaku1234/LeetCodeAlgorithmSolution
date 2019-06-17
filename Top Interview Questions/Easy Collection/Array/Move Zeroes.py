"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/
"""
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        count = 0

        while (count < len(nums)):
            if (nums[index] == 0):
                nums.append(0)
                nums.pop(index)
            else:
                index += 1
            count += 1

