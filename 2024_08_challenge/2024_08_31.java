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
         * We did this problem four days ago!
         *
         * O((E + V)logV), 62 ms, faster than 10.12%
         */
        double epsilon = 0.00001;
        Map<Integer, List<double[]>> graph = new HashMap<>();
        for (int i = 0; i < edges.length; i++) {
            int[] edge = edges[i];
            graph.putIfAbsent(edge[0], new ArrayList<>());
            graph.putIfAbsent(edge[1], new ArrayList<>());
            graph.get(edge[0]).add(new double[]{succProb[i], edge[1]});
            graph.get(edge[1]).add(new double[]{succProb[i], edge[0]});
        }
        PriorityQueue<double[]> queue = new PriorityQueue<>((a, b) -> Double.compare(b[0], a[0]));
        double[] probs = new double[n];
        probs[start_node] = 1.0;
        queue.add(new double[]{1.0, start_node});
        while (!queue.isEmpty()) {
            double[] tmp = queue.poll();
            int node = (int)tmp[1];
            double p = tmp[0];
            if (Math.abs(p - probs[node]) > epsilon)
                continue;
            for (double[] e : graph.getOrDefault(node, Collections.emptyList())) {
                int child = (int)e[1];
                double pp = e[0];
                if (pp * p > probs[child]) {
                    probs[child] = pp * p;
                    queue.add(new double[]{probs[child], child});
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
