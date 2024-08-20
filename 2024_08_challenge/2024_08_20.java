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
    private int getMaxStones(int idx, int M, int[] piles, int[][] dp, int[] presum) {
        if (idx >= piles.length)
            return 0;
        if (dp[idx][M] == 0) {
            for (int X = 1; X <= 2 * M; X++) {
                int nextIdx = Math.min(idx + X, piles.length);
                int nextM = Math.max(M, X);
                int nextMax = getMaxStones(nextIdx, nextM, piles, dp, presum);
                int available = idx > 0 ? presum[presum.length - 1] - presum[idx - 1] : presum[presum.length - 1];
                dp[idx][M] = Math.max(dp[idx][M], available - nextMax);
            }
        }
        return dp[idx][M];
    }

    public int stoneGameII(int[] piles) {
        /*
         * LeetCode 1140
         *
         * Very poorly configured DP. dp[i][j] = max stones any player can get
         * starting from piles[i] with M = j
         *
         * O(N^3), 10 ms, faster than 54.85%
         * */
        int N = piles.length;
        int[] presum = new int[N];
        int[][] dp = new int[N + 1][2 * N + 1];
        presum[0] = piles[0];
        for (int i = 1; i < N; i++)
            presum[i] = presum[i - 1] + piles[i];
        return getMaxStones(0, 1, piles, dp, presum);
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
