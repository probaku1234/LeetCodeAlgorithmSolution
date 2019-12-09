"""
URL : https://leetcode.com/explore/interview/card/google/66/others-4/3098/
"""
from collections import defaultdict

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0 or len(s) == 1:
            return True

        s_dict = defaultdict(set)
        t_dict = defaultdict(set)

        for index, char in enumerate(s):
            s_dict[char].add(index)

        for index, char in enumerate(t):
            t_dict[char].add(index)

        if len(s_dict.keys()) != len(t_dict.keys()):
            return False

        for key, value in s_dict.items():
            found = False

            for v in t_dict.values():
                if value == v:
                    found = True
                    break

            if not found:
                return False
        return True


print(Solution().isIsomorphic('foo','title'))
