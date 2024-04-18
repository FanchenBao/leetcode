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

class Solution1 {
    String res = "{";

    private void helper(TreeNode node, String cur) {
        char c = (char)(node.val + 97);
        String next = c + cur;
        if (node.left == null && node.right == null) {
            res = res.compareTo(next) > 0 ? next : res;
            return;
        }   
        if (node.left != null)
            helper(node.left, next);
        if (node.right != null)
            helper(node.right, c + cur);
    }

    public String smallestFromLeaf(TreeNode root) {
        /*
         * LeetCode 988
         *
         * DFS, O(N^2) due to concatenation of string, 8 ms, faster than 39.83%
         */
        helper(root, "");
        return res;
    }
}


class Solution2 {
    String res = "{";
    char[] arr = new char[8500];

    private void helper(TreeNode node, int idx) {
        arr[idx] = (char)(node.val + 97);
        if (node.left == null && node.right == null) {
            String cur = String.valueOf(Arrays.copyOfRange(arr, idx, arr.length));
            res = res.compareTo(cur) > 0 ? cur : res;
            return;
        }   
        if (node.left != null)
            helper(node.left, idx - 1);
        if (node.right != null)
            helper(node.right, idx - 1);
    }

    public String smallestFromLeaf(TreeNode root) {
        /*
         * LeetCode 988
         *
         * O(N) because there is concatenation, with char array, it's much much faster.
         * 1 ms, faster than 99.37%
         *
         */
        helper(root, 8499);
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
