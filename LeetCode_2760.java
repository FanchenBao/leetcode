class Solution {
    public int longestAlternatingSubarray(int[] nums, int threshold) {
        /*
        The logic is not that easy to write.

        4 ms, faster than 92.95% 
        */
        int res = 0;
        int lo = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > threshold) {
                res = Math.max(res, i - lo);
                lo = i + 1;
                continue;
            }
            if (nums[i] % 2 == 1) {
                if (lo == i || nums[i - 1] % 2 != 0) {
                    res = Math.max(res, i - lo);
                    lo = i + 1;
                }
            } else {
                if (lo == i || nums[i - 1] % 2 != 1) {
                    res = Math.max(res, i - lo);
                    lo = i;
                }
            }
        }
        return Math.max(res, nums.length - 1 - lo + 1);
    }
}
