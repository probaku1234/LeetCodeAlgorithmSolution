"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/
"""
class Solution:
    def containsDuplicate(self, nums) -> bool:
        dic = {}
        for n in nums:
            if dic.get(n) == 1:
                return True
            else:
                dic[n] = 1
        return False