"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        else:
            str1AlphNum = [0] * 26
            str2AlphNum = [0] * 26

            for alph in s:
                index = ord(alph) - 97
                str1AlphNum[index] += 1

            for alph in t:
                index = ord(alph) - 97
                str2AlphNum[index] += 1

            for i in range(26):
                if (str1AlphNum[i] != str2AlphNum[i]):
                    return False

            return True
