class Solution {
    Integer[][] memo;
    int MAX = 300001;
    int[] jobDiff;

    private int dp(int idx, int rem) {
        if (jobDiff.length - idx < rem || rem < 0)
            return MAX;
        if (idx == jobDiff.length)
            return 0;
        if (memo[idx][rem] != null)
            return memo[idx][rem];
        memo[idx][rem] = MAX;
        int max = -1;
        for (int i = idx; jobDiff.length - i >= rem && i < jobDiff.length; i++) {
            max = Math.max(max, jobDiff[i]);
            memo[idx][rem] = Math.min(memo[idx][rem], max + dp(i + 1, rem - 1));
        }
        return memo[idx][rem];
    }

    public int minDifficulty(int[] jobDifficulty, int d) {
        /*
        LeetCode 1335
        
        This problem is very similar to yesterday's (LeetCode 1531). But first
        of all, we need to rephrase the problem as such:
        
        Given an array of numbers, divide it into d subarrays such that the sum
        of the max value of each subarray is minimized. What is this minimum sum?
        
        We use dp(idx, rem) as the recursive function to compute the min sum
        of the array from idx to the end with rem number of subarrays allowed.
        
        Within the recursive function, we go from i = idx to the end and create
        all possible subarrays starting from idx ending at i. We find the max in
        it and call dp(i + 1, rem - 1) to get the min of the remaining. This is
        the part that resembles LeetCode 1531 the most.
        
        O(N^2D), where N = len(jobDifficulty), 53 ms, faster than 7.49%
        */
        memo = new Integer[jobDifficulty.length][d + 1];
        jobDiff = jobDifficulty;
        int res = dp(0, d);
        return res < MAX ? res : -1;
    }
}

