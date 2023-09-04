class Solution {
    public int uniquePaths(int m, int n) {
        /*
        LeetCode 62

        Standard DP, can be 1D.

        O(MN), 0 ms, faster than 100.00%
         */
        int[] dp = new int[n + 1];
        for (int j = 0; j < n; j++) {
            dp[j] = 1;
        }
        for (int i = m - 2; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                dp[j] += dp[j + 1];
            }
        }
        return dp[0];
    }
}
