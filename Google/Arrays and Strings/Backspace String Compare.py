"""
URL : https://leetcode.com/explore/interview/card/google/59/array-and-strings/3060/
"""
import itertools


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        i = len(S) - 1
        j = len(T) - 1
        s_skip = 0
        t_skip = 0

    def backspaceCompare2(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        # The all() method returns True when all elements in the given iterable are true. If not, it returns False.
        # Make an iterator that aggregates elements from each of the iterables. If the iterables are of uneven length,
        # missing values are filled-in with fillvalue.
        # Iteration continues until the longest iterable is exhausted.
        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))


print(Solution().backspaceCompare2('aa#b#','a'))
print(Solution().backspaceCompare2('b#c#','a#'))
print(Solution().backspaceCompare2('ab##','a#'))