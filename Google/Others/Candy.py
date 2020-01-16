"""
URL : https://leetcode.com/explore/interview/card/google/66/others-4/3097/
"""


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        ans = 0
        left2right = [1] * n
        right2left = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left2right[i] = left2right[i-1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right2left[i] = right2left[i+1] + 1

        for i in range(n):
            ans += max(left2right[i], right2left[i])

        return ans