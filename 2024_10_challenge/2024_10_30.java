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
    public int minimumMountainRemovals(int[] nums) {
        /*
         * LeetCode 1671
         *
         * Find the longest monotonic increasing array from left to right
         * ending at each nums[i]. Save it in monLen array such that monLen[i]
         * is the max length.
         *
         * Do the same thing from right to left, and for each nums[i], we know
         * its longest length monotonic increasing array (right to left) and
         * its longest length left to right. Therefore, the longest mountain
         * array with nums[i] as the peak is the left to right length plus
         * the right to left length minus one.
         *
         * O(N^2), 36 ms, faster than 65.71%
         */
        int N = nums.length;
        int[] monLen = new int[N]; // monLenLR[i] = max length of mon-increasing ending at nums[i]
        // mon-increasing array from left to right
        // BUT, we do not pop!
        for (int i = 0; i < N; i++) {
            monLen[i] = 1;
            for (int j = i - 1; j >= 0; j--) {
                if (nums[j] < nums[i])
                    monLen[i] = Math.max(monLen[i], monLen[j] + 1);
            }
        }
        // mon-increasing array from right to left. We will reuse monLen and
        // update it in-place for right to left traversal.
        int longest = 0;
        for (int i = N - 1; i >= 0; i--) {
            int len = 1;
            for (int j = i + 1; j < N; j++) {
                if (nums[j] < nums[i])
                    len = Math.max(len, monLen[j] + 1);
            }
            if (monLen[i] > 1 && len > 1)
                // both left to right and right to left mon-array must be
                // of length at least 2
                longest = Math.max(longest, len + monLen[i] - 1);
            monLen[i] = len;
        }
        return N - longest;
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
