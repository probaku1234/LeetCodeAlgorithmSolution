"""
URL : https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/2983/
"""
from collections import defaultdict


class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)

    def add_edges(self, v, w):
        self.graph[v].append(w)

    def is_cycle_helper(self, v, visited, stack):
        visited[v] = True
        stack[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.is_cycle_helper(neighbor, visited, stack):
                    return True
            elif stack[neighbor]:
                return True

        stack[v] = False
        return False

    def is_cycle(self):
        visited = [False] * self.n
        stack = [False] * self.n

        for node in range(self.n):
            if not visited[node]:
                if self.is_cycle_helper(node, visited, stack):
                    return True

        return False


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        g = Graph(numCourses)
        for p in prerequisites:
            g.add_edges(p[1], p[0])

        return not g.is_cycle()

print(Solution().canFinish(2, [[1,0],[0,1]]))