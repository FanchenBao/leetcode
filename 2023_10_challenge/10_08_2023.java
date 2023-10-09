class Solution {
    public int maxDotProduct(int[] nums1, int[] nums2) {
        /*
        LeetCode 1458

        We know immediately that this is DP. And it's similar to finding LCS.

        O(M^2N^2), 356 ms, faster than 5.56% 
         */
        int[][] dp = new int[nums1.length][nums2.length];
        // initialize
        dp[0][0] = nums1[0] * nums2[0];
        for (int i = 1; i < nums1.length; i++) dp[i][0] = Math.max(dp[i - 1][0], nums1[i] * nums2[0]);
        for (int j = 1; j < nums2.length; j++) dp[0][j] = Math.max(dp[0][j - 1], nums1[0] * nums2[j]);
        // DP
        for (int i = 1; i < nums1.length; i++) {
            for (int j = 1; j < nums2.length; j++) {
               dp[i][j] = Math.max(
                   Math.max(dp[i - 1][j], dp[i][j - 1]),
                   Math.max(dp[i - 1][j - 1] + nums1[i] * nums2[j], nums1[i] * nums2[j])
               );
                for (int jj = 1; jj < j; jj++) { // use nums1[i - 1] to pair with all possible nums2
                    dp[i][j] = Math.max(
                        dp[i][j], Math.max(dp[i - 1][jj - 1] + nums1[i] * nums2[jj], nums1[i] * nums2[jj])
                    );
                }
                for (int ii = 1; ii < i; ii++) { // use nums2[j - 1] to pair with all possible nums1
                    dp[i][j] = Math.max(
                        dp[i][j], Math.max(dp[ii - 1][j - 1] + nums1[ii] * nums2[j], nums1[ii] * nums2[j])
                    );
                }
            }
        }
        return dp[nums1.length - 1][nums2.length - 1];
    }
}


class Solution {
    public int maxDotProduct(int[] nums1, int[] nums2) {
        /*
        Exactly the same as LCS
        
        O(MN), 9 ms, faster than 94.44%
        */
        int[][] dp = new int[nums1.length][nums2.length];
        // initialize
        dp[0][0] = nums1[0] * nums2[0];
        for (int i = 1; i < nums1.length; i++) dp[i][0] = Math.max(dp[i - 1][0], nums1[i] * nums2[0]);
        for (int j = 1; j < nums2.length; j++) dp[0][j] = Math.max(dp[0][j - 1], nums1[0] * nums2[j]);
        // DP
        for (int i = 1; i < nums1.length; i++) {
            for (int j = 1; j < nums2.length; j++) {
               dp[i][j] = Math.max(
                   Math.max(dp[i - 1][j], dp[i][j - 1]),
                   Math.max(dp[i - 1][j - 1] + nums1[i] * nums2[j], nums1[i] * nums2[j])
               );
            }
        }
        return dp[nums1.length - 1][nums2.length - 1];
    }
}