class Solution {
    public int sumOfSquares(int[] nums) {
        /*
        O(N), 1 ms, faster than 100.00%
        */
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums.length % (i + 1) == 0)
                res += nums[i] * nums[i];
        }
        return res;
    }
}

