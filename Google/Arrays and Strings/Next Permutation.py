"""
URL : https://leetcode.com/explore/interview/card/google/59/array-and-strings/3050/
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        nums[i+1:] = reversed(nums[i+1:])
        print(nums)

Solution().nextPermutation([9, 5, 4, 3, 1])
