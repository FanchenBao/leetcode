class Solution {
    int[] memo;
    int N;
    int[] arr;
    int k;

    private int dp(int idx) {
        /*
        dp(idx) = max sum of partitioned array from arr[idx] to the end
         */
        if (idx == N)
            return 0;
        if (memo[idx] >= 0)
            return memo[idx];
        int curMax = -1;
        for (int i = idx; i - idx + 1 <= this.k && i < this.N; i++) {
            curMax = Math.max(curMax, this.arr[i]);
            memo[idx] = Math.max(memo[idx], curMax * (i - idx + 1) + dp(i + 1));
        }
        return memo[idx];
    }

    public int maxSumAfterPartitioning(int[] arr, int k) {
        /*
        LeetCode 1043
        
        DP solution, in which we find the max sum starting from any index
        towards the end. During DP, we try all possible grouping from index
        until we hit the max length of k. For each grouping, we find its max
        sum and record it.
        
        We have solved something similar before, twice!
        
        O(NK), 5 ms, faster than 99.61% 
        */
        this.N = arr.length;
        this.memo = new int[N];
        for (int i = 0; i < N; i++) this.memo[i] = -1;
        this.arr = arr;
        this.k = k;
        return dp(0);
    }
}

