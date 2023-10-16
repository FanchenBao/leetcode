class Solution {
    public int numWays(int steps, int arrLen) {
        int MOD = 1000000007;
        int[] dp = new int[arrLen + 2];
        dp[1] = 1;
        for (int i = 1; i < steps; i++) {
            int[] tmp = new int[arrLen + 2];
            for (int j = 1; j <= Math.min(steps - i + 1, arrLen); j++) {
                tmp[j] = (int)(((long)dp[j - 1] + (long)dp[j] + (long)dp[j + 1]) % MOD);
            }
            dp = tmp;
        }
        return (int)((long)dp[0] + (long)dp[1] + (long)dp[2]) % MOD;
    }
}


class Solution {
    public int numWays(int steps, int arrLen) {
        /*
        LeetCode 1269
        
        dp[i][j] is the total number of ways to return to pos 0 from pos j with i number of steps left. The transition
        is dp[i][j] =
            dp[i - 1][j] stay
          + dp[i - 1][j - 1] move left
          + dp[i - 1][j + 1] move right
         
         One piece of optimization is needed to pass all the test cases: we need to terminate the traversal on j early
         because there is no need to go all the way to the end of j on each i. Essentially, on a 2D matrix, we are
         only traversing the upper left triangle. Translated to code, this is represented by the bound on j as
         min(steps - i + 1, arrLen)
         
         O(MN) time and O(N) space, where M = steps and N = arrLen.
         */
        int MOD = 1000000007;
        int[] dp = new int[arrLen + 2];
        dp[1] = 1;
        for (int i = 1; i < steps; i++) {
            int[] tmp = new int[arrLen + 2];
            for (int j = 1; j <= Math.min(steps - i + 1, arrLen); j++) {
                tmp[j] = (int)((((long)dp[j - 1] + (long)dp[j]) % MOD + (long)dp[j + 1]) % MOD);
            }
            dp = tmp;
        }
        return (int)((((long)dp[0] + (long)dp[1]) % MOD + (long)dp[2]) % MOD);
    }
}



class Solution {
    public int numWays(int steps, int arrLen) {
        /*
        UPDATE: if steps is smaller than arrLen, then we can never reach beyond the steps-th position on array.
        Essentially, this means we can shrink the arrLen to that of steps. Since steps is at most 500, that will
        make the computation A LOT faster!
        
        6 ms, faster than 96.34%
         */
        int MOD = 1000000007;
        arrLen = Math.min(steps, arrLen); // Extremely important
        int[] dp = new int[arrLen + 2];
        dp[1] = 1;
        for (int i = 1; i < steps; i++) {
            int[] tmp = new int[arrLen + 2];
            for (int j = 1; j <= arrLen; j++) {
                tmp[j] = (int)(((long)dp[j - 1] + (long)dp[j] + (long)dp[j + 1]) % MOD);
            }
            dp = tmp;
        }
        return (int)(((long)dp[0] + (long)dp[1] + (long)dp[2]) % MOD);
    }
}
