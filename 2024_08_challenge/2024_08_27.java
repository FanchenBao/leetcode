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
    public double maxProbability(int n, int[][] edges, double[] succProb, int start_node, int end_node) {
        /*
         * LeetCode 1514
         *
         * Standard Dijkstra, but using a max heap for finding the max product
         * of all probabilities.
         *
         * O(VlogV + E), 57 ms, faster than 23.15%
         */
        double epsilon = 0.00001;
        Map<Integer, List<double[]>> graph = new HashMap<>(); // [succProb, node]
        for (int i = 0; i < edges.length; i++) {
            int[] edge = edges[i];
            graph.putIfAbsent(edge[0], new ArrayList<>());
            graph.putIfAbsent(edge[1], new ArrayList<>());
            graph.get(edge[0]).add(new double[]{succProb[i], edge[1]});
            graph.get(edge[1]).add(new double[]{succProb[i], edge[0]});
        }
        // Dijkstra
        PriorityQueue<double[]> queue = new PriorityQueue<>((a, b) -> Double.compare(-a[0], -b[0]));
        double[] probs = new double[n];
        probs[start_node] = 1.0;
        queue.add(new double[]{1.0, start_node});
        while (!queue.isEmpty()) {
            double[] cur = queue.poll();
            double curProb = cur[0];
            int curNode = (int)cur[1];
            if (Math.abs(curProb - probs[curNode]) > epsilon) {
                continue;
            }
            for (double[] probNode : graph.getOrDefault(curNode, Collections.emptyList())) {
                double p = probNode[0];
                int child = (int)probNode[1];
                double tmpProb = curProb * p;
                if (tmpProb - probs[child] > epsilon) {
                    probs[child] = tmpProb;
                    queue.add(new double[]{tmpProb, child});
                }
            }
        }
        return probs[end_node];
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
