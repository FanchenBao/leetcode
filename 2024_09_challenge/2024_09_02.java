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
    public int chalkReplacer(int[] chalk, int k) {
        /*
         * LeetCode 1894
         *
         * Prefix sum on chalk and then binary search to find which index has
         * the value larger than total chalk sum MOD k.
         *
         * O(N + logN), 2 ms, faster than 72.59%
         */
        int N = chalk.length;
        long[] presum = new long[N];
        presum[0] = (long)chalk[0];
        for (int i = 1; i < N; i++)        
            presum[i] = presum[i - 1] + (long)chalk[i];
        int idx = Arrays.binarySearch(presum, k % presum[N - 1]);
        return (idx < 0 ? -(idx + 1) : idx + 1) % N;
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
