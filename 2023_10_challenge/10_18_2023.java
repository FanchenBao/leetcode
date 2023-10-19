class Solution {
    public int minimumTime(int n, int[][] relations, int[] time) {
        /*
        LeetCode 2050 (Fail)

        We are close. I know it is topological sort to start from the nodes with zero indegrees. I also know that
        for all the nodes at the same indegree level, the time it takes should go with the node that takes the max
        amount of time.

        However, what I was going for was to find out how much extra time a child node can have based on the situation
        of the current level. Unfortunately, this method cannot handle complex relations. It is just too complicated
        to figure out the extract extra time a child can have based on some previous levels.

        The official solution offers a different view of the problem. We still start from nodes with zero indegree.
        Then we can monitor the latest time needed to reach any node of next level. This determines the earliest time
        that the node of next level can start execution. Thus, if we keep track of the earliest time that a node can
        start executing, we will be able to cascade this computation for the next node and the next next node. In the
        end, we will have the earliest time needed to execute any node in the graph. Then the answer is the max value
        of such earliest time plus the time needed to execute the node.

        O(V + E), 19 ms, faster than 80.89%
         */
        int[] indegrees = new int[n];
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        for (int[] tup : relations) {
            int pre = tup[0]; int nex = tup[1];
            indegrees[nex - 1]++;
            graph.get(pre - 1).add(nex - 1);
        }
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (indegrees[i] == 0) queue.add(i);
        }
        int[] ticks = new int[n]; // ticks[i] is the earliest time when node i is taken
        while (!queue.isEmpty()) {
            int node = queue.poll();
            for (int child : graph.get(node)) {
                indegrees[child]--;
                // the earliest time that a child can be executed is the latest time that one of its parents finishes
                ticks[child] = Math.max(ticks[child], ticks[node] + time[node]);
                if (indegrees[child] == 0) {
                    queue.add(child);
                }
            }
        }
        int res = 0;
        for (int i = 0; i < n; i++) res = Math.max(res, ticks[i] + time[i]);
        return res;
    }
}


class Solution {
    Integer[] dp; // dp[i] is the min time needed to finish all the classes startin from node i
    List<List<Integer>> graph = new ArrayList<>();
    int[] time;

    private int dfs(int node) {
        if (dp[node] != null) return dp[node];
        dp[node] = time[node];
        if (graph.get(node).isEmpty()) return dp[node];
        int nextTime = 0;
        for (int child : graph.get(node)) {
            nextTime = Math.max(nextTime, dfs(child));
        }
        dp[node] += nextTime;
        return dp[node];
    }

    public int minimumTime(int n, int[][] relations, int[] time) {
        /*
        The DFS + DP solution. We define dfs(node) to return the min time needed to finish all the classes starting
        from node. We go through all the nodes and the max of all the dfs(node) is the answer. No need to do topological
        sort.

        O(V + E), 19 ms, faster than 80.89%
         */

        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        for (int[] tup : relations) {
            graph.get(tup[0] - 1).add(tup[1] - 1);
        }
        dp = new Integer[n];
        this.time = time;
        int res = 0;
        for (int i = 0; i < n; i++) res = Math.max(res, dfs(i));
        return res;
    }
}
