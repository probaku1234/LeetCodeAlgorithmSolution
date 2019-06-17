"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
"""
class Solution:
    def intersect(self, nums1, nums2):
        first = []
        second = []
        result = []

        if (len(nums1) > len(nums2)):
            first = nums1
            second = nums2
        else:
            first = nums2
            second = nums1

        for x in second:
            for y in first:
                if (y == x):
                    result.append(x)
                    first.remove(x)

                    break

        return result