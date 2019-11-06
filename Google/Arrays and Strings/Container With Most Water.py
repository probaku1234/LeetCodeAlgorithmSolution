"""
URL : https://leetcode.com/explore/interview/card/google/59/array-and-strings/3048/
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        start_index = 0
        current_length = 0
        end_index = len(height) - 1
        turn = 0

        while start_index < end_index:
            max_area = max(max_area, min(height[start_index], height[end_index])*(end_index-start_index))
            if height[start_index] < height[end_index]:
                start_index += 1
            else:
                end_index -= 1

        return max_area

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))