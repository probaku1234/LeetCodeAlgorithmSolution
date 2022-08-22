"""
URL : https://leetcode.com/explore/interview/card/google/63/sorting-and-searching-4/445/

Greedy algorithms

Add to the output all the intervals starting before newInterval.
Add to the output newInterval. Merge it with the last added interval if newInterval starts before the last added interval.
Add the next intervals one by one. Merge with the last added interval if the current interval starts before the last added interval.
"""


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        index = 0
        n = len(intervals)

        while index < n and newInterval[0] > intervals[index][0]:
            ans.append(intervals[index])
            index += 1

        if not ans or ans[-1][1] < newInterval[0]:
            ans.append(newInterval)
        else:
            ans[-1][1] = max(ans[-1][1], newInterval[1])

        while index < n:
            interval = intervals[index]
            start, end = interval
            index += 1

            if ans[-1][1] < start:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], end)

        return ans

print(Solution().insert([[6,7],[8,10],[12,16]], [4,8]))