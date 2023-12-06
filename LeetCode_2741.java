class Solution {
    Integer[][] memo;
    int MOD = 1000000007;
    int N;
    int[] nums;

    private int dp(int idx, int seen) {
        // seen is a bit mask to keep track of which indices have been used
        if (memo[idx][seen] != null)
            return memo[idx][seen];
        int cur = seen | (1 << idx);
        if (cur == (1 << N) - 1)
            return 1;
        
        long res = 0;
        for (int a = 0; a < N; a++) {
            // Do not pre-create the graph. Since
            // the size of nums is small, we can simply
            // loop through it to find the next child.
            if (((1 << a) & cur) == 0 && (nums[a] % nums[idx] == 0 || nums[idx] % nums[a] == 0))
                res = (res + dp(a, cur)) % MOD;
        }
        memo[idx][seen] = (int)res;
        return memo[idx][seen];
    }

    public int specialPerm(int[] nums) {
        /*
        Fail
        
        Not difficult problem, and also already found the solution, but
        we got sloppy in writing the DP recursion. We basically misaligned
        the dp(idx, seen) with memo[idx][seen]. Once these two are aligned,
        we have the solution.
        
        O(N^2 * 2 ^N)
        */
        N = nums.length;
        this.nums = nums;
        
        // DP to find the answer
        memo = new Integer[N][1 << N];
        long res = 0;
        for (int i = 0; i < N; i++)
            res = (res + dp(i, 0)) % MOD;
        return (int)res;
    }
}
