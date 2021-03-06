"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/587/
"""
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last, i, j = m + n - 1, m - 1, n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                last, i = last - 1, i - 1
            else:
                nums1[last] = nums2[j]
                last, j = last - 1, j - 1

        while j >= 0:
            nums1[last] = nums2[j]
            last, j = last - 1, j - 1

if __name__ == "__main__":
    s = Solution()
