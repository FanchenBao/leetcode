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
    public boolean flipEquiv(TreeNode root1, TreeNode root2) {
        /*
         * LeetCode 951
         *
         * For each pair of root1 and root2, first consider the edge cases,
         * such as one is null and the other is not null, etc.
         *
         * When both are not null and their values are the same, we can
         * proceed with two possibilites of the next round of check: flip or
         * not flip. We will take the OR of the two outcome.
         *
         * Since each value is unique, only one of the checks will return true.
         * So the time complexity should be O(N)
         * 0 ms, faster than 100.00%
         */
        if (root1 == null && root2 == null)
            return true;
        if (root1 != null && root2 != null) {
            if (root1.val != root2.val)
                return false;
            return (
                flipEquiv(root1.left, root2.left) && flipEquiv(root1.right, root2.right)
            ) || (
                flipEquiv(root1.left, root2.right) && flipEquiv(root1.right, root2.left)
            );
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
