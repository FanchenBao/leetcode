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
    public int minPatches(int[] nums, int n) {
        /*
         * LeetCode 330
         *
         * Find the max reach all the numbers from nums[i] towards the current
         * can get. If this max reach overlaps with nums[i + 1], then we can
         * extend the reach by doing reach + nums[i + 1]. Otherwise, we have
         * a gap and need to fill in some values. The value to put in must not
         * create a gap from the reach. Thus the only one we can use is
         * reach + 1. This will extend the reach to reach + reach + 1. Then we
         * can check with nums[i + 1] again.
         *
         * We keep going until the reach exceeds n.
         *
         * 0 ms, faster than 100.00%
         */
        int res = 0;
        long reach = 0;
        int i = 0;
        while (reach < n) {
            if (i < nums.length && nums[i] - reach <= 1) {
                // no gap
                reach += (long)nums[i];
                i++;
            } else {
                reach += reach + (long)1;
                res++;
            }
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
