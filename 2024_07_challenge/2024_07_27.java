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
    private long dijkstra(int[][] graph, int src, int tgt) {
        // Find the lowest cost from src to tgt
        long[] costs = new long[26];
        Arrays.fill(costs, Long.MAX_VALUE);
        costs[src] = 0;
        PriorityQueue<long[]> queue = new PriorityQueue<>((a, b) -> Long.compare(a[1], b[1])); // element = [node, accCost]
        queue.add(new long[]{src, 0});
        while (!queue.isEmpty()) {
            long[] ele = queue.poll();
            int node = (int)ele[0];
            long c = ele[1];
            if (c != costs[node])
                continue;
            if (node == tgt)
                return c;
            for (int child = 0; child < 26; child++) {
                if (graph[node][child] > 0) {
                    long accCost = c + graph[node][child];
                    if (accCost < costs[child]) {
                        costs[child] = accCost;
                        queue.add(new long[]{child, accCost});
                    }
                }
            }
        }
        return -1;
    }

    public long minimumCost(String source, String target, char[] original, char[] changed, int[] cost) {
        /*
         * LeetCode 2976
         *
         * Create a directed and weighted graph from all the letters from
         * original to changed. Then run Dijkstra to find the lowest cost to
         * go from a letter in source to an altered letter in target.
         *
         * O(N*26*26), 109 ms, faster than 19.27%
         */
        int[][] graph = new int[26][26];
        for (int i = 0; i < original.length; i++) {
            int ole = original[i] - 'a';
            int cle = changed[i] - 'a';
            if (graph[ole][cle] == 0)
                graph[ole][cle] = cost[i];
            else
                graph[ole][cle] = Math.min(graph[ole][cle], cost[i]);
        }
        long res = 0;
        long[][] cache = new long[26][26];
        for (int i = 0; i < source.length(); i++) {
            int sle = source.charAt(i) - 'a';
            int tle = target.charAt(i) - 'a';
            if (sle != tle) {
                if (cache[sle][tle] == 0)
                    cache[sle][tle] = dijkstra(graph, source.charAt(i) - 'a', target.charAt(i) - 'a');
                if (cache[sle][tle] < 0)
                    return -1;
                res += cache[sle][tle];
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
