"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        array = []

        for i in s:
            if (i.isalnum()):
                array.append(i.lower())

        size = len(array)
        index = 0

        while (index < size - 1 - index):
            if (array[index] != array[size - 1 - index]):
                return False
            index += 1

        return True