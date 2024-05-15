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
    int res = 0;
    int[][] dir = new int[][]{{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

    private int dfs(int i, int j, int[][] grid) {
        int curGold = grid[i][j];
        grid[i][j] = 0;
        int M = grid.length;
        int N = grid[0].length;
        int nextGold = 0;
        for (int k = 0; k < 4; k++) {
            int ni = dir[k][0] + i;
            int nj = dir[k][1] + j;
            if (ni < M && ni >= 0 && nj < N && nj >= 0 && grid[ni][nj] > 0) {
                nextGold = Math.max(dfs(ni, nj, grid), nextGold);
            }
        }
        grid[i][j] = curGold;
        return curGold + nextGold;
    }

    public int getMaximumGold(int[][] grid) {
        /*
         * LeetCode 1219
         *
         * Backtrack on every cell
         *
         * O(M^2N^2), 72 ms, faster than 54.56%
         */
        int res = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] > 0)
                    res = Math.max(res, dfs(i, j, grid));
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
