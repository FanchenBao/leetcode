import java.util.*;
import java.util.stream.Stream;

import com.sun.tools.javac.resources.legacy;

import java.math.*;

/**
 * Definition for a binary tree node.
 */
//class TreeNode {
//    int val;
//    TreeNode left;
//    TreeNode right;
//    TreeNode() {}
//    TreeNode(int val) { this.val = val; }
//    TreeNode(int val, TreeNode left, TreeNode right) {
//        this.val = val;
//        this.left = left;
//        this.right = right;
//    }
//}

class Solution1 {
    private int shortestDist(Map<Integer, List<Integer>> graph, int tgt) {
        Deque<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{0, 0});
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int city = cur[0];
            int dist = cur[1];
            if (city == tgt)
                return dist;
            for (int next : graph.get(city))
                queue.add(new int[]{next, dist + 1});
        }
        return -1; // should not reach here.
    }

    public int[] shortestDistanceAfterQueries(int n, int[][] queries) {
        /*
         * LeetCode 3243
         *
         * This is the naive solution where we perform a new BFS each time a
         * new road is added to the graph.
         *
         * O(MN)
         */
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < n - 1; i++) {
            graph.put(i, new ArrayList<>());
            graph.get(i).add(i + 1);
        }
        int[] res = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            graph.get(queries[i][0]).add(queries[i][1]);
            res[i] = shortestDist(graph, n - 1);
        }
        return res;
    }
}


class Solution2 {
    private void update(int[] dp, int st, int ed, Map<Integer, List<Integer>> parents) {
        // a new path is created from st to ed, update dp array for st and all
        // the nodes that are parents to st.
        if (dp[ed] + 1 < dp[st]) {
            dp[st] = dp[ed] + 1;
            for (int par : parents.getOrDefault(st, Collections.emptyList()))
                update(dp, par, st, parents);
        }
    }

    public int[] shortestDistanceAfterQueries(int n, int[][] queries) {
        /*
         * We use a dp array to keep track of the shortest distance from i to
         * n - 1. Each time a new path is provided, the only nodes whose
         * shortest distance need to be updated are the ones to the left of
         * queries[j][0]. This update should be faster than running BFS for
         * each query because we are not going through the entire n.
         *
         * O(MN), 14 ms, faster than 99.03%
         */
        int[] dp = new int[n]; // dp[i] = min dist from i to n - 1
        Map<Integer, List<Integer>> parents = new HashMap<>();
        for (int i = 0; i < n; i++) {
            dp[i] = n - 1 - i;
            if (i > 0) {
                parents.put(i, new ArrayList<>());
                parents.get(i).add(i - 1);
            }
        }
        int[] res = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int u = queries[i][0];
            int v = queries[i][1];
            parents.get(v).add(u);
            update(dp, u, v, parents);
            res[i] = dp[0];
        }
        return res;
    }
}

class Solution3 {
    private int shortestDist(Map<Integer, List<Integer>> graph, int tgt, int n) {
        Deque<int[]> queue = new ArrayDeque<>();
        boolean[] seen = new boolean[n]; // use this to speed things up. If a node has been seen already, do not visit it again
        queue.add(new int[]{0, 0});
        seen[0] = true;
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int city = cur[0];
            int dist = cur[1];
            if (city == tgt)
                return dist;
            for (int next : graph.get(city)) {
                if (!seen[next]) {
                    queue.add(new int[]{next, dist + 1});
                    seen[next] = true;
                }
            }
        }
        return -1; // should not reach here.
    }

    public int[] shortestDistanceAfterQueries(int n, int[][] queries) {
        /*
         * LeetCode 3243
         *
         * This is the naive solution where we perform a new BFS each time a
         * new road is added to the graph.
         *
         * Note that we use a seen array in the BFS to speed things up (how
         * I did not see this before is quite embarassing).
         *
         * O(MN), 108 ms, faster than 71.01%
         */
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < n - 1; i++) {
            graph.put(i, new ArrayList<>());
            graph.get(i).add(i + 1);
        }
        int[] res = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            graph.get(queries[i][0]).add(queries[i][1]);
            res[i] = shortestDist(graph, n - 1, n);
        }
        return res;
    }
}




class Main{
    public static void main(String[] args) {
        String s = "acbbaca";
        String t = "aba";
        Solution sol = new Solution();
        System.out.println(sol.minWindow(s, t));
    }
}
