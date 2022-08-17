class Solution {
    void dfs(char[][] grid, boolean[][] visited, int r, int c) {
        int numRow = grid.length;
        int numCol = grid[0].length;

        if (r < 0 || c < 0 || r >= numRow || c >= numCol || grid[r][c] == '0' || visited[r][c]) {
            return;
        }

        visited[r][c] = true;
        dfs(grid, visited, r-1, c);
        dfs(grid, visited, r+1, c);
        dfs(grid, visited, r, c+1);
        dfs(grid, visited, r, c-1);
    }

    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0;
        }

        int numRow = grid.length;
        int numCol = grid[0].length;
        int res = 0;
        boolean[][] visited = new boolean[numRow][numCol];

        for (int r = 0; r < numRow; r++) {
            for (int c = 0; c < numCol; c++) {
                if (grid[r][c] == '1' && !visited[r][c]) {
                    res++;
                    dfs(grid, visited,r,c);
                }

            }
        }

        return res;
    }
}