
//#     Algorithm
//        #
//        #     Initialize a queue, Q to keep a track of all the nodes in the graph with 0 in-degree.
//        #     Iterate over all the edges in the input and create an adjacency list and also a map of node v/s in-degree.
//        #     Add all the nodes with 0 in-degree to Q.
//        #     The following steps are to be done until the Q becomes empty.
//        #     Pop a node from the Q. Let's call this node, N.
//        #     For all the neighbors of this node, N, reduce their in-degree by 1. If any of the nodes' in-degree reaches 0, add it to the Q.
//        #     Add the node N to the list maintaining topologically sorted order.
//        #     Continue from step 4.1.
class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> adjList = new HashMap<>();
        int[] indegree = new int[numCourses];
        int[] topologicalOrder = new int[numCourses];

        for (int i = 0; i < prerequisites.length; i++) {
            int dest = prerequisites[i][0];
            int src = prerequisites[i][1];
            List<Integer> lst = adjList.getOrDefault(src, new ArrayList<Integer>());
            lst.add(dest);
            adjList.put(src, lst);

            indegree[dest] += 1;
        }

        Queue<Integer> q = new LinkedList<Integer>();
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                q.add(i);
            }
        }

        int i = 0;

        while (!q.isEmpty()) {
            int node = q.remove();
            topologicalOrder[i++] = node;

            if (adjList.containsKey(node)) {
                for (Integer neighbor : adjList.get(node)) {
                    indegree[neighbor]--;

                    // If in-degree of a neighbor becomes 0, add it to the Q
                    if (indegree[neighbor] == 0) {
                        q.add(neighbor);
                    }
                }
            }
        }

        if (i == numCourses) {
            return topologicalOrder;
        }

        return new int[0];
    }
}