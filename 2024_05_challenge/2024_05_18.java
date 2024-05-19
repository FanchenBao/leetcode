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
    private void treeToMap(TreeNode node, int idx, Map<Integer, Integer> numConn, Map<Integer, Integer> coins) {
        if (node == null)
            return;
        coins.put(idx, node.val);
        numConn.putIfAbsent(idx, 1);
        int lc = 2 * idx;
        int rc = 2 * idx + 1;
        if (node.left != null) {
            numConn.put(idx, numConn.get(idx) + 1);
            treeToMap(node.left, lc, numConn, coins);
        }
        if (node.right != null) {
            numConn.put(idx, numConn.get(idx) + 1);
            treeToMap(node.right, rc, numConn, coins);
        }
    }

    public int distributeCoins(TreeNode root) {
        /*
         * LeetCode 979
         *
         * Turn the tree into a map, then do topological sort from leaf.
         * To make each leaf node has one coin, we push the request to its
         * parent. The request can be positive if the leaf contains more than
         * one coin, or negative otherwise. The absolute value of the request
         * is the minimum steps needed to distribute the coins to the leaf
         * node. We progress this process until all the nodes are taken care
         * of.
         *
         * O(N), 7 ms, faster than 100.00%
         */
        // record the number of connections of each node, and turn the tree
        // into a map
        Map<Integer, Integer> numConn = new HashMap<>();
        Map<Integer, Integer> coins = new HashMap<>();
        treeToMap(root, 1, numConn, coins);
        numConn.put(1, numConn.get(1) - 1); // root does not have parent
        // Topological sort
        Deque<Integer> queue = new ArrayDeque<>();
        for (int k : numConn.keySet()) {
            if (numConn.get(k) == 1) {
                queue.addLast(k);
            }
        }
        int res = 0;
        while (!queue.isEmpty()) {
            int node = queue.removeFirst();
            numConn.remove(node);
            int amount = coins.get(node) - 1;
            int[] nexts = new int[]{node / 2, 2 * node, 2 * node + 1};
            for (int nex : nexts) {
                if (numConn.getOrDefault(nex, 0) > 0) {
                    coins.put(nex, coins.get(nex) + amount);
                    res += Math.abs(amount);
                    numConn.put(nex, numConn.get(nex) - 1);
                    if (numConn.getOrDefault(nex, 0) == 1)
                        queue.addLast(nex);
                    break;
                }
            }
        }
        return res;
    }
}


class Solution2 {
    int res = 0;

    private int dfs(TreeNode node) {
        if (node == null)
            return 0;
        int left = dfs(node.left);
        int right = dfs(node.right);
        int dif = left + right + node.val - 1;
        res += Math.abs(dif);
        return dif;
    }

    public int distributeCoins(TreeNode root) {
        /*
         * I was really dumb with the previous solution, because topological
         * sort on a tree is just regular DFS.
         *
         * O(N), 0 ms, faster than 100.00%
         */
        dfs(root);
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
