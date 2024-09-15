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
    public int longestSubarray(int[] nums) {
        /*
         * LeetCode 2419
         *
         * The max AND of an array must be the max value of the array.
         *
         * Thus the problem is equivalent to finding the longest subarray that
         * contains only the max value.
         *
         * O(N), 3 ms, faster than 89.89%
         */
        int max = -1;
        for (int n : nums)
            max = Math.max(max, n);
        int res = 0;
        int cnt = 0;
        for (int n : nums) {
            if (n == max) {
                cnt++;
            } else {
                res = Math.max(res, cnt);
                cnt = 0;
            }
        }
        return Math.max(res, cnt);
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
