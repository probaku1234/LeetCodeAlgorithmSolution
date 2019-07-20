"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/792/
"""


class Graph:
    def __init__(self, row, col, grid):
        self.row = row
        self.col = col
        self.grid = grid

    def isSafe(self, i, j, visited):
        return 0 <= i < self.row and 0 <= j < self.col and not visited[i][j] and self.grid[i][j] == "1"

    def DFS(self, i, j, visited):
        row_neighbor_index_list = [-1, 0, 0, 1]
        col_neighbor_index_list = [0, -1, 1, 0]

        visited[i][j] = True

        for k in range(4):
            if self.isSafe(i + row_neighbor_index_list[k], j + col_neighbor_index_list[k], visited):
                self.DFS(i + row_neighbor_index_list[k], j + col_neighbor_index_list[k], visited)


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None or len(grid) == 0:
            return 0

        count = 0
        row_num = len(grid)
        col_num = len(grid[0])
        visited = [[False for j in range(col_num)] for i in range(row_num)]
        graph = Graph(row_num, col_num, grid)

        for i in range(row_num):
            for j in range(col_num):
                if visited[i][j] is False and grid[i][j] == "1":
                    graph.DFS(i, j, visited)
                    count += 1

        return count
