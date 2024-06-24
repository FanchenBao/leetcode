import java.util.*;
import java.util.stream.Stream;
import java.math.*;

/**
 * Definition for a binary tree node.
 */
//class TreeNode {
//    int val;
//    TreeNode left;
//    TreeNode right;
//    TreeNode() {}
//    TreeNode(int val) { this.val = val; }
//    TreeNode(int val, TreeNode left, TreeNode right) {
//        this.val = val;
//        this.left = left;
//        this.right = right;
//    }
//}

class Solution1 {
    public int longestSubarray(int[] nums, int limit) {
        /*
         * LeetCode 1438
         *
         * Two heaps, to keep track of the min and max of the current sliding
         * window. Very slow.
         *
         * O(NlogN), 81 ms, faster than 29.65% 
         */
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a, b) -> Integer.compare(-a[0], -b[0]));
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        int lo = 0;
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            maxHeap.add(new int[]{nums[i], i});
            minHeap.add(new int[]{nums[i], i});
            while (!maxHeap.isEmpty() && (Math.abs(nums[i] - maxHeap.peek()[0]) > limit || maxHeap.peek()[1] < lo)) {
                int[] popped = maxHeap.poll();
                lo = Math.max(lo, popped[1] + 1);
            }
            while (!minHeap.isEmpty() && (Math.abs(nums[i] - minHeap.peek()[0]) > limit || minHeap.peek()[1] < lo)) {
                int[] popped = minHeap.poll();
                lo = Math.max(lo, popped[1] + 1);
            }
            res = Math.max(res, i - lo + 1);
        }
        return res;
    }
}


class Solution2 {
    public int longestSubarray(int[] nums, int limit) {
        /*
         * Another solution, use monotonic increasing array. If the current
         * value is bigger than the end of the array, compare it with the
         * front. If the difference between them is larger than limit, we pop
         * the front. If the current value is smaller than the end of the array
         * compare it with the end. If the difference is larger than limit, we
         * start the monotonic increasing array from scratch.
         *
         * O(N)
         */
        Deque<int[]> mono = new ArrayDeque<>();
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            if (!mono.isEmpty()) {
                if (mono.getLast()[0] - nums[i] > limit) {
                    mono.clear();
                } else {
                    while (!mono.isEmpty() && mono.getLast()[0] >= nums[i])
                        mono.removeLast();
                    while (!mono.isEmpty() && nums[i] - mono.getFirst()[0] > limit)
                        mono.removeFirst();
                }
            }
            mono.add(new int[]{nums[i], i});
            res = Math.max(res, mono.getLast()[1] - mono.getFirst()[1] + 1);
        }
        return res;
    }
}




class Main{
    public static void main(String[] args) {
        String s = "acbbaca";
        String t = "aba";
        Solution sol = new Solution();
        System.out.println(sol.minWindow(s, t));
    }
}
