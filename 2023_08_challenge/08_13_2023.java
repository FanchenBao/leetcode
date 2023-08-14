class Solution1 {

    Boolean[] memo;
    int[] nums;

    private boolean dp(int idx) {
        if (idx == nums.length) {
            return true;
        }
        if (idx == nums.length - 1) {
            return false;
        }
        if (memo[idx] != null) {
            return memo[idx];
        }
        memo[idx] = false;
        // op1, identical tuple
        if (nums[idx] == nums[idx + 1]) {
            memo[idx] |= dp(idx + 2);
        }
        // op2, identical triplet, or op3 consecutive increasing triplet
        if (idx + 2 < nums.length && (nums[idx] == nums[idx + 1] && nums[idx + 1] == nums[idx + 2]) | (nums[idx + 1] == nums[idx] + 1 && nums[idx + 2] == nums[idx + 1] + 1)) {
            memo[idx] |= dp(idx + 3);
        }
        return memo[idx];
    }
    public boolean validPartition(int[] nums) {
        /*
        LeetCode 2369

        Pretty naive DP, in which DP(idx) is whether it is possible to partition nums[idx:].

        O(N), 13 ms, faster than 34.95%
         */
        memo = new Boolean[nums.length];
        this.nums = nums;
        return dp(0);
    }
}


class Solution2 {
    public boolean validPartition(int[] nums) {
        /*
        Bottom up
        
        O(N). 6 ms, faster than 92.23%
        
        From previous days of experience, in Java, bottom up is much faster than top down in DP.
         */
        boolean[] dp = new boolean[nums.length + 1];
        dp[nums.length] = true;
        dp[nums.length - 1] = false;
        for (int i = nums.length - 2; i >= 0; i--) {
            if (nums[i] == nums[i + 1]) {
                dp[i] = dp[i + 2];
                if (i + 2 < nums.length && nums[i + 1] == nums[i + 2]) {
                    dp[i] |= dp[i + 3];
                }
            } else if (i + 2 < nums.length && nums[i + 1] == nums[i] + 1 && nums[i + 2] == nums[i + 1] + 1) {
                dp[i] = dp[i + 3];
            }
        }
        return dp[0];
    }
}

class Solution3 {
    public boolean validPartition(int[] nums) {
        /*
        Bottom up, with space optimization. No need to create an array. All we need is two additional
        values, i.e. to compute dp[idx], we need dp[idx + 2] and dp[idx + 3]

        O(N), 7 ms, faster than 82.52% 
        O(1) space complexity.
         */
        boolean nxt = false; boolean nnxt = true; boolean nnnxt = true;
        for (int i = nums.length - 2; i >= 0; i--) {
            boolean cur = false;
            if (nums[i] == nums[i + 1]) {
                cur |= nnxt;
                if (i + 2 < nums.length && nums[i + 1] == nums[i + 2]) {
                    cur |= nnnxt;
                }
            } else if (i + 2 < nums.length && nums[i + 1] == nums[i] + 1 && nums[i + 2] == nums[i + 1] + 1) {
                cur |= nnnxt;
            }
            nnnxt = nnxt; nnxt = nxt; nxt = cur;

        }
        return nxt;
    }
}

