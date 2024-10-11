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
    public int maxWidthRamp(int[] nums) {
        /*
         * LeetCode 962
         *
         * Do a suffix max from right to left on nums. Use a TreeMap to keep
         * track of the last index of each occurrence of new max value.
         *
         * Then go from left to right to find the smallest key in the TreeMap
         * that is bigger than the current value. This guarantees that the
         * smallest big key has the max index.
         *
         * O(NlogN), 119 ms, faster than 5.97%
         */
        TreeMap<Integer, Integer> lastIndices = new TreeMap<>();
        int max = -1;
        for (int i = nums.length - 1; i >= 0; i--) {
            max = Math.max(nums[i], max);
            if (!lastIndices.containsKey(max))
                lastIndices.put(max, i);
        }
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            Integer ceil = lastIndices.ceilingKey(nums[i]);
            if (ceil != null)
                res = Math.max(lastIndices.get(ceil) - i, res);
        }
        return res;
    }
}


class Solution2 {
    public int maxWidthRamp(int[] nums) {
        /*
         * Use a suffix max and a prefix min. We can solve the problem in O(N)
         *
         * 4 ms, faster than 84.83%
         */
        int N = nums.length;
        int[] suffixMax = new int[N];
        suffixMax[N - 1] = nums[N - 1];
        for (int i = N - 2; i >= 0; i--)
            suffixMax[i] = Math.max(suffixMax[i + 1], nums[i]);
        int j = 0; // suffix Max
        int pm = Integer.MAX_VALUE;
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            pm = Math.min(pm, nums[i]);
            while (j < nums.length && suffixMax[j] >= pm)
                j++;
            res = Math.max(res, j - i - 1);
        }
        return res;
    }
}


class Solution3 {
    public int maxWidthRamp(int[] nums) {
        /*
         * No need to use prefix min. We just go through every
         * value in nums and compare it to the suffix max array.
         */
        int N = nums.length;
        int[] suffixMax = new int[N];
        suffixMax[N - 1] = nums[N - 1];
        for (int i = N - 2; i >= 0; i--)
            suffixMax[i] = Math.max(suffixMax[i + 1], nums[i]);
        int j = 0; // suffix Max
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            while (j < nums.length && suffixMax[j] >= nums[i])
                j++;
            res = Math.max(res, j - i - 1);
        }
        return res;
    }
}


class Solution4 {
    public int maxWidthRamp(int[] nums) {
        /*
         * This is the monotonic decreasing stack solution from the official
         * solution. It pushes not the value but the index of the value in
         * the monotonic decreasing stack.
         */
        Stack<Integer> mon = new Stack<>(); // monotonic decreasing array with indices
        for (int i = 0; i < nums.length; i++) {
            if (mon.isEmpty() || nums[mon.peek()] > nums[i])
                mon.add(i);
        }
        int res = 0;
        for (int i = nums.length - 1; i >= 0; i--) {
            // go from right to left. Pop the stack if the top of the stack
            // is smaller or equal to nums[i]. Each popped indices can be
            // used to compute the width
            while (!mon.isEmpty() && nums[mon.peek()] <= nums[i])
                res = Math.max(res, i - mon.pop());
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
