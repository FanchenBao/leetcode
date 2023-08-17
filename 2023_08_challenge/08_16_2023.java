class Solution1 {
    public int[] maxSlidingWindow(int[] nums, int k) {
        /*
        LeetCode 239
        
        Use max heap to keep track of the max value within each window.
        
        O(NlogN), 90 ms, faster than 18.04%
         */
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>(Comparator.comparingInt(a -> -a[0]));
        int[] res = new int[nums.length - k + 1];
        for (int i = 0; i < k; i++) {
            maxHeap.add(new int[]{nums[i], i});
        }
        res[0] = maxHeap.peek()[0];
        for (int i = k; i < nums.length; i++) {
            maxHeap.add(new int[]{nums[i], i});
            while (!maxHeap.isEmpty() && maxHeap.peek()[1] < i - k + 1) {
                maxHeap.poll();
            }
            res[i - k + 1] = maxHeap.peek()[0];
        }
        return res;
    }
}


class Solution2 {
    public int[] maxSlidingWindow(int[] nums, int k) {
        /*
        Monotonic decrease deque to keep track of the max value in each window.
        
        O(N), 30 ms, faster than 87.28%
         */
        Deque<int[]> deque = new ArrayDeque<>();
        int[] res = new int[nums.length - k + 1];
        for (int i = 0; i < nums.length; i++) {
            while (!deque.isEmpty() && nums[i] >= deque.getLast()[0]) {
                deque.removeLast();
            }
            deque.addLast(new int[]{nums[i], i});
            while (!deque.isEmpty() && deque.getFirst()[1] < i - k + 1) {
                deque.removeFirst();
            }
            if (i - k + 1 >= 0) {
                res[i - k + 1] = deque.getFirst()[0];
            }
        }
        return res;
    }
}
