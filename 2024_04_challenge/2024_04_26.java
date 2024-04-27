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
    private void updateMinAndSecMin(int val, int idx, int[] minAndSecMin) {
        if (val < minAndSecMin[0]) {
            minAndSecMin[2] = minAndSecMin[0];
            minAndSecMin[0] = val;
            minAndSecMin[1] = idx;
        } else if (val < minAndSecMin[2]) {
            minAndSecMin[2] = val;
        }
    }

    public int minFallingPathSum(int[][] grid) {
        /*
         * LeetCode 1289
         *
         * DP. We can use grid as the DP table and change it in-place. The
         * goal is to compute dp[i][j] such that it contains the smallest sum
         * of a falling path ending at positin (i, j)
         *
         * To do so, we need the min falling path on the previous row that is
         * not on the same colum as the current cell. So we produce a min sum
         * and second min sum for each row. If the current cell does not fall
         * on the same column as the min sum, we always use the min sum of the
         * previous row. Otherwise, we use the second min sum.
         *
         * O(N^2), 4 ms, faster than 90.82% 
         */
        // minAndSecMin is an array of [min, minIdx, secMin]
        int[] minAndSecMin = new int[]{1000000000, -1, 1000000000};
        int N = grid.length;
        for (int j = 0; j < N; j++)
            updateMinAndSecMin(grid[0][j], j, minAndSecMin);
        for (int i = 1; i < N; i++) {
            int[] tmp = new int[]{1000000000, -1, 1000000000};
            for (int j = 0; j < N; j++) {
                if (j != minAndSecMin[1])
                    grid[i][j] += minAndSecMin[0];
                else
                    grid[i][j] += minAndSecMin[2];
                updateMinAndSecMin(grid[i][j], j, tmp);
            }
            minAndSecMin = tmp;
        }
        return minAndSecMin[0];
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
