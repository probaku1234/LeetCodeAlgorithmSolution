"""
URL : https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/502/
"""

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1_list = version1.split('.')
        version2_list = version2.split('.')

        i, j = 0, 0

        while i < len(version1_list) and j < len(version2_list):
            v1 = int(version1_list[i])
            v2 = int(version2_list[j])
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
            else:
                i += 1
                j += 1

        if i < len(version1_list):
            for index in range(i, len(version1_list)):
                if int(version1_list[index]) > 0:
                    return 1
            return 0
        elif j < len(version2_list):
            for index in range(j, len(version2_list)):
                if int(version2_list[index]) > 0:
                    return -1
            return 0
        else:
            return 0


print(Solution().compareVersion('0.1', '1.1'))
print(Solution().compareVersion('1.0.1', '1'))
print(Solution().compareVersion('7.5.2.4', '7.5.3'))
print(Solution().compareVersion('1.01', '1.0001'))
print(Solution().compareVersion('1.0', '1.0.0'))
