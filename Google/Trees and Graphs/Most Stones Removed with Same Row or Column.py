"""
URL : https://leetcode.com/explore/interview/card/google/61/trees-and-graphs/3076/
"""
from collections import defaultdict, deque


class Graph:
    def __init__(self, n):
        self.N = n
        self.graph = defaultdict(list)

    def add_edge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def count_size_of_components(self):
        ans = 0
        seen = [False] * self.N
        for i in range(self.N):
            if not seen[i]:
                stack = [i]
                seen[i] = True
                while stack:
                    ans += 1
                    node = stack.pop()
                    for neighbor in self.graph[node]:
                        if not seen[neighbor]:
                            stack.append(neighbor)
                            seen[neighbor] = True
                ans -= 1
        return ans


class DSU:
    def __init__(self):
        self.parents = list(range(1001))
        self.rank = [0] * 1001

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rank[xr] < self.rank[yr]:
            self.parents[xr] = yr
        elif self.rank[xr] > self.rank[yr]:
            self.parents[yr] = xr
        else:
            self.parents[yr] = xr
            self.rank[xr] += 1
        return True


class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        if len(stones) == 0 or len(stones) == 1:
            return 0

        g = Graph(len(stones))
        for i, x in enumerate(stones):
            for j in range(i):
                y = stones[j]
                if x[0] == y[0] or x[1] == y[1]:
                    g.add_edge(i, j)
                    g.add_edge(j, i)

        return g.count_size_of_components()


