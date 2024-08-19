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
    public int minSteps(int n) {
        /*
         * LeetCode 650
         *
         * dp[i][j] = min operations to create i number of 'A's with the last
         * copy containing j number of 'A's.
         *
         * O(N^2), 37 ms, faster than 8.16%
         */
        int[][] dp = new int[n + 1][n + 1];
        int MAX = 2000; // some big value to avoid overflow
        for (int i = 1; i <= n; i++)
            Arrays.fill(dp[i], MAX);
        dp[1][1] = 1;
        for (int i = 2; i <= n; i++) {
            for (int j = 1; j <= i / 2; j++) {
                dp[i][j] = dp[i - j][j] + 1;
                dp[i][i] = Math.min(dp[i][i], dp[i][j]);
            }
            dp[i][i]++;
        }
        return dp[n][n] - 1;
    }
}


class Solution2 {
    public int minSteps(int n) {
        /*
         * Standard DP.
         *
         * dp[i] is the min operations to reach i number of 'A's.
         *
         * To find dp[k], we go through j from k // 2 to 1, in which the js
         * that divides k can be used as the last copy such that the operations
         * needed to reach k is dp[j] + k // j
         *
         * O(N^2) 27 ms, faster than 19.85%
         */
        int[] dp = new int[n + 1];
        int MAX = 2000;
        Arrays.fill(dp, MAX);
        dp[1] = 0;
        for (int i = 2; i <= n; i++) {
            for (int j = 1; j <= i / 2; j++) {
                if (i % j == 0)
                    dp[i] = Math.min(dp[i], dp[j] + i / j);
            }
        }
        return dp[n];
    }
}


class Solution3 {
    public int minSteps(int n) {
        /*
         * The official solution provides a very good explanation why the
         * problem is equivalent to finding the sum of all prime factors of n.
         *
         * The explanation is as follows. Given n, we can always break it down
         * to a series of Copy and Paste, such as
         * [CPP][CPPP][CP]
         *
         * Suppose that each sequence contains g steps, then the total number
         * of operations is g1 + g2 + g3.
         *
         * Meanwhile, the total number of 'A' produced is g1 * g2 * g3, because
         * each subsequent copy copies the entirety of the previous 'A's
         * produced.
         *
         * Thus, the problem becomes finding the factors of n such that the
         * sum of these factors is minimized.
         * 
         * We can observe that if g is not a prime, we can break it down to
         * g = p * q. Since p + q is always no bigger than p * q when both
         * p and q are larger than 1 (this can be readily proved), the best
         * strategy is to break down n as much as possible, i.e., finding all
         * the prime factors. The answer to the problem is the sum of all the
         * prime factors.
         *
         * O(N), 0 ms, faster than 100.00%
         */
        int res = 0;
        int f = 2;
        while (n > 1) {
            if (n % f == 0) {
                n /= f;
                res += f;
            } else {
                f++;
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
