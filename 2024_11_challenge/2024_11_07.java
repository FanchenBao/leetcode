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
    public int largestCombination(int[] candidates) {
        /*
         * LeetCode 2275
         *
         * Count the number of 1s at each bit position. The answer should be
         * the largest count among all the positions.
         *
         * O(N), 35 ms, faster than 15.87%
         */
        int[] counter = new int[24];
        for (int c : candidates) {
            for (int i = 0; i <= 23; i++)
                counter[i] += ((1 << i) & c) == 0 ? 0 : 1;
        }
        int res = 0;
        for (int c : counter)
            res = Math.max(res, c);
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
