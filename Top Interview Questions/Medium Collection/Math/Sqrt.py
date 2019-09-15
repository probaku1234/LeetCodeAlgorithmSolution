"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/819/
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        else:
            start = 0
            end = x
            while start <= end:
                mid = int((start + end) / 2)
                if mid * mid == x:
                    return mid
                elif mid * mid < x:
                    start = mid + 1
                    ans = mid
                else:
                    end = mid - 1
            return ans


if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(8))
