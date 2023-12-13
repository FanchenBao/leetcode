class Solution {
    public int maxProduct(int[] nums) {
        /*
        LeetCode 1464
        
        O(NlogN) 2 ms, faster than 70.74%
        */
        Arrays.sort(nums);
        return (nums[nums.length - 1] - 1) * (nums[nums.length - 2] - 1);
    }
}


class Solution {
    public int maxProduct(int[] nums) {
        /*
         * We will use O(N) to find the largest and the second largest values.
        */
        int max = 0;
        int secmax = 0;
        for (int n : nums) {
            if (n > max) 
                secmax = max; max = n;
            else if (n > secmax)
                secmax = n;
        }
        return (max - 1) * (secmax - 1);

    }
}

