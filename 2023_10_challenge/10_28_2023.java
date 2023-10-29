class Solution {
    public int countVowelPermutation(int n) {
        /*
        LeetCode 1220
        
        The trivial DP solution is not difficult, but the magic
        of using matrix power to compute the DP process is not
        easy. However, I have no intention to implement matrix power
        in Java. Nor do I have the gana to write the matrix power
        solution in Python again.
        
        O(5N), 10 ms, faster than 77.89%
        */
        long[] dp = new long[]{1, 1, 1, 1, 1};
        int MOD = 1000000007;
        for (int i = 2; i <= n; i++) {
            long[] tmp = new long[5];
            tmp[0] = dp[1]; // a -> e
            tmp[1] = (dp[0] + dp[2]) % MOD; // e -> a | i
            tmp[2] = (dp[0] + dp[1] + dp[3] + dp[4]) % MOD; // i -> a | e | o | u
            tmp[3] = (dp[2] + dp[4]) % MOD; // o -> i | u
            tmp[4] = dp[0]; // u -> a
            dp = tmp;
        }
        long res = 0;
        for (long d : dp) res = (res + d) % MOD;
        return (int)res;
    }
}
