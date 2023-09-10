class Solution1 {
    Integer[][] memo;
    int[] nums;

    int dp(int idx, int tgt) {
        if (idx == nums.length || nums[idx] > tgt) {
            return 0;
        }
        if (tgt == nums[idx]) {
            return 1;
        }
        if (memo[idx][tgt] == null) {
            memo[idx][tgt] = 0;
            for (int i = 0; i < nums.length; i++) {
                memo[idx][tgt] += dp(i, tgt - nums[idx]);
            }
        }
        return memo[idx][tgt];
    }

    public int combinationSum4(int[] nums, int target) {
        /*
        LeetCode 377

        DP(idx, tgt) = number of combinations to make up tgt with nums[idx] as the first value.

        O(N^2T), where N = len(nums) and T = target. 15 ms, faster than 5.16%
         */
        Arrays.sort(nums);
        this.nums = nums;
        memo = new Integer[nums.length][target + 1];
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            res += dp(i, target);
        }
        return res;
    }
}


class Solution2 {
    Integer[] memo;
    int[] nums;

    int dp(int tgt) {
        if (tgt < 0) {return 0;}
        if (tgt == 0) {return 1;}
        if (memo[tgt] == null) {
            memo[tgt] = 0;
            for (int num : nums) {
                memo[tgt] += dp(tgt - num);
            }
        }
        return memo[tgt];
    }

    public int combinationSum4(int[] nums, int target) {
        /*
        I did not get this way of DP thinking. Basically it is a 1D DP.
        We call dp(tgt) to find the total number of combinations to make
        tgt using the entire range of nums.
        
        To get dp(tgt), we can choose to remove any number, and call dp(tgt - num)
        for the next iteration. That's it.
        
        O(N*T), 0 ms, faster than 100.00% 
        */
        this.nums = nums;
        memo = new Integer[target + 1];
        return dp(target);
    }
}
