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
    public int equalSubstring(String s, String t, int maxCost) {
        /*
         * LeetCode 1208
         *
         * Classic sliding window problem
         *
         * O(N), 8 ms, faster than 55.43%
         */
        int i = 0;
        int res = 0;
        int cost = 0;
        for (int j = 0; j < s.length(); j++) {
            cost += Math.abs(s.charAt(j) - t.charAt(j));
            while (cost > maxCost) {
                cost -= Math.abs(s.charAt(i) - t.charAt(i));
                i++;
            }
            res = Math.max(res, j - i + 1);
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
