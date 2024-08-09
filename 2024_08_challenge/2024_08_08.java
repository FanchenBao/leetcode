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
    public int[][] spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        /*
         * LeetCode 885
         *
         * Not a complex problem, but it took a while to get all the logic in
         * place.
         *
         * O(MN), 5 ms, faster than 47.43%
         **/
        int[][] dirs = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int steps = 0;
        int turns = 0;
        int[][] res = new int[rows * cols][2];
        int idx = 0;
        int i = rStart;
        int j = cStart;
        while (idx < rows * cols) {
            if (turns % 2 == 0)
                steps++;
            // compute the actual steps and actual start position
            int di = dirs[turns][0];
            int dj = dirs[turns][1];
            int endI = i + di * steps;
            int endJ = j + dj * steps;
            if (i == endI && i >= 0 && i < rows) {
                int sj = Math.max(0, Math.min(j, cols - 1));
                int ej = Math.max(0, Math.min(endJ, cols - 1));
                for (int jj = sj; (dj >= 0 && jj <= ej) || (dj < 0 && jj >= ej); jj += dj) {
                    if (idx == 0 || (res[idx - 1][0] != i || res[idx - 1][1] != jj))
                        res[idx++] = new int[]{i, jj};
                }
            }
            if (j == endJ && j >= 0 && j < cols) {
                int si = Math.max(0, Math.min(i, rows - 1));
                int ei = Math.max(0, Math.min(endI, rows - 1));
                for (int ii = si; (di >= 0 && ii <= ei) || (di < 0 && ii >= ei); ii += di) {
                    if (idx == 0 || (res[idx - 1][0] != ii || res[idx - 1][1] != j))
                        res[idx++] = new int[]{ii, j};
                }
            }
            i = endI;
            j = endJ;
            turns = (turns + 1) % 4;
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
