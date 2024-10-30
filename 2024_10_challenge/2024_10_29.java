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
    public int maxMoves(int[][] grid) {
        /*
         * LeetCode 2684
         *
         * Use DP from bottom right to top left. Each dp[i][j] represent the
         * max number of moves starting from grid[i][j].
         *
         * In the actual implementation, we can use 1D dp.
         *
         * O(MN), 15 ms, faster than 50.00%
         */
        int M = grid.length;
        int N = grid[0].length;
        int[] dp = new int[M];
        for (int j = N - 2; j >= 0; j--) {
            int[] tmp = new int[M];
            for (int i = M - 1; i >= 0; i--) {
                for (int k = -1; k <= 1; k++) {
                    if (i + k >= 0 && i + k < M && grid[i][j] < grid[i + k][j + 1])
                        tmp[i] = Math.max(tmp[i], 1 + dp[i + k]);
                }
            }
            dp = tmp;
        }
        int res = 0;
        for (int v : dp)
            res = Math.max(res, v);
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
