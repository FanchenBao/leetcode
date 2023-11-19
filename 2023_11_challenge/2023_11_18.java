class Solution {
    public int maxFrequency(int[] nums, int k) {
        /*
        LeetCode 1838

        This is the perfect example of a medium problem. Solved with two pointers.
        We sort nums first. It is easy to see that if nums[j] is the value with the max possible frequency,
        all the numbers that add up to nums[j] must lie immediately to the left of nums[j]. Thus, we can
        use nums[i] to mark the beginning of the subarray with the max possible length.

        If we use kk to record the total number of operations needed to achieve the max possible frequency,
        as we move j forward, each forward move would incur in total kk + (j - i + 1) * (nums[j + 1] - nums[j])
        If this new operation cost is smaller or equal to k, we don't have to shrink the subarray. Otherwise,
        we move i forward and reduce the new operation cost, until the cost drops below k. Then we have
        the max possible frequency ending at nums[j + 1].

        O(NlogN), 29 ms, faster than 72.60%
         */
        Arrays.sort(nums);
        int i = 0; // index of the left end
        int c = 1; // the max frequency achievable if every possible numbers increase to nums[j]
        int kk = 0; // the amount of operations needed to achieve c
        int res = 1;
        for (int j = 1; j < nums.length; j++) {
            kk += c * (nums[j] - nums[j - 1]);
            while (kk > k && i < j)
                kk -= nums[j] - nums[i++];
            c = j - i + 1;
            res = Math.max(res, c);
        }
        return res;
    }
}


class Solution {
    public int maxFrequency(int[] nums, int k) {
        /*
        This is the extended sliding window from the official solution.
        
        The key is that we do NOT have to shrink the window because we don't care for a
        smaller window size. All we need to do is to expand it whenever possible.

        O(NlogN), 27 ms, faster than 98.03%
         */
        Arrays.sort(nums);
        int i = 0; // index of the left end
        int windowSum = 0;
        for (int j = 0; j < nums.length; j++) {
            windowSum += nums[j];
            if (nums[j] * (j - i + 1) - windowSum > k)
                // Current window contains too many operations, we simply move the
                // window forward
                windowSum -= nums[i++];
        }
        return nums.length - i;
    }
}
