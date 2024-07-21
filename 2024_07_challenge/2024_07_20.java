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
    int[][] res;
    private void solve(int i, int j, int[] rowSum, int[] colSum) {
        if (i >= res.length || j >= res[0].length)
            return;
        if (rowSum[i] <= colSum[j]) {
            this.res[i][j] = rowSum[i];
            colSum[j] -= rowSum[i];
            solve(i + 1, j, rowSum, colSum);
        } else {
            this.res[i][j] = colSum[j];
            rowSum[i] -= colSum[j];
            solve(i, j + 1, rowSum, colSum);
        }
    }

    public int[][] restoreMatrix(int[] rowSum, int[] colSum) {
        /*
         * LeetCode 1605
         *
         * We always set the top left cell with the min row or col sum for its
         * corresponding row and col. After that, we essentially remove the
         * row or col that has just been fulfilled, update the row or col sum
         * on the other side, and move the top left position accordingly.
         *
         * O(MN), 1 ms, faster than 100.00%
         */
        int M = rowSum.length;
        int N = colSum.length;
        this.res = new int[M][N];
        solve(0, 0, rowSum, colSum);
        return this.res;
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
