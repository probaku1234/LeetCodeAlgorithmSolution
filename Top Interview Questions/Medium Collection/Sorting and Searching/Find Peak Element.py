"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/801/
"""


class Solution(object):
    def search(self, num, start, end):
        if start == end:
            return start
        if start + 1 == end:
            return [start, end][num[start] < num[end]]
        mid = (start + end) // 2
        if num[mid] < num[mid - 1]:
            return self.search(num, start, mid - 1)
        if num[mid] < num[mid + 1]:
            return self.search(num, mid + 1, end)
        return mid

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        return self.search(nums, 0, size - 1)

print(Solution().findPeakElement([1,6,1,3,5,5,4]))