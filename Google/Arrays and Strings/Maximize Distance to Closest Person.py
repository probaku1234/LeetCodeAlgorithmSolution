"""
URL : https://leetcode.com/explore/interview/card/google/59/array-and-strings/3058/
"""


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

print(Solution().maxDistToClosest([1,1,0,0,0,1,0]))
print(Solution().maxDistToClosest([1,0,0,0]))
print(Solution().maxDistToClosest([0,0,0,1]))