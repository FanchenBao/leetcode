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
    public TreeNode addOneRow(TreeNode root, int val, int depth) {
        /*
        LeetCode 623
        
        DFS, 0 ms, faster than 100.00%
        */
        if (depth - 1 == 0)
            return new TreeNode(val, root, null);
        if (depth - 1 == 1) {
            root.left = new TreeNode(val, root.left, null);
            root.right = new TreeNode(val, null, root.right);
            return root;
        }
        if (root.left != null)
            addOneRow(root.left, val, depth - 1);
        if (root.right != null)
            addOneRow(root.right, val, depth - 1);
        return root;
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
