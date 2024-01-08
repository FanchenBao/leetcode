class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        /*
        LeetCode 446
        
        Very convoluted solution, in which dp[i] is a map with
        difference as its key and another map as its value. The
        second level map is a counter to count the frequency of
        certain length of arithmetic subseq ending at nums[i]
        with a given difference.
        */
        int N = nums.length;
        // dp[i] = {diff: {length: count of arith subseq of such length}}
        List<Map<Long, Map<Integer, Integer>>> dp = new ArrayList<>();
        int res = 0;
        for (int i = 0; i < N; i++) {
            // Initialization
            dp.add(new HashMap<>());
            dp.get(i).put((long)0, new HashMap<>());
            dp.get(i).get((long)0).put(1, 1); // diff 0 always has one subseq of length 1
            for (int j = i - 1; j >= 0; j--) {
                long di = (long)nums[i] - nums[j];
                dp.get(i).putIfAbsent(di, new HashMap<>());
                Map<Integer, Integer> iC = dp.get(i).get(di);
                iC.put(1, 1); // any diff has one subseq of length 1
                if (dp.get(j).containsKey(di)) {
                    Map<Integer, Integer> jC = dp.get(j).get(di);
                    for (int l : jC.keySet()) {
                        iC.put(l + 1, iC.getOrDefault(l + 1, 0) + jC.get(l));
                        if (l + 1 >= 3)
                            res += jC.get(l);
                    }
                } else {
                    iC.put(2, iC.getOrDefault(2, 0) + 1);
                }
            }
        }
        return res;
    }
}


class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        /*
        Much better method, copied from the last time when I solved
        this problem. The DP can be very simple, where dp[i] is
        a counter to keep track of the number of arithmetic subseq
        of length 2 or more for each difference. That's it.

        Each time a new nums[i] is encountered, we go back the array
        and add all the count of previous subseq of the same difference.
        
        O(N^2), 202 ms, faster than 36.63%
         */
        // dp[i] = {diff: count}
        List<Map<Long, Integer>> dp = new ArrayList<>();
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            dp.add(new HashMap<>());
            for (int j = i - 1; j >= 0; j--) {
                long di = (long)nums[j] - nums[i];
                // No need to check the length, because if
                // dp[j][di] is larger than 0, that means
                // the subseq ending at nums[j] has at least
                // two values. Adding the current one would
                // satisfy the requirement of arithematic subseq.
                res += dp.get(j).getOrDefault(di, 0);
                dp.get(i).put(di, dp.get(i).getOrDefault(di, 0) + dp.get(j).getOrDefault(di, 0) + 1);
            }
        }
        return res;
    }
}

