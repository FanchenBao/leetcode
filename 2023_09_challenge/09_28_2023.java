class Solution {
    public int[] sortArrayByParity(int[] nums) {
        /*
        LeetCode 905
        
        O(N), 0 ms, faster than 100.00%
        */
        int i = 0; int j = nums.length - 1; int tmp;
        while (i < j) {
            if (nums[j] % 2 == 0) {
                tmp = nums[i];
                nums[i] = nums[j];
                nums[j] = tmp;
                i++;
            } else {
                j--;
            }
        }
        return nums;
    }
}