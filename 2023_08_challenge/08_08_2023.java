class Solution {
    public int search(int[] nums, int target) {
        /*
        LeetCode 33

        A more complex binary search.

        O(logN), 0 ms.
        
        Update: during binary search, we can use nums[lo] and nums[hi] for the left and right
        boundary instead of nums[0] and nums[nums.lenght - 1]
         */
        int lo = 0;
        int hi = nums.length - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            if (nums[mid] >= nums[lo]) {
                if (target < nums[mid] && target >= nums[lo]) {
                    hi = mid - 1;
                } else {
                    lo = mid + 1;
                }
            } else {
                if (target <= nums[hi] && target > nums[mid]) {
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }
        }
        return -1;
    }
}