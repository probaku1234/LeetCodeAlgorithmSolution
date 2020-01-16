"""
URL : https://leetcode.com/explore/interview/card/google/66/others-4/3102/
"""


class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        Jset = set(J)
        return sum(s in Jset for s in S)


print(Solution().numJewelsInStones("aA", "aAAbbbb"))
