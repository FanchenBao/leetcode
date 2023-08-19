class Solution1 {
    public int maximalNetworkRank(int n, int[][] roads) {
        /*
        LeetCode 1615

        This is not a difficult problem. All we need to do is to count the number of edges associated with
        each node. Then pick the nodes with the highest edges and find all the possible pairs. If a pair exists
        that does not share an edge, that pair will give us the max rank. Of course, when checking the pairs,
        we must first check all the pairs within the max number of edges. If there are no pairs in max number
        of edges, we go for the second max number of edges.

        However, Java really slowed me down.

        O(N^2 + M), where M = roads.length, 6 ms, faster than 61.14%
         */
        int[][] edges = new int[n][n];
        int[] edgeCounts = new int[n];
        for (int[] e : roads) {
            edges[e[0]][e[1]] = 1;
            edges[e[1]][e[0]] = 1;
            edgeCounts[e[0]] += 1;
            edgeCounts[e[1]] += 1;
        }
        HashMap<Integer, ArrayList<Integer>> countOfEdges = new HashMap<>();
        for (int v = 0; v < n; v++) {
            countOfEdges.computeIfAbsent(edgeCounts[v], k -> new ArrayList<>()).add(v);
        }
        Integer[] sortedCounts = countOfEdges.keySet().toArray(new Integer[0]);
        Arrays.sort(sortedCounts, Comparator.reverseOrder());
        int res;
        if (countOfEdges.get(sortedCounts[0]).size() > 1) {
            res = 2 * sortedCounts[0];
            for (int a : countOfEdges.get(sortedCounts[0])) {
                for (int b: countOfEdges.get(sortedCounts[0])) {
                    if (a != b && edges[a][b] == 0) {
                        return res;
                    }
                }
            }
            return res - 1;
        }
        // only one node has max number of edge counts
        res = sortedCounts[0] + sortedCounts[1];
        for (int b: countOfEdges.get(sortedCounts[1])) {
            if (edges[countOfEdges.get(sortedCounts[0]).get(0)][b] == 0) {
                return res;
            }
        }
        return res - 1;
    }
}


class Solution2 {
    public int maximalNetworkRank(int n, int[][] roads) {
        /*
        The official solution just creates an adjacency list and iterate through all pairs. Kind of dumb
        but there is a lot less overhead.

        NOPE, this is slower, which is expected. Again, this shows that in Java, the overhead of a slightly
        more complex algo is not that big. In other words, a better thoughtout algo shall perform better.

        O(V^2 + E), 28 ms, faster than 39.36%
         */
        HashMap<Integer, Set<Integer>> graph = new HashMap<>();
        for (int[] e : roads) {
            graph.computeIfAbsent(e[0], k -> new HashSet<>()).add(e[1]);
            graph.computeIfAbsent(e[1], k -> new HashSet<>()).add(e[0]);
        }
        int res = 0;
        for (int a = 0; a < n; a++) {
            for (int b = a + 1; b < n; b++) {
                int rank = graph.getOrDefault(a, Collections.emptySet()).size() + graph.getOrDefault(b, Collections.emptySet()).size();
                if (graph.getOrDefault(a, Collections.emptySet()).contains(b)) {
                    rank--;
                }
                res = Math.max(res, rank);
            }
        }
        return res;
    }
}
