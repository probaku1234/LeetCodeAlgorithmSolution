"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/
"""
class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i,j]

    def twoSumHash(self, nums, target):
        dic = {}
        for index, num in enumerate(nums):
            complement = target - num
            if dic.get(complement) is not None and dic.get(complement) != index:
                return [index, dic.get(complement)]
            dic[num] = index

Solution().twoSumHash([2,7,11,15], 9)