import java.math.*;
import java.util.*;
import java.util.stream.Stream;

/**
 * Definition for a binary tree node.
 */
// class TreeNode {
// int val;
// TreeNode left;
// TreeNode right;
// TreeNode() {}
// TreeNode(int val) { this.val = val; }
// TreeNode(int val, TreeNode left, TreeNode right) {
// this.val = val;
// this.left = left;
// this.right = right;
// }
// }

class Solution {
    private void dfs(Map<Integer, Stack<Integer>> graph, int node,
            Stack<Integer> revPath) {
        // Use postorder traversal to ensure correct order.
        // From each node, we first visit all its possible outgoing edges.
        // It is guaranteed that each outgoing edge will eventually lead back
        // to the starting node. So the correct order can only be established
        // when all the outgoing edges are visited.
        // The path we record is a reverse-path
        Stack<Integer> children = graph.getOrDefault(node, new Stack<>());
        while (!children.isEmpty()) {
            dfs(graph, children.pop(), revPath);
        }
        revPath.add(node);
    }

    public int[][] validArrangement(int[][] pairs) {
        /*
         * LeetCode 2097 (Fail)
         *
         * Although I was not able to solve it by myself, it did require some
         * knowledge, in particular, Eulerian's path. I did realize that the
         * problem is a graph, but there are two key pieces that I was able to
         * intuit.
         *
         * 1. Treat each number in the pair as a node. Thus the pair itself
         * becomes a directed edge. The rule of Eulerian's path is to traverse
         * a connected graph by visiting each edge exactly once, while allowing
         * visiting the same nodes multiple times.
         * 2. For a connected graph to have an Eulerian path, there must be
         * exactly two nodes with odd degrees or all the nodes with even degrees
         * If two nodes have odd degrees, one of them must be the starting
         * point. If all the nodes have even degrees, then we have an Eulerian
         * circuit, which means any node can serve as the starting point.
         *
         * Then the problem becomes a DFS with postorder traversal to visit
         * all the edges in the correct order and NOT TLE.
         *
         * O(E + V + E)
         */
        Map<Integer, Stack<Integer>> graph = new HashMap<>();
        Map<Integer, Integer> degrees = new HashMap<>();
        for (int[] edge : pairs) {
            graph.putIfAbsent(edge[0], new Stack<>());
            graph.get(edge[0]).add(edge[1]);
            degrees.put(edge[0], degrees.getOrDefault(edge[0], 0) + 1);
            degrees.put(edge[1], degrees.getOrDefault(edge[1], 0) + 1);
        }
        int node1 = -1;
        int node2 = -1;
        for (int k : degrees.keySet()) {
            if (degrees.get(k) % 2 == 1) {
                if (node1 < 0)
                    node1 = k;
                else if (node2 < 0)
                    node2 = k;
                else
                    break;
            }
        }
        Stack<Integer> revPath = new Stack<>();
        if (node1 < 0 || node2 < 0) {
            // we have an Eulerian circuit, which means we can start from any
            // node as the root
            dfs(graph, pairs[0][0], revPath);
        } else {
            // starting point must have one more outgoing than incoming
            if (graph.getOrDefault(node1, new Stack<>()).size() * 2 > degrees.get(node1))
                dfs(graph, node1, revPath);
            else
                dfs(graph, node2, revPath);
        }
        int[][] res = new int[pairs.length][2];
        for (int i = 0; i < pairs.length; i++)
            res[i] = new int[] { revPath.pop(), revPath.peek() };
        return res;
    }
}

class Main {
    public static void main(String[] args) {
        String s = "acbbaca";
        String t = "aba";
        Solution sol = new Solution();
        System.out.println(sol.minWindow(s, t));
    }
}
