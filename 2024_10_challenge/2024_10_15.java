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
    public long minimumSteps(String s) {
        /*
         * LeetCode 2938
         *
         * From right to left, count the number of zeros. Each time a one is
         * encountered, add the current count of zeros as the number of min
         * swaps needed to move that one to the right.
         *
         * O(N), 7 ms, faster than 100.00%
         */
        long res = 0;
        long zeros = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == '0')
                zeros++;
            else
                res += zeros;
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
