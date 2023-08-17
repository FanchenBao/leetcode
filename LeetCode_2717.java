class Solution {
    public int semiOrderedPermutation(int[] nums) {
        /*
        1 ms, faster than 100.00%
        */
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == nums.length) {
                res += nums.length - i - 1; 
            } else if (nums[i] == 1) {
                res += res == 0 ? i : i - 1;
            }
        }
        return res;
    }
}
