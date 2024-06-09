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
    public boolean checkSubarraySum(int[] nums, int k) {
        /*
         * LeetCode 523
         *
         * Create prefix sum and then take remainder of each value MOD k.
         * A subarray sum that is divisible by k shows up if there are two
         * remainder values of the prefix sum that are identical and differ in
         * position by more than or equal to 2.
         *
         * O(N), 24 ms, faster than 44.31%
         */
        // record the first position of all remainders
        Map<Integer, Integer> rems = new HashMap<>();
        rems.put(0, 0);
        int presum = 0;
        for (int i = 0; i < nums.length; i++) {
            presum += nums[i];
            int r = presum % k;
            if (rems.getOrDefault(r, -1) < 0)
                rems.put(r, i + 1);  // the position of remainder is 1-based
            else if (i + 1 - rems.get(r) >= 2)
                return true;
        }
        return false;
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
