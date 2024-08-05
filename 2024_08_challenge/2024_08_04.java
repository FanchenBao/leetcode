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
    private int slidingWindow(int size, int sumsIdx, int[] sums, int[] nums) {
        int s = 0;
        int i = 0;
        for (int j = 0; j < nums.length; j++) {
            s += nums[j];
            if (j - i + 1 == size) {
                sums[sumsIdx++] = s;
                s -= nums[i++];
            }
        }
        return sumsIdx;
    }

    public int rangeSum(int[] nums, int n, int left, int right) {
        /*
         * LeetCode 1508
         *
         * Sliding window to produce the sums of all continous subarrays.
         *
         * O(N^2logN), 58 ms, faster than 89.64%
         */
        int[] sums = new int[n * (n + 1) / 2];
        int sumsIdx = 0;
        for (int size = 1; size <= n; size++)
            sumsIdx = slidingWindow(size, sumsIdx, sums, nums);
        Arrays.sort(sums);
        int res = 0;
        int MOD = 1000000007;
        for (int i = left - 1; i < right; i++)
            res = (res + sums[i]) % MOD;
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
