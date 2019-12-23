"""
URL : https://leetcode.com/explore/interview/card/google/59/array-and-strings/3058/
"""
import itertools


class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        is_start = False
        max_distance = 0
        current_length = 1
        start_index = -1

        for index, s in enumerate(seats):
            if s == 0:
                if is_start:
                    current_length += 1
                else:
                    is_start = True
                    start_index = index
            else:
                if is_start:
                    is_start = False
                    end_index = index
                    if start_index == 0:
                        max_distance = max(max_distance, current_length)
                    else:
                        max_distance = max(max_distance, (end_index - (start_index-1)) // 2)
                    start_index = -1
                    current_length = 1

        if is_start:
            max_distance = max(max_distance, current_length)

        return max_distance

    def maxDistToClosest2(self, seats):
        ans = 0
        for seat, group in itertools.groupby(seats):
            if not seat:
                pika = list(group)
                K = len(list(group))
                ans = max(ans, (K + 1) / 2)

        return max(ans, seats.index(1), seats[::-1].index(1))

print(Solution().maxDistToClosest2([1,1,0,0,0,1,0]))
print(Solution().maxDistToClosest([1,0,0,0]))
print(Solution().maxDistToClosest([0,0,0,1]))