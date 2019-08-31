"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/824/
"""
import math

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        dict = {}
        ans = 0

        for num in nums:
            if num in dict.keys():
                dict[num] += 1
            else:
                dict[num] = 1

            if dict[num] > math.floor(size/2):
                ans = num

        return ans

s = Solution()
print(s.majorityElement([3,2,3]))