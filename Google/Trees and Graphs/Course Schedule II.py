"""
URL : https://leetcode.com/explore/interview/card/google/61/trees-and-graphs/3070/
"""

from collections import defaultdict, deque


class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)

    def add_edges(self, v, w):
        self.graph[v].append(w)

#     Algorithm
#
#     Initialize a queue, Q to keep a track of all the nodes in the graph with 0 in-degree.
#     Iterate over all the edges in the input and create an adjacency list and also a map of node v/s in-degree.
#     Add all the nodes with 0 in-degree to Q.
#     The following steps are to be done until the Q becomes empty.
#     Pop a node from the Q. Let's call this node, N.
#     For all the neighbors of this node, N, reduce their in-degree by 1. If any of the nodes' in-degree reaches 0, add it to the Q.
#     Add the node N to the list maintaining topologically sorted order.
#     Continue from step 4.1.
    def topological_order_non_recursive(self):
        queue = deque([])
        in_degree = [0] * self.n

        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1

        # Create an queue and enqueue all vertices with
        # indegree 0
        for i in range(self.n):
            if in_degree[i] == 0:
                queue.append(i)

        count = 0
        top_order = []

        # One by one dequeue vertices from queue and enqueue
        # adjacents if indegree of adjacent becomes 0
        while queue:
            # Extract front of queue (or perform dequeue)
            # and add it to topological order
            u = queue.popleft()
            top_order.append(u)

            # Iterate through all neighbouring nodes
            # of dequeued node u and decrease their in-degree
            # by 1
            for i in self.graph[u]:
                in_degree[i] -= 1
                # If in-degree becomes zero, add it to queue
                if in_degree[i] == 0:
                    queue.append(i)

            count += 1

        return top_order if count == self.n else []

    def topological_order_recursive(self):
        topological_sorted_order = []
        is_possible = True

        color = { k : 1 for k in range(self.n)}
        def dfs(node):
            nonlocal is_possible

            if not is_possible:
                return

            color[node] = 2

            if node in self.graph:
                for neighbor in self.graph[node]:
                    if color[neighbor] == 1:
                        dfs(neighbor)
                    elif color[neighbor] == 2:
                        is_possible = False
            color[node] = 3
            topological_sorted_order.append(node)

        for vertex in range(self.n):
            if color[vertex] == 1:
                dfs(vertex)

        return topological_sorted_order[::-1] if is_possible else []

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        g = Graph(numCourses)

        for prerequisite in prerequisites:
            g.add_edges(prerequisite[1], prerequisite[0])

        #result = g.dfs()
        print(g.topological_order_non_recursive())
        return g.topological_order_recursive()


print(Solution().findOrder(3, [[1, 0], [2, 1], [0, 2]]))
print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
