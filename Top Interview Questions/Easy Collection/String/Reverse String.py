"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/
"""
class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)

        for i in reversed(s):
            s.append(i)

        del s[0:n]