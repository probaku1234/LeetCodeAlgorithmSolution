"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/780/
"""


class Solution:
    def getlongestpalindrome(self, str, left, right):
        while left >= 0 and right < len(str) and str[left] == str[right]:
            left -= 1;
            right += 1
        return str[left + 1: right]

    def longestPalindrome(self, s):
        palindrome = ''
        for index in range(len(s)):
            len1 = len(self.getlongestpalindrome(s, index, index))
            if len1 > len(palindrome):
                palindrome = self.getlongestpalindrome(s, index, index)
            len2 = len(self.getlongestpalindrome(s, index, index + 1))
            if len2 > len(palindrome):
                palindrome = self.getlongestpalindrome(s, index, index + 1)
        return palindrome


s = Solution()
print(s.longestPalindrome("babad"))