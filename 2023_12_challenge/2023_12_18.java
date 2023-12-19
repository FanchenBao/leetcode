class Solution {
    public int maxProductDifference(int[] nums) {
        /*
        LeetCode 1913
        
        Find the two smallest and the two largest.
        
        But it is not as easy as I had expected. For one, the initial
        values for min, secMin, and max, secMax need to be carefully
        configured. For another, the processing of max and min has to
        be separated.
        
        O(N), 3 ms, faster than 86.05%
         */
        int min = Math.min(nums[0], nums[1]); int secMin = Math.max(nums[0], nums[1]);
        int max = secMin; int secMax = min;
        for (int i = 2; i < nums.length; i++) {
            // handle the min
            if (nums[i] < min) {
                secMin = min;
                min = nums[i];
            } else if (nums[i] < secMin) {
                secMin = nums[i];
            }
            // handle the max
            if (nums[i] > max) {
                secMax = max;
                max = nums[i];
            } else if (nums[i] > secMax) {
                secMax = nums[i];
            }
        }
        return max * secMax - min * secMin;
    }
}

