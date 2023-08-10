import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

class Solution1 {
    Integer[] memo;

    private int dp(int idx, int[] nums, int maxDiff) {
        /*
        dp(i) is the max number of pairs in nums that are smaller or equal to maxDiff
         */
        if (idx >= nums.length - 1) {
            return 0;
        }
        if (memo[idx] != null) {
            return memo[idx];
        }
        memo[idx] = Math.max(
                // Op1, do not consider the pair (nums[idx], nums[idx + 1])
                dp(idx + 1, nums, maxDiff),
                // Op2, consider the current pair
                (Math.abs(nums[idx] - nums[idx + 1]) <= maxDiff ? 1 : 0) + dp(idx + 2, nums, maxDiff)
        );
        return memo[idx];
    }
    public int minimizeMax(int[] nums, int p) {
        /*
        LeetCode 2616

        Use binary search to find the min max diff. Use DP to find the max number of pairs that can satisfy
        the current diff. If the max number of pairs is larger or equal to p, we can shrink the diff even
        more. Otherwise, we have to increase the diff.

        O(NlogN), 246 ms, faster than 5.63%
         */
        Arrays.sort(nums);
        int lo = 0;
        int hi = nums[nums.length - 1] - nums[0] + 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            memo = new Integer[nums.length];
            if (dp(0, nums, mid) >= p) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
}


class Solution2 {
    public int minimizeMax(int[] nums, int p) {
        /*
        No need for DP. We can use greedy. For any adjacent triplet in nums, we can only pick one pair, either
        (a0, a1) or (a1, a2). Thus, it doesn't matter which pair we pick (i.e., picking the first pair and thus
        excluding the second pair would not have any impact in the overall analysis). Thus, for any given diff,
        we simply go through nums and always pick the first pair that has diff smaller or equal to the given diff.

        O(NlogN + NlogM), where M is the diff between the min and max of nums. 16 ms, faster than 99.38% 
         */
        Arrays.sort(nums);
        int lo = 0;
        int hi = nums[nums.length - 1] - nums[0] + 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            int maxPairs = 0;
            for (int i = 0; i < nums.length - 1;) {
                if (nums[i + 1] - nums[i] <= mid) {
                    maxPairs += 1;
                    i += 2;
                } else {
                    i += 1;
                }
            }
            if (maxPairs >= p) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
}
