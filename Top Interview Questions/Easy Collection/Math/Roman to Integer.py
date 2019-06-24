"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/878/
"""


class Solution:
    def romanToInt(self, s):
        dictForSingle = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        dictForDouble = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        index = 0
        result = 0
        size = len(s)

        while index < size:
            if index + 1 < size:
                if s[index:index+2] in dictForDouble:
                    result += dictForDouble[s[index:index+2]]
                    index += 2
                else:
                    result += dictForSingle[s[index]]
                    index += 1
            else:
                result += dictForSingle[s[index]]
                index += 1
        return result

s = Solution()
print(s.romanToInt(""))