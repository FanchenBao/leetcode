class Solution {
    public int minOperations(int[] nums, int x) {
        /*
        LeetCode 1658
        
        DP is not gonna work because we need two indices for state, and that would make the runtime O(N^2).
        
        Binary search is not gonna work because the check for a given number of possible answer is not O(N).
        
        Then the intuition is that we are basically doing a prefix sum and suffix sum, and we are trying to solve a
        two-sum problem with the prefix and suffix sum. So, we can produce the prefix sum until it exceeds x. We can
        then preoduce suffix sum in a map to facilitate the two-sum algorithm. Then viola, we are done!
        
        O(N), 54 ms, faster than 26.67% 
         */
        List<Integer> left = new ArrayList<>();
        left.add(0);
        Map<Integer, Integer> right = new HashMap<>();
        right.put(0, 0);
        // build the prefix sum
        int last = 0;
        for (int i = 0; i < nums.length && last + nums[i] <= x; i++) {
            last += nums[i];
            left.add(last);
        }
        // build the suffix sum
        last = 0;
        for (int i = nums.length - 1; i >= 0 && nums[i] + last <= x; i--) {
            last += nums[i];
            right.put(last, nums.length - i);
        }
        int MAX = nums.length + 1;
        int res = MAX;
        for (int j = 0; j < left.size(); j++) {
            res = Math.min(res, j + right.getOrDefault(x - left.get(j), MAX));
        }
        return res < MAX ? res : -1;
    }
}


class Solution {
    public int minOperations(int[] nums, int x) {
        /*
        No need to build the prefix sum array.
        */
        Map<Integer, Integer> right = new HashMap<>();
        right.put(0, 0);
        // build the suffix sum
        int last = 0;
        for (int i = nums.length - 1; i >= 0 && nums[i] + last <= x; i--) {
            last += nums[i];
            right.put(last, nums.length - i);
        }
        int MAX = nums.length + 1;
        int res = right.getOrDefault(x, MAX);
        last = 0;
        for (int j = 0; j < nums.length && last + nums[j] <= x; j++) {
            last += nums[j];
            res = Math.min(res, j + 1 + right.getOrDefault(x - last, MAX));
        }
        return res < MAX ? res : -1;
    }
}


class Solution {
    public int minOperations(int[] nums, int x) {
        /*
        This is another way to implement something very similar to what we have tried before. Instead of a two sum
        problem using prefix and suffix sum, we can do a two sum problem still with just the prefix sum. The key idea
        is the to find some prefix and suffix sum to equal x is equivalent to find some stretch of the values in the
        middle adding up to sum(nums) - x. Then we can do prefix sum, record all the positions of the previous prefix
        sum, and do two-sum to find where the match is going to be.

        This probably has an easier implementation.
        
        O(N), 66 ms, faster than 17.50%
         */
        Map<Integer, Integer> presumPos = new HashMap<>();
        int total = 0; for (int n : nums) {total += n;}
        presumPos.put(0, -1);
        int cur = 0;
        int MAX = nums.length + 1;
        int res = MAX;
        int tgt = total - x;
        for (int i = 0; i < nums.length; i++) {
            cur += nums[i];
            presumPos.put(cur, i);
            if (presumPos.containsKey(cur - tgt)) {
                int j = presumPos.get(cur - tgt);
                res = Math.min(res, nums.length - i + j);
            }
        }
        return res < MAX ? res : -1;
    }
}
