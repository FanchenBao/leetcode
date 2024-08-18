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

class Solution1 {
    public long maxPoints(int[][] points) {
        /*
         * LeetCode 1937
         *
         * Basic dp where dp[i][j] is the max points earned when points[i][j]
         * is selected. However, this will result in O(MN * N) runtime and it
         * will time out if points is a very fat matrix.
         *
         * To reduce the amount of check, we first obtain the max value for
         * dp[i - 1]. Then for points[i], we only visit the j that do not
         * result in a distance penalty larger than the max of dp[i - 1]. This
         * can shrink the amount of check needed, but still not foolproof, 
         * because I can see scenarios where this can still fail.
         *
         * 1663 ms, faster than 9.41%
         */
        int M = points.length;
        int N = points[0].length;
        long[] dp = new long[N];
        long res = 0;
        for (int j = 0; j < N; j++) {
            dp[j] = (long)points[0][j];
            res = Math.max(res, dp[j]);
        }
        for (int i = 1; i < M; i++) {
            long[] tmp = new long[N];
            long rowMax = 0;
            for (long p : dp)
                rowMax = Math.max(rowMax, p);
            for (int j = 0; j < N; j++) {
                for (long k = Math.max(0, j - rowMax); k < Math.min(N, j + rowMax + 1);  k++) {
                    tmp[j] = Math.max(tmp[j], (long)points[i][j] + dp[(int)k] - Math.abs(j - (int)k));
                }
                res = Math.max(res, tmp[j]);
            }
            dp = tmp;
        }
        return res;
    }
}


class Solution2 {
    public long maxPoints(int[][] points) {
        /*
         * This is the official solution. It uses two auxilary array leftMax
         * and rightMax to find the max points achievable from the previous
         * row in range [0, i] or [i, N]
         *
         * Essentially, this is a second DP, because we have the following
         * relationship
         *
         * leftMax[i] = max(leftMax[i - 1] - 1, preRow[i])
         *
         * We are saying that for the current position, the max value we can
         * achieve is either with no penalty to take preRow[i], or with a
         * penalty to use leftMax[i - 1]
         *
         * The same applies to rightMax.
         *
         * This solution runs in O(MN), 7 ms, faster than 75.88%
         */
        int M = points.length;
        int N = points[0].length;
        long[] dp = new long[N];
        long res = 0;
        for (int j = 0; j < N; j++) {
            dp[j] = points[0][j];
            res = Math.max(res, dp[j]);
        }
        for (int i = 1; i < M; i++) {
            long[] tmp = new long[N];
            tmp[0] = dp[0];
            // create leftMax directly on tmp
            for (int j = 1; j < N; j++)
                tmp[j] = Math.max(dp[j], tmp[j - 1] - 1);
            // create rightMax and update tmp directly
            long curRM = 0;
            for (int j = N - 1; j >= 0; j--) {
                curRM = Math.max(dp[j], curRM - 1);
                tmp[j] = Math.max(tmp[j], curRM) + points[i][j];
                res = Math.max(res, tmp[j]);
            }
            dp = tmp;
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
