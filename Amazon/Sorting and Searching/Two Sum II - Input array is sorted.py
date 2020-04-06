"""
URL : https://leetcode.com/explore/interview/card/amazon/79/sorting-and-searching/2994/
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1
        result = [0,0]

        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                result[0] = i+1
                result[1] = j+1
                break

        return result


print(Solution().twoSum([2, 7, 11, 15], 9))
