class Solution {
    private int bisectRight(int[] nums, int target) {
        int lo = 0; int hi = nums.length; int mid;
        while (lo < hi) {
            mid = (lo + hi) / 2;
            if (nums[mid] > target) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
    
    private int bisectLeft(int[] nums, int target) {
        int lo = -1; int hi = nums.length - 1; int mid;
        while (lo < hi) {
            mid = (lo + hi + 1) / 2;
            if (nums[mid] >= target) hi = mid - 1;
            else lo = mid;
        }
        return hi + 1;
    }
    
    public int[] searchRange(int[] nums, int target) {
        /*
        LeetCode 34

        It is never trivial to write bisect left and bisect right from scratch.
        Note that bisect right is the "default" way of doing binary search,
        whereas bisect left is a left-shifted version of bisect right.

        O(logN), 0 ms, faster than 100.00%
        */
        int l = bisectLeft(nums, target);
        int r = bisectRight(nums, target);
        return new int[]{
                0 <= l && l < nums.length ? (nums[l] == target ? l : -1) : -1,
                0 <= r - 1 && r - 1 < nums.length ? (nums[r - 1] == target ? r - 1: -1) : -1,
        };
    }
}
