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
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        /*
         * LeetCode 1971
         *
         * Just a BFS, but very verbose.
         *
         * O(V + E), 126 ms, faster than 43.45% 
         */
        boolean[] visited = new boolean[n];
        Map<Integer, List<Integer>> graph = new HashMap();
        for (int[] e : edges) {
            if (!graph.containsKey(e[0]))
                graph.put(e[0], new ArrayList<>());
            graph.get(e[0]).add(e[1]);
            if (!graph.containsKey(e[1]))
                graph.put(e[1], new ArrayList<>());
            graph.get(e[1]).add(e[0]);
        }
        Deque<Integer> queue = new ArrayDeque<>();
        queue.addLast(source);
        visited[source] = true;
        while (!queue.isEmpty()) {
            int cur = queue.removeFirst();
            if (cur == destination)
                return true;
            for (int child : graph.getOrDefault(cur, Collections.emptyList())) {
                if (!visited[child]) {
                    visited[child] = true;
                    queue.addLast(child);
                }
            }
        }
        return false;
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
