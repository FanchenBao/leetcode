class Solution {
    public int[] getSumAbsoluteDifferences(int[] nums) {
        /*
        LeetCode 1685
        
        Use prefix sum.
        
        O(N) 4 ms, faster than 65.38%
        */
        int N = nums.length;
        int[] presum = new int[N + 1];
        for (int i = 0; i < N; i++) presum[i + 1] = presum[i] + nums[i];
        int[] res = new int[N];
        for (int i = 0; i < N; i++) 
            res[i] = nums[i] * i - presum[i] + presum[N] - presum[i + 1] - nums[i] * (N - i - 1);
        return res;
    }
}


class Solution {
    public int[] getSumAbsoluteDifferences(int[] nums) {
        /*
        Update: from the official solution, we learned that there is no need to
        create a prefix sum array, because all we need is the prefix sum up to
        the current value and a total sum.
        
        3 ms, faster than 99.36%
         */
        int N = nums.length;
        int presum = 0; int total = 0;
        for (int num : nums) total += num;
        int[] res = new int[N];
        for (int i = 0; i < N; i++) {
            presum += nums[i];
            res[i] = nums[i] * i - presum - nums[i] + total - presum - nums[i] * (N - i - 1);
        }
        return res;
    }
}
