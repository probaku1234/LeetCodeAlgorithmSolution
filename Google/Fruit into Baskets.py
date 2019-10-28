"""
URL : https://leetcode.com/explore/interview/card/google/67/sql-2/3046/
"""


class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        max_length = 0
        index = 0
        type_set = set()
        length = 0
        temp_index = -1

        while index < len(tree):
            if len(type_set) <= 1:
                temp_length = len(type_set)
                type_set.add(tree[index])
                if temp_length != len(type_set):
                    temp_index = index
                length += 1
                index += 1
            elif tree[index] in type_set:
                length += 1
                index += 1
            else:
                if max_length < length:
                    max_length = length
                type_set.clear()
                length = 0
                index = temp_index

        if max_length < length:
            max_length = length
        return max_length

print(Solution().totalFruit([0, 1, 6, 6, 4, 4, 6]))