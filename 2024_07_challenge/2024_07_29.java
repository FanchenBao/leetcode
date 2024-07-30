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
    public int numTeams(int[] rating) {
        /*
         * LeetCode 1395
         *
         * Brute force O(N^2). First find the count of numbers down the line
         * that are smaller or bigger than the current number. Then use this
         * info to compute the number of triplets available.
         *
         * 20 ms, faster than 48.38%
         */
        int[] cntBigger = new int[rating.length];
        int[] cntSmaller = new int[rating.length];
        for (int i = 0; i < rating.length; i++) {
            for (int j = i + 1; j < rating.length; j++) {
                if (rating[j] > rating[i])
                    cntBigger[i]++;
                else
                    cntSmaller[i]++;
            }
        }
        int res = 0;
        for (int i = 0; i < rating.length; i++) {
            if (cntBigger[i] >= 2) {
                for (int j = i + 1; j < rating.length; j++) {
                    if (rating[j] > rating[i])
                        res += cntBigger[j];
                }
            }
            if (cntSmaller[i] >= 2) {
                for (int j = i + 1; j < rating.length; j++) {
                    if (rating[j] < rating[i])
                        res += cntSmaller[j];
                }
            }
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
