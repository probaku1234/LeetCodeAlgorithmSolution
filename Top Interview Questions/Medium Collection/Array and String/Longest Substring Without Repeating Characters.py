"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/779/
"""
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or s == "":
            return 0

        result = 1
        count = 1
        alphaDict = defaultdict(list)
        alphaDict[s[0]] = [1, 0]

        for i in range(1, len(s)):
            if s[i] in alphaDict and alphaDict[s[i]][0] == 1:
                result = max(result, count)
                count = 0
                for alpha in alphaDict:
                    if alphaDict[alpha][1] <= alphaDict[s[i]][1]:
                        alphaDict[alpha][0] = 0
                    else:
                        count += 1

                count += 1
                alphaDict[s[i]] = [1, i]
            else:
                alphaDict[s[i]] = [1, i]
                count += 1
                result = max(result, count)

        return result

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or s == "":
            return 0

        n = len(s)
        alpha_set = set()
        result = 0
        i = 0
        j = 0

        while i < n and j < n:
            if s[j] not in alpha_set:
                alpha_set.add(s[j])
                j += 1
                result = max(result, j - i)
            else:
                alpha_set.remove(s[i])
                i += 1

        return result


s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))

