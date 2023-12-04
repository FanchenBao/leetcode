class Solution {
    public int findValueOfPartition(int[] nums) {
        /*
        Sort the values and find the minimum difference
        between consecutive values.
        
        O(NlogN), 19 ms, faster than 56.19%
        */
        Arrays.sort(nums);
        int res = Integer.MAX_VALUE;
        for (int i = 1; i < nums.length; i++) {
            res = Math.min(res, nums[i] - nums[i - 1]);
        }
        return res;
    }
}
