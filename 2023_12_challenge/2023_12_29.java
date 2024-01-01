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


class Solution {
    public int minDifficulty(int[] jobDifficulty, int d) {
        /*
        This is the faster solution from more than a year ago.

        It is still DP, in which dp[i][j] represents the min
        difficulty ending at jobDifficulty[j] with i number of
        subarrays.

        However, we can do this using a 1D DP and two DP arrays,
        one for the current i (we can call it tmp) and the other
        for i - 1 (we can call it dp).

        The real trick to make this solution O(ND) is that we use
        a monotonic decreasing stack to speed up the check from
        jobDifficulty[j] back to jobDifficulty[0].

        Notice that if all the values between some jobDifficulty[k] to
        jobDifficulty[j] are smaller or equal to jobDifficulty[j],
        then as we go from j to k, the difficulty of the subarray
        does not change and remains jobDifficulty[j]. Therefore, if
        we use a monotonic decreasing array for all the job difficulty
        on the left, we only need to compare with very few of them,
        since all the other job difficulties would be smaller than the
        ones in the stack.

        !!!IMPORTANT!!! Read this comment:

        https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/discuss/490316/JavaC++Python3-DP-O(nd)-Solution/958543

        to understand why this line works
        `tmp[j] = Math.min(tmp[j], tmp[k] - jobDifficulty[k] + jobDifficulty[j])`

        Once we encounter some jobDifficulty[k] that is bigger than
        jobDifficulty[j], the current difficulty would be the same as
        the difficulty of the previous difficulty already computed for
        jobDifficulty[k]. Then we continue with the stack.

        With this setup, each value in the jobDifficulty array is visited
        at most twice. Hence the overall complexity is O(ND).

        10 ms, faster than 78.09%
         */
        int N = jobDifficulty.length;
        if (N < d)
            return -1;
        int MAX = 300001;
        int[] dp = new int[N]; // represents the result of having 0 subarray
        dp[0] = jobDifficulty[0];
        for (int i = 1; i < N; i++)
            dp[i] = Math.max(dp[i - 1], jobDifficulty[i]);
        for (int i = 2; i <= d; i++) {
            Stack<Integer> stack = new Stack<>();
            int[] tmp = new int[N];
            Arrays.fill(tmp, MAX);
            for (int j = i - 1; j < N; j++) {
                // This is where everything starts
                // This is the minimum possible j position to allow i
                // number of subarrays.
                tmp[j] = (j == 0 ? 0 : dp[j - 1]) + jobDifficulty[j];
                while (!stack.isEmpty() && jobDifficulty[stack.peek()] <= jobDifficulty[j]) {
                    int k = stack.pop();
                    tmp[j] = Math.min(tmp[j], tmp[k] - jobDifficulty[k] + jobDifficulty[j]);
                }
                if (!stack.isEmpty()) {
                    tmp[j] = Math.min(tmp[j], tmp[stack.peek()]);
                }
                stack.push(j);
            }
            dp = tmp;
        }
        return dp[N - 1] == MAX ? -1 : dp[N - 1];
    }
}

