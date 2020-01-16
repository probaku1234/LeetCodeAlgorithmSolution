"""
URL : https://leetcode.com/explore/interview/card/google/66/others-4/3103/
"""


class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        index = 0

        while index < len(start):
            if start[index] != end[index]:
                if index + 1 == len(start):
                    return False

                if (start[index:index+2] == 'RX' or start[index:index+2] == 'XL') and (start[index:index+2] == ''.join(reversed(end[index:index+2]))):
                    index += 2
                else:
                    return False
            else:
                index += 1

        return True

print(Solution().canTransform('RL', 'LR'))