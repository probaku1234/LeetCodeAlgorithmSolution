"""
URL : https://leetcode.com/explore/interview/card/google/64/dynamic-programming-4/3087/
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_max_value, current_min_value = nums[0], nums[0]
        result = nums[0]
        for num in nums[1:]:
            current_max_value, current_min_value = max(num, current_max_value * num, current_min_value * num), \
                                                   min(num, current_max_value * num, current_min_value * num)
            result = max(result, current_max_value)
        return result


Solution().maxProduct([2, -3, -2, 4])