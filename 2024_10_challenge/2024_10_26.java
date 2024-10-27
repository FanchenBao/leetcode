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

class Solution {
    private int getHeight(TreeNode node, TreeNode par, Map<Integer, Integer> heights, Map<Integer, int[]> mapping) {
        if (node == null)
            return -1;
        int lh = getHeight(node.left, node, heights, mapping) + 1;
        int ln = node.left == null ? 0 : node.left.val;
        int rh = getHeight(node.right, node, heights, mapping) + 1;
        int rn = node.right == null ? 0 : node.right.val;
        heights.put(node.val, Math.max(lh, rh));
        mapping.put(node.val, new int[]{ln, rn, par.val});
        return heights.get(node.val);
    }

    private void getImpacting(TreeNode node, Map<Integer, Integer> heights, Map<Integer, Boolean> impacting) {
        if (node == null)
            return;
        impacting.put(node.val, true); // if a node is visited, it must be impacting the heights
        int lh = node.left == null ? -1 : heights.get(node.left.val);
        int rh = node.right == null ? -1 : heights.get(node.right.val);
        if (lh > rh && lh >= 0) {
            getImpacting(node.left, heights, impacting);
        } else if (rh > lh && rh >= 0) {
            getImpacting(node.right, heights, impacting);
        }
        // notice that if lh == rh, we do not set any impact because there
        // are redundancy now even if both branches contribute to the max
        // height. Removing any subtree of left or right will not impact the
        // max height
    }

    public int[] treeQueries(TreeNode root, int[] queries) {
        /*
         * LeetCode 2458
         *
         * We keep track of each node's height and its left child, right child
         * and parent. We store this information in two hashmaps. Then each
         * time when a node is removed, we update its parent's new height, and
         * then move one level up to update its parent's parent's height. So
         * on and so forth, until we obtain the updated height of the root.
         *
         * O(N + KlogN), where N is the number of nodes in the tree and K =
         * len(queries)
         *
         * Unfortunately, it TLE
         */
        Map<Integer, Integer> heights = new HashMap<>();
        heights.put(0, -1);
        Map<Integer, int[]> mapping = new HashMap<>(); // node -> [left, right, parent]
        getHeight(root, new TreeNode(0), heights, mapping);
        Map<Integer, Boolean> impacting = new HashMap<>(); // True means a node impacts the max height
        getImpacting(root, heights, impacting);
        int[] res = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int c = queries[i]; // deleted node
            if (!impacting.getOrDefault(c, false)) {
                // if the deleted node will not impact the max height, no need
                // to do any computation
                res[i] = heights.get(root.val);
                continue;
            }
            int ch = -1; // current child height
            int p = mapping.get(c)[2]; // parent od deleted node
            while (p > 0) {
                // other child height
                int oh = mapping.get(p)[0] == c ? heights.get(mapping.get(p)[1]) : heights.get(mapping.get(p)[0]);
                ch = Math.max(ch, oh) + 1;
                c = p;
                p = mapping.get(p)[2];
            }
            res[i] = ch;
        }
        return res;
    }
}


class Solution1 {
    int MAX = 10000;
    int[] heights = new int[MAX + 1];
    boolean[] impacting = new boolean[MAX + 1];
    int[][] mapping = new int[MAX + 1][3]; //node -> [left, right, parent]

    private int getHeight(TreeNode node, TreeNode par) {
        if (node == null)
            return -1;
        int lh = getHeight(node.left, node) + 1;
        int ln = node.left == null ? 0 : node.left.val;
        int rh = getHeight(node.right, node) + 1;
        int rn = node.right == null ? 0 : node.right.val;
        this.heights[node.val] = Math.max(lh, rh);
        this.mapping[node.val][0] = ln;
        this.mapping[node.val][1] = rn;
        this.mapping[node.val][2] = par.val;
        return heights[node.val];
    }

    private void getImpacting(TreeNode node) {
        if (node == null)
            return;
        this.impacting[node.val] = true; // if a node is visited, it must be impacting the heights
        int lh = node.left == null ? -1 : heights[node.left.val];
        int rh = node.right == null ? -1 : heights[node.right.val];
        if (lh > rh && lh >= 0) {
            getImpacting(node.left);
        } else if (rh > lh && rh >= 0) {
            getImpacting(node.right);
        }
        // notice that if lh == rh, we do not set any impact because there
        // are redundancy now even if both branches contribute to the max
        // height. Removing any subtree of left or right will not impact the
        // max height
    }

    public int[] treeQueries(TreeNode root, int[] queries) {
        /*
         * LeetCode 2458
         *
         * We keep track of each node's height and its left child, right child
         * and parent. We store this information in two hashmaps. Then each
         * time when a node is removed, we update its parent's new height, and
         * then move one level up to update its parent's parent's height. So
         * on and so forth, until we obtain the updated height of the root.
         *
         * O(N + KlogN), where N is the number of nodes in the tree and K =
         * len(queries)
         *
         * 315 ms, faster than 5.26%
         */
        this.heights[0] = -1;
        getHeight(root, new TreeNode(0));
        getImpacting(root);
        int[] res = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int c = queries[i]; // deleted node
            if (!impacting[c]) {
                // if the deleted node will not impact the max height, no need
                // to do any computation
                res[i] = heights[root.val];
                continue;
            }
            int ch = -1; // current child height
            int p = mapping[c][2]; // parent od deleted node
            while (p > 0) {
                // other child height
                int oh = mapping[p][0] == c ? heights[mapping[p][1]] : heights[mapping[p][0]];
                ch = Math.max(ch, oh) + 1;
                c = p;
                p = mapping[p][2];
            }
            res[i] = ch;
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
