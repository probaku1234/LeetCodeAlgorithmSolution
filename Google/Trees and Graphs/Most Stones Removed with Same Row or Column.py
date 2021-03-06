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
    def __init__(self, N):
        self.parents = list(range(N))

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.parents[xr] = yr


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

    def removeStonesWithDSU(self, stones):
        N = len(stones)
        dsu = DSU(20000)
        for x, y in stones:
            dsu.union(x, y + 10000)

        return N - len({dsu.find(x) for x, y in stones})

Solution().removeStonesWithDSU([[0,0],[0,2],[1,1],[2,0],[2,2]])

