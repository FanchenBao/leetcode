class Solution {
    public int integerBreak(int n) {
        /*
        LeetCode 343
        
        For each n, we break it up to 1 + n - 1, 2 + n - 2, ...
        Let the first element not break up, then the max of the break
        would be the max product of 1 * integerBreak(n - 1), 2 * integerBreak(n - 2), ...
        This is typical DP.
        
        O(N^2), 0 ms, faster than 100.00% 
        */
        if (n == 2) return 1;
        if (n == 3) return 2;
        int[] dp = new int[n + 1];
        dp[2] = 2; dp[3] = 3;
        for (int i = 4; i <= n; i++) {
            for (int j = 1; j <= i / 2; j++) {
                dp[i] = Math.max(dp[i], dp[i - j] * j);
            }
        }
        return dp[n];
    }
}
