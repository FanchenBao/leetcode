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
    public int countSquares(int[][] matrix) {
        /*
         * LeetCode 1277
         *
         * Use 2D prefix sum for each cell. Then at each cell, check if a
         * square can be formed with the cell being the bottom right corner.
         *
         * O(MN * min(M, N)), 9 ms, faster than 14.63%
         */
        int M = matrix.length;
        int N = matrix[0].length; 
        for (int i = 0; i < M; i++) {
            int psum = 0;
            for (int j = 0; j < N; j++) {
                psum += matrix[i][j];
                matrix[i][j] = psum + (i > 0 ? matrix[i - 1][j] : 0);
            }
        }
        int res = 0;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                int side = 1;
                while (side * side <= matrix[i][j]) {
                    int top = i - side >= 0 ? matrix[i - side][j] : 0;
                    int left = j - side >= 0 ? matrix[i][j - side] : 0;
                    int diag = (i - side >= 0 && j - side >= 0) ? matrix[i - side][j - side] : 0;
                    if (matrix[i][j] - top - left + diag == side * side)
                        res++;
                    else
                        break;
                    side++;
                }
            }
        }
        return res;
    }
}


class Solution2 {
    public int countSquares(int[][] matrix) {
        /*
         * We can implement some speed up. For example, if the prefix
         * sum at matrix[i][j] = (i + 1) * (j + 1), then all the cells are one
         * In this case, the number of squares is min(i + 1, j + 1). This shall
         * save us a lot of time if the matrix is not sparse.
         *
         * 10 ms, faster than 12.20%
         */
        int M = matrix.length;
        int N = matrix[0].length; 
        for (int i = 0; i < M; i++) {
            int psum = 0;
            for (int j = 0; j < N; j++) {
                psum += matrix[i][j];
                matrix[i][j] = psum + (i > 0 ? matrix[i - 1][j] : 0);
            }
        }
        int res = 0;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (matrix[i][j] == (i + 1) * (j + 1)) {
                    res += Math.min(i + 1, j + 1);
                    continue;
                }
                int side = 1;
                while (side * side <= matrix[i][j]) {
                    int top = i - side >= 0 ? matrix[i - side][j] : 0;
                    int left = j - side >= 0 ? matrix[i][j - side] : 0;
                    int diag = (i - side >= 0 && j - side >= 0) ? matrix[i - side][j - side] : 0;
                    if (matrix[i][j] - top - left + diag == side * side)
                        res++;
                    else
                        break;
                    side++;
                }
            }
        }
        return res;
    }
}


class Solution3 {
    public int countSquares(int[][] matrix) {
        /*
         * Did not read the official solution, but got a BIG hint from it.
         * We shall use DP.
         *
         * dp[i][j] = the number of squares ending at matrix[i][j]. If
         * matrix[i][j] = 0, dp[i][j] = 0.
         *
         * Otherwise, dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
         *
         * And just to be lazy, we will implement the DP matrix in-place.
         *
         * O(MN), 8 ms, faster than 20.73%
         */
        int res = 0;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == 1) {
                    int top = i - 1 >= 0 ? matrix[i - 1][j] : 0;
                    int left = j - 1 >= 0 ? matrix[i][j - 1] : 0;
                    int diag = (i - 1 >= 0 && j - 1 >= 0) ? matrix[i - 1][j - 1] : 0;
                    matrix[i][j] = Math.min(Math.min(top, left), diag) + 1;
                    res += matrix[i][j];
                }
            }
        }
        return res;
    }
}


class Solution4 {
    public int countSquares(int[][] matrix) {
        /*
         * Same as Solution3, but we create an auxillary DP array and making
         * it one bigger on both row and col. This way we can avoid excessive
         * IF condition checks.
         *
         * 6 ms, faster than 70.73% This is the fastest solution! Don't do
         * too much IF condition checks.
         */
        int M = matrix.length;
        int N = matrix[0].length;
        int[][] dp = new int[M + 1][N + 1];
        int res = 0;
        for (int i = 1; i < M + 1; i++) {
            for (int j = 1; j < N + 1; j++) {
                if (matrix[i - 1][j - 1] == 1) {
                    dp[i][j] = Math.min(Math.min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1;
                    res += dp[i][j];
                }
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
