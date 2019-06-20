"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        sizeOfNeedle = len(needle)
        sizeOfHaystack = len(haystack)

        if sizeOfNeedle == 0 or haystack == needle:
            return 0

        if sizeOfNeedle > sizeOfHaystack:
            return -1

        for i in range(sizeOfHaystack - sizeOfNeedle + 1):
            if haystack[i:i + sizeOfNeedle] == needle:
                return i

        return -1