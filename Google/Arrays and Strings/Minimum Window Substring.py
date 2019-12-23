"""
URL : https://leetcode.com/explore/interview/card/google/59/array-and-strings/345/
"""
from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        dict_t = Counter(t)
        required = len(dict_t)
        left, right = 0, 0
        formed = 0
        window_count = {}

        ans = float('inf'), None, None

        while right < len(s):
            character = s[right]
            window_count[character] = window_count.get(character, 0) + 1

            if character in dict_t and window_count[character] == dict_t[character]:
                formed += 1

            while left <= right and formed == required:
                character = s[left]

                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                window_count[character] -= 1
                if character in dict_t and window_count[character] < dict_t[character]:
                    formed -= 1

                left += 1

            right += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]

print(Solution().minWindow("ADOBECODEBANC", "ABC"))
