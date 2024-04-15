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
    private int helper(TreeNode root, boolean isLeft) {
        if (root == null)
            return 0;
        if (isLeft && root.left == null && root.right == null)
            return root.val;
        return helper(root.left, true) + helper(root.right, false);
    }
    public int sumOfLeftLeaves(TreeNode root) {
        /*
         * LeetCode 404
         *
         * 0 ms, faster than 100.00%
         */
        return helper(root, false);
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
