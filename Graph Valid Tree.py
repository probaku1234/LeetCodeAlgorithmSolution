"""
URL : https://leetcode.com/problems/graph-valid-tree/description/
"""
from collections import defaultdict


"""
undirected graph is tree if
1. no cycle
2. graph is connected
"""


class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)

    def add_edges(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def is_cycle(self, v, visited, parent):
        visited[v] = True

        for i in self.graph[v]:
            # If an adjacent is not visited,
            # then recur for that adjacent
            if not visited[i]:
                if self.is_cycle(i, visited, v):
                    return True
            # If an adjacent is visited and not
            # parent of current vertex, then there
            # is a cycle.
            elif i != parent:
                return True

        return False

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        graph = Graph(n)

        for edge in edges:
            graph.add_edges(edge[0], edge[1])

        visited = [False] * n

        if graph.is_cycle(0, visited, -1):
            return False

        for i in range(n):
            if not visited[i]:
                return False

        return True


print(Solution().validTree(5, [[0,1], [0,2], [0,3], [1,4]]))