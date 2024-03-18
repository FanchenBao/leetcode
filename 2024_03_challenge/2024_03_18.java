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
    public int findMinArrowShots(int[][] points) {
        /*
         * LeetCode 452
         *
         * Greedy. Try to find as many balloons as possible that overlap with
         * the current one under consideration. Once the overlap ends, we reset
         * the current balloon and all the previous balloons will be popped by
         * one arrow.
         *
         * O(NlogN), 57 ms, faster than 35.08% 
         */
        Arrays.sort(points, Comparator.comparingInt(p -> p[0]));
        int minRight = points[0][1];
        int res = 0;
        for (int i = 1; i < points.length; i++) {
            if (points[i][0] > minRight) {
                res++;
                minRight = points[i][1];
            } else {
                minRight = Math.min(minRight, points[i][1]);
            }
        }
        return res + 1;
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
