graph is undirected
        nodes are the given stone locations
        connections/edges exist if two stone locations are on the same row or same col
        max removed stones = total number of stones - number of connected components

class Solution {
    public int removeStones(int[][] stones) {
        List<Integer>[] graph = new ArrayList[stones.length];
        for (int i = 0; i < stones.length; i++) {
            for (int j = i + 1; j < stones.length; j++) {
                int[] stone1 = stones[i];
                int[] stone2 = stones[j];

                if (stone1[0] == stone2[0] || stone1[1] == stone2[1]) {
                    if (graph[i] == null) graph[i] = new ArrayList<>();
                    if (graph[j] == null) graph[j] = new ArrayList<>();
                    graph[i].add(j);
                    graph[j].add(i);
                }
            }
        }

        int islands = 0;
        boolean[] visited = new boolean[stones.length];
        for (int i = 0; i < stones.length; i++) {
            islands += dfs(i, graph, visited);
        }
        return stones.length - islands;
    }

    private int dfs(int i, List<Integer>[] graph, boolean[] visited) {
        if (visited[i]) return 0;
        visited[i] = true;
        if (graph[i] != null) {
            for (int n : graph[i]) {
                dfs(n, graph, visited);
            }
        }
        return 1;
    }
}