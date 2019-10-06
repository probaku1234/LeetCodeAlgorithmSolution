"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/803/
"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 1:
            return intervals

        sorted_list = sorted(intervals, key=lambda l:l[0])

        index = 0
        while index < len(sorted_list)-1:
            if sorted_list[index][1] >= sorted_list[index+1][1]:
                sorted_list.pop(index+1)
            elif sorted_list[index][1] >= sorted_list[index+1][0]:
                sorted_list.insert(index, [sorted_list[index][0], sorted_list[index+1][1]])
                sorted_list.pop(index+1)
                sorted_list.pop(index+1)
            else:
                index += 1

        return sorted_list

print(Solution().merge([[1,4],[2,3]]))