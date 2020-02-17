"""
URL : https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2973/
"""
from collections import Counter


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # Sets are significantly faster than lists if you want to check if an item is contained within it.
        banset = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        count = Counter(
            word for word in paragraph.lower().split())

        ans, best = '', 0
        for word in count:
            if count[word] > best and word not in banset:
                ans, best = word, count[word]

        return ans

print(Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ['hit']))