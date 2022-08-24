"""
https://leetcode.com/problems/degree-of-an-array/
"""

from collections import defaultdict


class Solution:
    def findShortestSubArray(self, nums):
        if len(nums) == 1:
            return 1

        degree = 1
        dict = defaultdict(list)
        for index, value in enumerate(nums):
            if value in dict.keys():
                dict[value][0] = dict[value][0] + 1
                dict[value].append(index)
            else:
                dict[value] = [1, index]
            degree = max(degree, dict[value][0])


        min_length = len(nums)
        for key, value in dict.items():
            if value[0] == degree:
                length = value[len(value) - 1] - value[1] + 1
                min_length = min(min_length, length)

        return min_length

    def findShortestSubArray2(self, nums):
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans

print(Solution().findShortestSubArray([1,1]))