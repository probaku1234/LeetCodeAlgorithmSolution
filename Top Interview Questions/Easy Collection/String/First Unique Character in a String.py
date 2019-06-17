"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        alpNum = [0] * 26
        alpIndex = [-1] * 26

        for i in range(len(s)):
            index = ord(s[i]) - 97
            alpNum[index] += 1
            if (alpIndex[index] == -1):
                alpIndex[index] = i

        for alphbet in s:
            index = ord(alphbet) - 97
            if (alpNum[index] == 1):
                return alpIndex[index]

        return -1