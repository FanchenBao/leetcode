class Solution {
    public int constrainedSubsetSum(int[] nums, int k) {
        /*
        LeetCode 1425

        DP, where DP[i] is the max sum that satisfies the requirement in nums[:i + 1].
        Then use max heap to keep track of the max dp value in the sliding window nums[i - k:i + 1].

        O(NlogN), 101 ms, faster than 11.81%
         */
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(tup -> -tup[0]));
        pq.add(new int[]{nums[0], 0})
        int res = nums[0]; int cur;
        for (int i = 1; i < nums.length; i++) {
            cur = Math.max(nums[i], nums[i] + pq.peek()[0]);
            res = Math.max(cur, res);
            while (!pq.isEmpty() && pq.peek()[1] <= i - k) pq.poll();
            pq.add(new int[]{cur, i});
        }
        return res;
    }
}


class Solution {
    public int constrainedSubsetSum(int[] nums, int k) {
        /*
        Using TreeMap, which maintains the order of the keys. If we put DP values as keys, we will always be able to
        obtain the max DP value in the sliding window. We treat the TreeMap as a counter, so that when we remove a
        value from the TreeMap, we first decrement its count. If the count becomes zero, we remove that key-value pair.

        O(NlogK), 358 ms, faster than 5.51% 
         */
        TreeMap<Integer, Integer> counter = new TreeMap<>();
        int[] dp = new int[nums.length]; dp[0] = nums[0];
        int res = nums[0];
        counter.put(nums[0], 1);
        for (int i = 1; i < nums.length; i++) {
            dp[i] = Math.max(nums[i], counter.lastKey() + nums[i]);
            res = Math.max(res, dp[i]);
            counter.put(dp[i], counter.getOrDefault(dp[i], 0) + 1);
            if (i >= k) {
                counter.put(dp[i - k], counter.get(dp[i - k]) - 1);
                if (counter.get(dp[i - k]) == 0) counter.remove(dp[i - k]);
            }
        }
        return res;
    }
}


class Solution {
    public int constrainedSubsetSum(int[] nums, int k) {
        /*
        Monotonic decreasing deque

        O(N), 36 ms, faster than 70.87% 
         */
        Deque<int[]> mon = new LinkedList<>();
        int res = nums[0]; int cur;
        mon.addLast(new int[]{nums[0], 0});
        for (int i = 1; i < nums.length; i++) {
            cur = Math.max(nums[i], mon.getFirst()[0] + nums[i]);
            res = Math.max(res, cur);
            // Add cur
            while (!mon.isEmpty() && mon.getLast()[0] <= cur) mon.removeLast();
            mon.addLast(new int[]{cur, i});
            // remove any element that is outside the current sliding window
            while (!mon.isEmpty() && mon.getFirst()[1] <= i - k) mon.removeFirst();
        }
        return res;
    }
}


class Solution {
    public int constrainedSubsetSum(int[] nums, int k) {
        /*
        Monotonic decreasing deque. Use ArrayDeque is even faster.

        O(N), 33 ms, faster than 94.49%
         */
        Deque<int[]> mon = new ArrayDeque<>();
        int res = nums[0]; int cur;
        mon.addLast(new int[]{nums[0], 0});
        for (int i = 1; i < nums.length; i++) {
            cur = Math.max(nums[i], mon.getFirst()[0] + nums[i]);
            res = Math.max(res, cur);
            // Add cur
            while (!mon.isEmpty() && mon.getLast()[0] <= cur) mon.removeLast();
            mon.addLast(new int[]{cur, i});
            // remove any element that is outside the current sliding window
            while (!mon.isEmpty() && mon.getFirst()[1] <= i - k) mon.removeFirst();
        }
        return res;
    }
}
