"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/798/
"""


class Solution:
    # two-pass
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        num_of_zero = 0
        num_of_one = 0
        num_of_two = 0

        for num in nums:
            if num == 0:
                num_of_zero += 1
            if num == 1:
                num_of_one += 1
            if num == 2:
                num_of_two += 1

        index = 0
        for i in range(num_of_zero):
            nums[index] = 0
            index += 1

        for i in range(num_of_one):
            nums[index] = 1
            index += 1

        for i in range(num_of_two):
            nums[index] = 2
            index += 1

    # one-pass
    def sortColors2(self, nums):
        index = 0
        left = 0
        right = len(nums) -1
        while index <= right:
            if nums[index] == 0:
                nums[index], nums[left] = nums[left], nums[index]
                index += 1
                left += 1
            elif nums[index] == 2:
                nums[index], nums[right] = nums[right], nums[index]
                right -= 1
            else:
                index += 1

s = Solution()
nums = [2,0,2,1,1,0]
s.sortColors2(nums)
print(nums)


