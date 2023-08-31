class Solution {
    public long minimumReplacement(int[] nums) {
        /*
        LeetCode 2366

        Greedy. From right to left, the right most must not split, because otherwise we will always be left with a
        smaller value to handle the remaining numbers. Let's set the limit to the right most value.

        Thus, for each number, we divide it by the limit and get q as quotient and r as remainder. If it is divisible,
        the next limit remains the same, and we perform q - 1 splits.

        Otherwise, we perform q splits, but we want the next limit to be as big as possible. To do so, we need to
        increase r by taking 1 value from each of the q limit. We keep doing this, until r becomes bigger than the
        value after 1s having been taken away from the limit. Then the next limit is the remaining limit after such
        operation. The purpose of doing this is to ensure that the next limit can be as big as possible.

        Suppose we need to do the taking away k times. Then we want r + q * k >= limit - k, which is
        k >= (limit - r) / (q + 1) If k is not an int, we take the ceil of it.

        O(N), 3 ms, faster than 100.00%
         */
        long res = 0;
        int lim = nums[nums.length - 1];
        for (int i = nums.length - 2; i >= 0; i--) {
            if (nums[i] <= lim) {
                lim = nums[i];
            } else {
                int r = nums[i] % lim; int q = nums[i] / lim;
                res += q;
                if (r == 0) {
                    res--;
                } else {
                    lim -= (int)Math.ceil((double)(lim - r) / (q + 1));
                }
            }
        }
        return res;
    }
}