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
    public long maxMatrixSum(int[][] matrix) {
        /*
         * LeetCode 1975
         *
         * The key is to realize that as long as there are even number of
         * negatives, they can always be converted to positives. Thus, if the
         * total count of negatives is even, the result is the sum of the
         * absolute values of everything in the matrix.
         *
         * Otherwise, one value must be negative. To make the total sum max,
         * we pick the smallest absolute value to assign the negative sign.
         *
         * O(N^2), 4 ms, faster than 99.19%
         */
        long s = 0;
        int min = 1000000;
        int cntNeg = 0;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix.length; j++) {
                int v = matrix[i][j];
                if (v < 0) {
                    cntNeg++;
                    v = -v;
                }
                s += (long)v;
                min = Math.min(min, v);
            }
        }
        if (cntNeg % 2 == 0)
            return s;
        return s - 2 * (long)min;
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
