"""
URL : https://leetcode.com/explore/interview/card/google/67/sql-2/472/
"""

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        temp_string = S.replace('-','').upper()
        print(temp_string)

        index = 0
        if len(temp_string) % K == 0:
            index = K
        else:
            index = len(temp_string) % K

        while index < len(temp_string):
            temp_string = temp_string[:index] + '-' + temp_string[index:]
            index += K + 1

        return temp_string
print(Solution().licenseKeyFormatting('5F3Z-2e-9-w', 3))
