import java.util.*;
import java.util.stream.Stream;
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

class Solution {
    private void dfs(Map<Integer, List<int[]>> graph, int node, int[] dists, int weights, int distanceThreshold) {
        for (int[] cw : graph.getOrDefault(node, Collections.emptyList())) {
            weights += cw[1];
            if (dists[cw[0]] > weights && weights <= distanceThreshold) {
                dists[cw[0]] = weights;
                dfs(graph, cw[0], dists, weights, distanceThreshold);
            }
            weights -= cw[1];
        }
    }

    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        /*
         * LeetCode 1334
         *
         * DFS to find the number of cities within the distanceThreshold. Since
         * n is small, we can run DFS with each node as root.
         *
         * O(N^2), 244 ms, faster than 5.23%
         */
        Map<Integer, List<int[]>> graph = new HashMap<>();
        int MAX = Integer.MAX_VALUE;
        for (int[] e : edges) {
            graph.putIfAbsent(e[0], new ArrayList<>());
            graph.putIfAbsent(e[1], new ArrayList<>());
            graph.get(e[0]).add(new int[]{e[1], e[2]});
            graph.get(e[1]).add(new int[]{e[0], e[2]});
        }
        int min = MAX;
        int res = 0;
        int[] dists = new int[n];
        for (int root = 0; root < n; root++) {
            Arrays.fill(dists, MAX);
            dists[root] = 0;
            dfs(graph, root, dists, 0, distanceThreshold);
            int cnt = 0;
            for (int d : dists)
                cnt += d < MAX ? 1 : 0;
            if (cnt <= min) {
                min = cnt;
                res = root;
            }
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
