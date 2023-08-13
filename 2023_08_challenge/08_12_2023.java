class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        /*
        LeetCode 63

        This is the most efficient DP solution. 1D, from bottom to top and right to left.
        Note that we don't have to prefill the last row separately, and as long as the
        last column is not an obstacle, it remains unchanged.

        O(MN)
         */
        int M = obstacleGrid.length;
        int N = obstacleGrid[0].length;
        int[] dp = new int[N];
        dp[N - 1] = 1;
        for (int i = M - 1; i >= 0; i--) {
            for (int j = N - 1; j >= 0; j--) {
                if (obstacleGrid[i][j] == 1) {
                    dp[j] = 0;
                } else if (j < N - 1) {
                    dp[j] += dp[j + 1];
                }
            }
        }
        return dp[0];
    }
}