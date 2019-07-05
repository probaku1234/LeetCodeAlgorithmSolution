"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/778/
"""
import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        m = collections.defaultdict(list)
        for s in strs:
            m[''.join(sorted(s))].append(s)
        return list(m.values())

s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
