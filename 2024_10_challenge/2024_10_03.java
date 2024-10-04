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
    public int minSubarray(int[] nums, int p) {
        /*
         * LeetCode 1590
         *
         * Produce an array in which each value is the remainder of prefix sum
         * of nums divided by p.
         *
         * Then the last value of the array is the target remainder that some
         * subarray sum's remainder shall match. As we traverse through the
         * array, for each remainder, we want to find a previous remainder
         * such that the remainder of their difference divided by p is the
         * same as the target remainder. We can maintain another array to keep
         * track of the index of the latest occurrence of a remainder.
         *
         * The edge case is when the last remainder is already zero, which
         * means the sum of nums divideds p already. In that case, we return
         * zero.
         *
         * Another edge case is when we need to remove the entire nums. Since
         * this is not allowed, we shall return -1.
         *
         * Another edge case is the cumulative sum can overflow.
         *
         * Another edge case is that p can be huge, thus using an array to
         * keep track of the latest indices of all remainders is not memory
         * efficient.
         *
         * O(N), 24 ms, faster than 81.69%
         */
        int MAX = 1000000;
        int[] ps = new int[nums.length + 1];
        long curSum = 0;
        for (int i = 0; i < nums.length; i++) {
            curSum += nums[i];
            ps[i + 1] = (int)(curSum % p);
        }
        int tgt = ps[ps.length - 1];
        if (tgt == 0)
            return 0; // no need to remove any subarray
        Map<Integer, Integer> rems = new HashMap<>();
        rems.put(0, 0);
        int res = MAX;
        for (int i = 1; i < ps.length; i++) {
            int match = ps[i] >= tgt ? ps[i] - tgt : p + ps[i] - tgt;
            res = Math.min(res, i - rems.getOrDefault(match, -MAX));
            rems.put(ps[i], i);
        }
        return res == nums.length ? -1 : res;
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
