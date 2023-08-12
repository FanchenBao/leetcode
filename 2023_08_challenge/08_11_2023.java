class Solution1 {
    Integer[][] memo;
    int[] coins;

    private int dp(int idx, int rem) {
        if (rem == 0) {
            return 1;
        }
        if (idx == memo.length) {
            return 0;
        }
        if (memo[idx][rem] != null) {
            return memo[idx][rem];
        }
        int res = 0;
        for (int i = 0; i * coins[idx] <= rem; i++) {
            res += dp(idx + 1, rem - i * coins[idx]);
        }
        memo[idx][rem] = res;
        return res;
    }

    public int change(int amount, int[] coins) {
        /*
        LeetCode 518

        DP(idx, rem) find the total number of ways to form rem money using coins[idx:].

        Worse than O(N * Amount), 48 ms, faster than 8.08%

        UPDATE: make coins a field of the class, thus we don't have to pass it to the dp function.
         */
        memo = new Integer[coins.length][amount + 1];
        this.coins = coins;
        return dp(0, amount);
    }
}


class Solution2 {
    public int change(int amount, int[] coins) {
        /*
        Bottom up DP
        This is worse than O(N * amount)
         */
        int[] dp = new int[amount + 1];
        dp[0] = 1; // edge case, which means when amount is zero and there is no coints, we have one way to form
        for (int i = coins.length - 1; i >= 0; i--) {
            for (int rem = amount; rem >= 0; rem--) {
                int curCount = 0;
                for (int j = 0; coins[i] * j <= rem; j++) {
                    curCount += dp[rem - coins[i] * j];
                }
                dp[rem] = curCount;
            }
        }
        return dp[amount];
    }
}


class Solution3 {
    public int change(int amount, int[] coins) {
        /*
        Bottom up DP, 1D from the official solution. Very very neat.
        
        3 ms, faster than 91.90%
         */
        int[] dp = new int[amount + 1];
        dp[0] = 1; // edge case, which means when amount is zero and there is no coints, we have one way to form
        for (int i = coins.length - 1; i >= 0; i--) {
            for (int rem = coins[i]; rem <= amount; rem++) {
                // To understand this, write the DP in 2D form first
                dp[rem] += dp[rem - coins[i]];
            }
        }
        return dp[amount];
    }
}


class Solution4 {
    Integer[][] memo;
    int[] coins;

    private int dp(int idx, int rem) {
        if (rem == 0) {
            return 1;
        }
        if (idx == memo.length) {
            return 0;
        }
        if (memo[idx][rem] != null) {
            return memo[idx][rem];
        }
        int res = 0;
        if (coins[idx] > rem) {
            memo[idx][rem] = dp(idx + 1, rem);
        } else {
            // either take coins[i] or not. If we take coins[i], we have rem - coins[i] left,
            // but we need to still dp from i, because we can take multiple i. If we don't take
            // coins[i], then we go directly for idx + 1
            memo[idx][rem] = dp(idx, rem - coins[idx]) + dp(idx + 1, rem);
        }
        return memo[idx][rem];
    }

    public int change(int amount, int[] coins) {
        /*
        Top down with better solution. We need to change the DP condition so that there is no additional
        loop in dp.
        
        O(N * Amount), 16 ms, faster than 16.39%
         */
        memo = new Integer[coins.length][amount + 1];
        this.coins = coins;
        return dp(0, amount);
    }
}