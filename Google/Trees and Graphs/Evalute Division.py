"""
URL : https://leetcode.com/explore/interview/card/google/61/trees-and-graphs/331/
"""

from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, v, u, w):
        self.graph[v].append((u, w))

    def bfs(self, v, u):
        queue = deque([[v]])
        weight_queue = deque([1.0])
        explored = []

        while queue:
            path = queue.pop()
            weight = weight_queue.pop()
            end_node = path[-1]

            if end_node not in explored:
                for neighbor in self.graph[end_node]:
                    new_path = list(path)
                    new_path.append(neighbor[0])
                    queue.append(new_path)
                    current_weight = weight * neighbor[1]
                    weight_queue.append(current_weight)
                    if neighbor[0] == u:
                        return current_weight

                explored.append(end_node)

        return -1.0


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        g = Graph()
        result = []

        for i in range(len(equations)):
            equation = equations[i]
            g.add_edge(equation[0], equation[1], values[i])
            g.add_edge(equation[1], equation[0], 1/values[i])

        for i in range(len(queries)):
            query = queries[i]
            if query[0] not in g.graph or query[1] not in g.graph:
                result.append(-1.0)
            elif query[0] == query[1]:
                result.append(1.0)
            else:
                result.append(g.bfs(query[0], query[1]))

        return result