"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/
"""
class Solution:
    def myAtoi(self, str: str) -> int:
        strForConvert = ""
        isFound = False

        for c in str:
            if not isFound:
                if c.isdigit():
                    isFound = True
                    strForConvert = strForConvert + c
                else:
                    if c == ' ':
                        continue
                    if c == '-' or c == '+':
                        isFound = True
                        strForConvert = strForConvert + c
                    else:
                        return 0
            else:
                if c.isdigit():
                    strForConvert = strForConvert + c
                else:
                    break

        if len(strForConvert) == 0:
            return 0

        if (strForConvert[0] == '-' or strForConvert[0] == '+') and len(strForConvert) == 1:
            return 0

        convertedInt = int(strForConvert)

        if convertedInt > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif convertedInt < -2 ** 31:
            return -2 ** 31
        else:
            return convertedInt

s = Solution()
print(s.myAtoi("3.1423"))