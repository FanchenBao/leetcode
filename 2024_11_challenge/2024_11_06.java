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
    public boolean canSortArray(int[] nums) {
        /*
         * LeetCode 3011
         *
         * Within a subarray of numbers of the same bit count, they can always
         * be sorted because there is no restriction on swapping.
         *
         * Between subarrays of different bit count, there is no way to swap
         * across the different subarrays. Hence, for these subarrays to be
         * sorted, the max of the previous subarray must not be bigger than
         * the min of the current subarray.
         *
         * O(N), 1 ms, faster than 100.00%
         */
        int preMax = 0;
        int min = nums[0];
        int max = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (Integer.bitCount(nums[i]) == Integer.bitCount(nums[i - 1])) {
                min = Math.min(min, nums[i]);
                max = Math.max(max, nums[i]);
            } else if (min >= preMax) {
                preMax = max;
                min = nums[i];
                max = nums[i];
            } else {
                return false;
            }
        }
        return min >= preMax;
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
