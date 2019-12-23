"""
URL : https://leetcode.com/explore/interview/card/google/59/array-and-strings/3054/
"""
from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 1:
            return 0

        ans = 0
        alpha_set = []
        current_alpha = None
        current_alpha_index = -1
        left, right = 0, 0

        while right < len(s):
            character = s[right]

            if len(alpha_set) < 2:
                if character not in alpha_set:
                    alpha_set.append(character)
            else:
                if character not in alpha_set:
                    alpha_set = list(filter(lambda c: c == current_alpha, alpha_set))
                    alpha_set.append(character)
                    left = current_alpha_index

            if len(alpha_set) <= 2:
                ans = max(ans, right - left + 1)

            if character != current_alpha:
                current_alpha = character
                current_alpha_index = right

            right += 1

        return ans

    def lengthOfLongestSubstringTwoDistinct(self, s):
        n = len(s)
        if n < 3:
            return n

        # sliding window left and right pointers
        left, right = 0, 0
        # hashmap character -> its rightmost position
        # in the sliding window
        hashmap = defaultdict()

        max_len = 2

        while right < n:
            # slidewindow contains less than 3 characters
            if len(hashmap) < 3:
                hashmap[s[right]] = right
                right += 1

            # slidewindow contains 3 characters
            if len(hashmap) == 3:
                # delete the leftmost character
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                # move left pointer of the slidewindow
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len