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

class Solution1 {
    int res = 0;
    int[][] didj = new int[][]{{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

    private void dfs(int i, int j, int[][] grid, int M, int N) {
        grid[i][j] = -1;
        for (int[] dd : didj) {
            int ni = dd[0] + i;
            int nj = dd[1] + j;
            if (ni >= 0 && ni < M && nj >= 0 && nj < N) {
                if (grid[ni][nj] == 1)
                    dfs(ni, nj, grid, M, N);
                else if (grid[ni][nj] == 0)
                    res++;
            } else {
                res++;
            }

        }
    } 

    public int islandPerimeter(int[][] grid) {
        /*
        * LeetCode 463
        * 
        * DFS and record an edge only when there is no more land to go.
        * O(MN)
        */
        int M = grid.length;
        int N = grid[0].length;
        int fi = 0;
        int fj = 0;
        while (fi < M) {
            while (fj < N) {
                if (grid[fi][fj] == 1)
                    break;
                fj++;
            }
            if (fj < N)
                break;
            fi++;
            fj = 0;
        }
        dfs(fi, fj, grid, M, N);
        return res;
    }
}


class Solution2 {
    public int islandPerimeter(int[][] grid) {
        /*
         * This is my solution from before. I think it is better
         *
         * O(MN), 6 ms, faster than 35.73%
         */
        int M = grid.length;
        int N = grid[0].length;
        int redundant = 0;
        int lands = 0;
        int[][] didj = new int[][]{{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (grid[i][j] == 1) {
                    lands++;
                    for (int[] dd : didj) {
                        int ni = dd[0] + i;
                        int nj = dd[1] + j;
                        if (ni >= 0 && ni < M && nj >= 0 && nj < N && grid[ni][nj] == 1)
                            redundant++;
                    }
                }
            }
        }
        return 4 * lands - redundant;
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
