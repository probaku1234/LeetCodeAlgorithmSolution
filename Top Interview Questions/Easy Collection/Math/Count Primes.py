"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/744/
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        vis = [False] * n
        for i in range(2, int(n ** 0.5) + 1):
            if vis[i]: continue
            j = i
            while j * i < n:
                vis[j * i] = True
                j += 1
        ans = 0
        for i in range(2, n):
            if not vis[i]: ans += 1
        return ans
