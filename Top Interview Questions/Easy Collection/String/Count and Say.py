"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/886/
REFERENCE : https://www.geeksforgeeks.org/look-and-say-sequence/
"""
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        if n == 2:
            return '11'

        result = "11"
        for i in range(3, n + 1):
            result += '$'
            length = len(result)

            count = 1
            temp = ""

            for j in range(1, length):
                if result[j] != result[j - 1]:
                    temp += str(count + 0)

                    temp += result[j - 1]

                    count = 1

                else:
                    count += 1

            result = temp
        return result;
