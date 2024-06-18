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
    public boolean judgeSquareSum(int c) {
        /*
         * LeetCode 633
         *
         * Check every possible square from 0 towards half of c.
         *
         * NOTE: use long to avoid overflow.
         * 4 ms, faster than 56.86%
         */
        long a = 0;
        long C = (long)c;
        while (2 * a * a <= C) {
            long bb = C - a * a;
            long b = (long)Math.sqrt((double)bb);
            if (b * b == bb)
                return true;
            a++;
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
