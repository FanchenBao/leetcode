class Solution {
    public int numFactoredBinaryTrees(int[] arr) {
        /*
        LeetCode 823

        Firsrt sort arr. Then Use DP, wherw dp[i] is the total number of unique binary trees
        that can be made with arr[i] as the root. For each new arr[i], we go from the front
        to find all possible pairs whose product is arr[i]. Since we know the number of
        unique binary trees created from those pairs, the number of unique binary trees
        for arr[i] is the product of the counts of its two subtrees. Note that if the
        two subtrees have different roots (e.g. parent = 6, left = 2, right = 3), then
        we need to double the product because the two subtrees can swap position.

        O(N^2), 12 ms, faster than 98.52%
         */
        Arrays.sort(arr);
        Map<Integer, Integer> arrIdx = new HashMap<>();
        for (int i = 0; i < arr.length; i++) arrIdx.put(arr[i], i);
        int MOD = 1000000007;
        long[] dp = new long[arr.length];
        Arrays.fill(dp, 1);
        int q; long res = 1;
        for (int i = 1; i < arr.length; i++) {
            for (int j = 0; j < i && arr[j] * arr[j] <= arr[i]; j++) {
                if (arr[i] % arr[j] == 0) {
                    q = arr[i] / arr[j];
                    if (arrIdx.containsKey(q)) {
                        if (arr[j] == q) dp[i] = (dp[i] + (dp[j] * dp[j]) % MOD) % MOD;
                        else dp[i] = (dp[i] + 2 * (dp[j] * dp[arrIdx.get(q)]) % MOD) % MOD;
                    }
                }
            }
            res = (res + dp[i]) % MOD;
        }
        return (int)res;
    }
}
