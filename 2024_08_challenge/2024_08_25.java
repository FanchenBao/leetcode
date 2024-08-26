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
    private void postorder(TreeNode node, List<Integer> res) {
        if (node != null)  {
            postorder(node.left, res);
            postorder(node.right, res);
            res.add(node.val);
        }
    }

    public List<Integer> postorderTraversal(TreeNode root) {
        /*
         * LeetCode 145
         *
         * 0 ms, faster than 100.00%
         */
        List<Integer> res = new ArrayList<>();
        postorder(root, res);
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
