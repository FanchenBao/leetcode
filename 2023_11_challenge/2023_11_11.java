class Graph {
    /*
    LeetCode 2642

    Use Dijkstra for each shortestPath call.
    
    94 ms, faster than 78.70% 
    */
     List<List<int[]>> graph = new ArrayList<>();
     int n;

    public Graph(int n, int[][] edges) {
        // O(N)
        this.n = n;
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        for (int[] tmp : edges) graph.get(tmp[0]).add(new int[]{tmp[1], tmp[2]});
    }
    
    public void addEdge(int[] edge) {
        // O(1)
        graph.get(edge[0]).add(new int[]{edge[1], edge[2]});
    }
    
    public int shortestPath(int node1, int node2) {
        // O(ElogV)
        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(tup -> tup[1]));
        int[] minPath = new int[n];
        for (int i = 0; i < n; i++) minPath[i] = Integer.MAX_VALUE;
        minPath[node1] = 0;
        heap.add(new int[]{node1, 0});
        int[] nodeCost;
        while (!heap.isEmpty()) {
            nodeCost = heap.poll();
            if (nodeCost[1] > minPath[nodeCost[0]])
                continue;
            if (nodeCost[0] == node2)
                return nodeCost[1];
            for (int[] childCost : graph.get(nodeCost[0])) {
                if (childCost[1] + nodeCost[1] < minPath[childCost[0]]) {
                    minPath[childCost[0]] = childCost[1] + nodeCost[1];
                    heap.add(new int[]{childCost[0], minPath[childCost[0]]});
                }
            }
        }
        return -1;
    }
}

/**
 * Your Graph object will be instantiated and called as such:
 * Graph obj = new Graph(n, edges);
 * obj.addEdge(edge);
 * int param_2 = obj.shortestPath(node1,node2);
 */


 class Graph {
     /*
     Use the Floyd-Warshall algorithm, according to the second official solution.
     
     75 ms, faster than 91.67%
     */
     int[][] adj;
     int n;
     int MAX = (int)1e9;

    public Graph(int n, int[][] edges) {
        // O(N^3)
        adj = new int[n][n];
        this.n = n;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                adj[i][j] = MAX;
        for (int[] e : edges) adj[e[0]][e[1]] = e[2];
        for (int i = 0; i < n; i++) adj[i][i] = 0;
        // Use Floyd-Warshall to find the min cost from i to j going through an
        // intermediate k
        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    adj[i][j] = Math.min(adj[i][j], adj[i][k] + adj[k][j]);
    }
    
    public void addEdge(int[] edge) {
        // O(N^2)
        // Ise Floyd-Warshall to update any node pair whose path cost can be reduced by
        // including the newly added edge
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                adj[i][j] = Math.min(adj[i][j], adj[i][edge[0]] + edge[2] + adj[edge[1]][j]);
    }
    
    public int shortestPath(int node1, int node2) {
        // O(1)
        return adj[node1][node2] < MAX ? adj[node1][node2] : -1;
    }
}
