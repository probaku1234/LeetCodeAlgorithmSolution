"""
URL : https://leetcode.com/explore/interview/card/google/59/array-and-strings/341/
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n == 0:
            return 0

        left_max = [-1] * n
        right_max = [-1] * n
        answer = 0

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i - 1])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        for i in range(1, n - 1):
            answer += min(left_max[i], right_max[i]) - height[i]

        return answer


print(Solution().trap([0,1,0,2,1,0,1,3]))