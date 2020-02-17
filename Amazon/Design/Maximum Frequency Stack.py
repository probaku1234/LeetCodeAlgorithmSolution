"""
URL : https://leetcode.com/explore/interview/card/amazon/81/design/3001/
"""
from collections import defaultdict, Counter


class FreqStack(object):

    def __init__(self):
        self.freq = Counter()
        self.group = defaultdict(list)
        self.maxfreq = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(x)

    def pop(self):
        """
        :rtype: int
        """
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x
