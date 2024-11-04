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
    public boolean rotateString(String s, String goal) {
        /*
         * LeetCode 796
         *
         * Concatenate goal by itself, then s must be a substring of the
         * concatenated new string.
         *
         * 0 ms, faster than 100.00%
         */
        if (s.length() != goal.length())
            return false;
        return (goal + goal).contains(s);
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
