"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/781/
"""


class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) < 3:
            return False

        a = b = None
        for n in nums:
            if a is None or a >= n:
                a = n
            elif b is None or b >= n:
                b = n
            else:
                return True
        return False

s = Solution()
print(s.increasingTriplet([2,1,5,0,6]))
