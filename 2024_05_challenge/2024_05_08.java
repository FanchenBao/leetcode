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
    public String[] findRelativeRanks(int[] score) {
        /*
         * LeetCode 506
         *
         * 8 ms, faster than 80.99%
         */
        int[][] sortedScore = new int[score.length][2];
        for (int i = 0; i < score.length; i++) {
            sortedScore[i][0] = score[i];
            sortedScore[i][1] = i;
        }
        Arrays.sort(sortedScore, (t1, t2) -> Integer.compare(-t1[0], -t2[0]));
        String[] res = new String[score.length];
        for (int i = 0; i < score.length; i++) {
            if (i == 0)
                res[sortedScore[i][1]] = "Gold Medal";
            else if (i == 1)
                res[sortedScore[i][1]] = "Silver Medal";
            else if (i == 2)
                res[sortedScore[i][1]] = "Bronze Medal";
            else
                res[sortedScore[i][1]] = String.valueOf(i + 1);
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
