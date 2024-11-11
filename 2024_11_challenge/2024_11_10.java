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
    private int convert(int[] counter) {
        int res = 0;
        for (int i = 0; i < counter.length; i++) {
            if (counter[counter.length - 1 - i] > 0)
                res |= (1 << i);
        }
        return res;
    }

    private void update(int[] counter, int n, int delta) {
        int i = counter.length - 1;
        while (n > 0) {
            if ((n & 1) > 0)
                counter[i] += delta;
            i--;
            n >>= 1;
        }
    }

    public int minimumSubarrayLength(int[] nums, int k) {
        /*
         * LeetCode 3097
         *
         * Two pointer + sliding window. The tricky part is to enable sliding
         * window on cumulative OR. Here we use a counter to simulate OR. This
         * way we are able to delete a number while keeping the cumulative OR
         * of the remaining numbers.
         *
         * O(32N), 45 ms, faster than 88.89%
         */
        int[] counter = new int[32];
        int i = 0;
        int res = Integer.MAX_VALUE;
        for (int j = 0; j < nums.length; j++) {
            update(counter, nums[j], 1);
            while (convert(counter) >= k && i <= j) {
                res = Math.min(res, j - i + 1);
                update(counter, nums[i++], -1);
            }
        }
        return res == Integer.MAX_VALUE ? -1 : res;
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
