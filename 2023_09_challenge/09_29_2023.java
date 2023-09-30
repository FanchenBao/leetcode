class Solution {
    public boolean isMonotonic(int[] nums) {
        /*
        LeetCode 896
        O(N) 2 ms, faster than 62.86%
        */
        if (nums.length == 1) {return true;}
        int i = 1;
        while (i < nums.length && nums[i] == nums[i - 1]) {
            i++;
        }
        if (i == nums.length) {return true;}
        boolean trend = nums[i] - nums[i - 1] > 0;
        while (i < nums.length) {
            if (nums[i] != nums[i - 1] && (nums[i] - nums[i - 1] > 0) != trend) {return false;}
            i++;
        }
        return true;
    }
}


class Solution {
    public boolean isMonotonic(int[] nums) {
        if (nums.length == 1) {return true;}
        int sign = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) {
                if (sign == 0) {
                    sign = nums[i] > nums[i - 1] ? 1 : -1;
                } else if (nums[i] > nums[i - 1] != sign > 0) {
                    return false;
                }
            }
        }
        return true;
    }
}
