"""
URL : https://leetcode.com/explore/interview/card/google/59/array-and-strings/3055/
"""
from collections import OrderedDict


class Solution(object):
    def range_to_string(self, low, up):
        if low + 1 == up - 1:
            return str(low+1)
        else:
            return str(low+1) + '->' + str(up-1)

    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        ans = []

        if lower == upper:
            if len(nums) == 0:
                return [str(lower)]
            else:
                return []
        elif lower != upper and len(nums) == 0:
            return [str(lower) + '->' + str(upper)]

        if lower < nums[0]:
            if lower == nums[0] - 1:
                ans.append(str(lower))
            else:
                ans.append(str(lower) + '->' + str(nums[0] - 1))

        for index in range(len(nums)-1):
            if nums[index] < nums[index+1] - 1:
                ans.append(self.range_to_string(nums[index], nums[index+1]))

        if nums[-1] < upper:
            if nums[-1] == upper-1:
                ans.append(str(upper))
            else:
                ans.append(str(nums[-1] + 1) + '->' + str(upper))
        return ans


print(Solution().findMissingRanges([4, 5, 10, 50, 75], 3, 76))