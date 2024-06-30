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
    public List<List<Integer>> getAncestors(int n, int[][] edges) {
        /*
         * LeetCode 2192
         *
         * Topological sort by taking the nodes with the min indegree. As we
         * visit these nodes, we can populate all of its ancestors via its
         * direct parents because the parents' ancestors have been determined
         * already.
         *
         * After handling the current node's ancestors, we put it in its
         * children's ancestor list and reduce its children's indegree. We
         * enqueue the children whose indegree has decreased to zero.
         *
         * O(N^2), 76 ms, faster than 64.38%
         */
        Map<Integer, List<Integer>> graph = new HashMap<>();
        int[] indegree = new int[n];
        for (int[] e : edges) {
            graph.putIfAbsent(e[0], new ArrayList<>());
            graph.get(e[0]).add(e[1]);
            indegree[e[1]]++;
        }

        Deque<Integer> queue = new ArrayDeque<>();
        List<List<Integer>> res = new ArrayList<>();
        for (int v = 0; v < n; v++) {
            res.add(new ArrayList<>());
            if (indegree[v] == 0)
                queue.add(v);
        }

        while (!queue.isEmpty()) {
            int cur = queue.removeFirst();
            // obtain all the ancestors of the current node
            Set<Integer> anc = new HashSet<>(res.get(cur));
            for (int p : res.get(cur))
                anc.addAll(res.get(p));
            res.set(cur, new ArrayList<>(anc));
            Collections.sort(res.get(cur));
            // Put current node in its children's ancestor list
            for (int child : graph.getOrDefault(cur, Collections.emptyList())) {
                res.get(child).add(cur);
                indegree[child]--;
                if (indegree[child] == 0)
                    queue.add(child);
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
