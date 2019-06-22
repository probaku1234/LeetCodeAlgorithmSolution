"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/
"""
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ''

        res = ''

        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res