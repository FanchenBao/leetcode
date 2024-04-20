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
    int[][] dir = new int[][]{{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
    int M;
    int N;
    char[][] grid;

    private void dfs(int i, int j) {
        this.grid[i][j] = '0';
        for (int[] dd : dir) {
            int ni = i + dd[0];
            int nj = j + dd[1];
            if (ni >= 0 && ni < this.M && nj >= 0 && nj < this.N && this.grid[ni][nj] == '1')
                dfs(ni, nj);
        }
    }

    public int numIslands(char[][] grid) {
        /*
         * LeetCode 200
         *
         * DFS
         *
         * O(MN) 3 ms, faster than 86.63% 
         */
        this.M = grid.length;
        this.N = grid[0].length;
        this.grid = grid;
        int res = 0;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (grid[i][j] == '1') {
                    dfs(i, j);
                    res++;
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
