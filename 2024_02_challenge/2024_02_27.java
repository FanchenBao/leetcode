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
    int diameter = 0;

    private int longestPath(TreeNode root) {
        if (root == null)
            return -1;
        if (root.left == null && root.right == null)
            return 0;
        int left = longestPath(root.left);
        int right = longestPath(root.right);
        this.diameter = Math.max(this.diameter, left + right + 2);
        return Math.max(left, right) + 1;
    }

    public int diameterOfBinaryTree(TreeNode root) {
        /*
        LeetCode 543
        
        Find the longest path starting of a node's left and/or right child.
        Then the longest diameter with the current node as pass-through is
        the sum of the left and right max path.
        
        Note the use of -1 as path when the current node is empty.
        */
        longestPath(root);
        return this.diameter;
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
