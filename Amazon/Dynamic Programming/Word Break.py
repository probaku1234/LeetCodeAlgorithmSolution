"""
URL : https://leetcode.com/explore/interview/card/amazon/80/dynamic-programming/2997/
"""


class Solution(object):
    def helper(self, s, word_set, start):
        if start == len(s):
            return True

        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_set and self.helper(s, word_set, end):
                return True
        return False

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.helper(s, set(wordDict), 0)

    def wordBreak2(self, s, wordDict):
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s)+1):
            for j in range(0, i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[len(s)]

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(Solution().wordBreak(s, wordDict))
