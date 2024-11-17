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

class Solution {
    public int[] resultsArray(int[] nums, int k) {
        /*
         * LeetCode 3254
         *
         * A subarray of consecutive increasing numbers has the properties that
         * the min must be the beginning, the max must be the end, max - 
         * min + 1 = k, and there are k unique numbers in the subarray.
         *
         * Using this property, we can keep track of the min and max of each
         * subarray of length k, and check if the subarray satisfies the
         * requirement of being consecutive and increasing.
         *
         * O(Nlogk), 16 ms, faster than 5.34% 
         */
        PriorityQueue<Integer> maxH = new PriorityQueue<>((a, b) -> Integer.compare(nums[b], nums[a]));
        PriorityQueue<Integer> minH = new PriorityQueue<>((a, b) -> Integer.compare(nums[a], nums[b]));
        int[] res = new int[nums.length - k + 1];
        Arrays.fill(res, -1);
        Map<Integer, Integer> counter = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            maxH.add(i);
            minH.add(i);
            counter.put(nums[i], counter.getOrDefault(nums[i], 0) + 1);
            if (i - k >= 0) {
                counter.put(nums[i - k], counter.get(nums[i - k]) - 1);
                if (counter.get(nums[i - k]) == 0)
                    counter.remove(nums[i - k]);
            }
            while (!maxH.isEmpty() && maxH.peek() < i - k + 1)
                maxH.poll();
            while (!minH.isEmpty() && minH.peek() < i - k + 1)
                minH.poll();
            if (nums[maxH.peek()] - nums[minH.peek()] + 1 == k && maxH.peek() == i && minH.peek() == i - k + 1 && counter.size() == k)
                res[i - k + 1] = nums[maxH.peek()];
        }
        return res;
    }
}

class Solution2 {
    public int[] resultsArray(int[] nums, int k) {
        /*
         * Let's use monotonic queue to both keep track of the min and max of
         * the current subarray AND its size can be used to represent the
         * number of unique numbers in the subarray.
         *
         * O(N), 3 ms, faster than 25.19%
         */
        Deque<Integer> mon = new ArrayDeque<>(); // put indices in monotonic
        int[] res = new int[nums.length - k + 1];
        Arrays.fill(res, -1);
        for (int i = 0; i < nums.length; i++) {
            while (!mon.isEmpty() && nums[mon.getLast()] >= nums[i])
                mon.removeLast();
            mon.add(i);
            while (!mon.isEmpty() && mon.getFirst() < i - k + 1)
                mon.removeFirst();
            if (nums[mon.getLast()] - nums[mon.getFirst()] + 1 == k && mon.size() == k)
                res[i - k + 1] = nums[mon.getLast()];
        }
        return res;
    }
}


class Solution3 {
    public int[] resultsArray(int[] nums, int k) {
        /*
         * This is the official solution using just a counter for the count
         * of consecutive increasing numbers.
         *
         * The most important trick is that whenever the consecutive increasing
         * requirement is broken, we reset the counter to 1, meaning that we
         * will re-count starting from whatever number that breaks the
         * requirement. This is okay because as long as the current broken
         * pair exists in a subarray, that subarray will not have power.
         *
         * O(N), but this should be much faster than Solution2 because we do
         * not use any fancy data strcture. 1 ms, faster than 100.00%
         */
        int[] res = new int[nums.length - k + 1];
        Arrays.fill(res, -1);
        if (k == 1)
            res[0] = nums[0];
        int counter = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1] + 1)
                counter++;
            else
                counter = 1;
            if (counter >= k)
                res[i - k + 1] = nums[i];
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
