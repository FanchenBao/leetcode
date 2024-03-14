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
    public int pivotInteger(int n) {
        /*
         * LeetCode 2485
         *
         * Some math manipulation shows that if n * (n + 1) / 2 is a perfect
         * square, then the answer is the square root of that value. Otherwise
         * such answer does not exist.
         *
         * 0 ms, faster than 100.00%
         */
        int test = n * (n + 1) / 2;
        double res = Math.sqrt(test);
        return res == Math.floor(res) ? (int)res : -1;
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
