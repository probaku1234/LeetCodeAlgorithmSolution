"""
URL : https://leetcode.com/explore/interview/card/google/59/array-and-strings/3056/
"""
import itertools


class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        # zip function map the similar index of multiple containers
        # unzip with * operator
        def RLE(S):
            return zip(*[(k, len(list(grp))) for k, grp in itertools.groupby(S)])

        R, count = RLE(S)
        ans = 0
        for word in words:
            R2, count2 = RLE(word)
            if R2 != R: continue
            ans += all(c1 >= max(c2, 3) or c1 == c2
                       for c1, c2 in zip(count, count2))

        return ans

