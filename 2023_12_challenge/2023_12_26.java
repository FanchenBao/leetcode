class Solution {
    public int numRollsToTarget(int n, int k, int target) {
        /*
        LeetCode 1155
        
        DP, where dp[i][j] is the number of ways to make j
        given i number of dices.
        
        O(NKT), where T = target. 17 ms, faster than 35.05%
         */
        long[] pre = new long[target + 1];
        int MOD = 1000000007;
        for (int i = 1; i <= Math.min(k, target); i++)
            pre[i] = 1;
        for (int i = 2; i <= n; i++) {
            long[] cur = new long[target + 1];
            for (int d = 1; d <= k; d++) {
                for (int j = 1; j <= target - d; j++) {
                    cur[j + d] = (cur[j + d] + pre[j]) % MOD;
                }
            }
            pre = cur;
        }
        return (int)pre[target];
    }
}


class Solution {
    public int numRollsToTarget(int n, int k, int target) {
        /*
        LeetCode 1155

        DP, where dp[i][j] is the number of ways to make j
        given i number of dices.

        Also, we use prefix sum to speed things up.

        O(NT), where T = target. 6 ms, faster than 94.31%
         */
        long[] pre = new long[target + 1]; // prefix sum
        int MOD = 1000000007;
        for (int i = 1; i <= target; i++)
            pre[i] = pre[i - 1] + (i <= k ? 1 : 0);
        for (int i = 2; i <= n; i++) {
            long[] cur = new long[target + 1]; // also a prefix sum
            for (int j = 1; j <= target; j++)
                cur[j] = (pre[j - 1] - pre[Math.max(1, j - k) - 1] + cur[j - 1]) % MOD;
            pre = cur;
        }
        return (int)(pre[target] - pre[target - 1] + MOD) % MOD;
    }
}

