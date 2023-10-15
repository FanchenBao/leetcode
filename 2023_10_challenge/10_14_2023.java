class Solution {
    public int paintWalls(int[] cost, int[] time) {
        /*
        Bottom up DP with O(N) space and O(N^2) time.
        
        8 ms, faster than 98.47% 
         */
        int N = cost.length;
        int[] dp = new int[N + 1];
        // handle the last row
        dp[0] = 0;
        for (int i = 1; i <= N; i++) {
            if (time[N - 1] + 1 >= i) dp[i] = cost[N - 1];
            else dp[i] = 500000000;
        }
        int p;
        for (int i = N - 2; i >= 0; i--) {
            for (int j = N; j > 0; j--) {
                p = j - 1 - time[i];
                dp[j] = Math.min(dp[j], cost[i] + (p < 0 ? 0 : dp[p]));
            }
        }
        return dp[N];
    }
}
