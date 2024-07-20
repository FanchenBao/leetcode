import java.util.*;
import java.util.stream.Stream;

import java.math.*;

/**
 * Definition for a binary tree node.
 */
class TreeNode {
   int val;
   TreeNode left;
   TreeNode right;
   TreeNode() {}
   TreeNode(int val) { this.val = val; }
   TreeNode(int val, TreeNode left, TreeNode right) {
       this.val = val;
       this.left = left;
       this.right = right;
   }
}


class Solution1 {
    Map<TreeNode, List<TreeNode>> leafPaths = new HashMap<>();

    private void dfs(TreeNode node, List<TreeNode> path) {
        if (node == null)
            return;
        path.add(node);
        if (node.left == null && node.right == null) {
            // a leaf
            this.leafPaths.put(node, new ArrayList<>(path));
        } else {
            dfs(node.left, path);
            dfs(node.right, path);
        }
        path.remove(path.size() - 1);
    }

    public int countPairs(TreeNode root, int distance) {
        /*
         * LeetCode 1530
         *
         * We find the path from root to all the leaves and save them in a
         * hashmap. Then we go through all pairs of leaves, use their paths
         * to find the lowest common ancestor, and then compute their min
         * distance. After that the solution is self-explanatory.
         *
         * O(N + N^2logN), 214 ms, faster than 5.08%
         */
        dfs(root, new ArrayList<>());
        List<TreeNode> leaves = new ArrayList<>(this.leafPaths.keySet());
        int res = 0;
        for (int i = 0; i < leaves.size(); i++) {
            for (int j = i + 1; j < leaves.size(); j++) {
                int k = 0;
                List<TreeNode> p1 = this.leafPaths.get(leaves.get(i));
                List<TreeNode> p2 = this.leafPaths.get(leaves.get(j));
                while (k < p1.size() && k < p2.size() && p1.get(k) == p2.get(k))
                    k++;
                if (p1.size() - k + p2.size() - k <= distance)
                    res++;
            }
        }
        return res;
    }
}


class Solution2 {
    int res = 0;
    int distance;

    private Map<Integer, Integer> dfs(TreeNode node) {
        Map<Integer, Integer> counter = new HashMap<>();
        if (node == null)
            return counter;
        Map<Integer, Integer> lc = dfs(node.left);
        Map<Integer, Integer> rc = dfs(node.right);
        for (int lk : lc.keySet()) {
            for (int rk : rc.keySet()) {
                if (lk + 1 + rk + 1 <= this.distance)
                    res += lc.get(lk) * rc.get(rk);
            }
        }
        for (int lk : lc.keySet())
            counter.put(lk + 1, counter.getOrDefault(lk + 1, 0) + lc.get(lk));
        for (int rk : rc.keySet())
            counter.put(rk + 1, counter.getOrDefault(rk + 1, 0) + rc.get(rk));
        if (node.left == null && node.right == null) // leaf
            counter.put(0, 1);
        return counter;
    }

    public int countPairs(TreeNode root, int distance) {
        /*
         * This is another solution because solution1 is too bad and too slow.
         * This solution will DFS the tree and for each node, it will acquire
         * a counter of all the distances from the node to its leaves. Then
         * we will iterate across the two counters from left and right subtree
         * and identify the number of leave pairs whose distance follows the
         * requirement.
         *
         * 13 ms, faster than 47.46%
         * O(N * D^2), where D is total possibilities of distances. Since the
         * problem has set D to be no more than 10, this solution is much much
         * faster than Solution1.
         */
        this.distance = distance;
        dfs(root);
        return this.res;
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
