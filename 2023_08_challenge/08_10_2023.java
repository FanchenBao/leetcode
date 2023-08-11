class Solution {
    public boolean search(int[] nums, int target) {
        /*
        LeetCode 81

        No way to get out of the situation when nums[mid] == nums[lo] == nums[hi], because we do not know
        which half to search in the next round. Thus, we simply move lo and hi inwards by one index.

        O(N) worst case, O(logN) best case.
         */
        int lo = 0;
        int hi = nums.length - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (nums[mid] == target) {
                return true;
            }
            if (nums[mid] == nums[lo] && nums[mid] == nums[hi]) {
                // skip all the duplicates
                lo += 1;
                hi -= 1;
            } else if (nums[mid] >= nums[lo]) {
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
        return false;
    }
}