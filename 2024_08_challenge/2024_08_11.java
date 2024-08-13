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

class DSU {
    int[] par;
    int[] rnk;
    int numRegions;

    DSU(int N) {
        this.par = new int[N];
        for (int i = 0; i < N; i++)
            this.par[i] = i;
        this.rnk = new int[N];
        this.numRegions = N;
    }

    int find(int x) {
        if (this.par[x] != x)
            this.par[x] = this.find(this.par[x]);
        return this.par[x];
    }

    boolean union(int x, int y) {
        int px = this.find(x);
        int py = this.find(y);
        if (px == py) 
            return false;
        if (this.rnk[px] > this.rnk[py]) {
            this.par[py] = px;
        } else if (this.rnk[px] < this.rnk[py]) {
            this.par[px] = py;
        } else {
            this.par[py] = px;
            this.rnk[px]++;
        }
        this.numRegions--;
        return true;
    }
}


class Solution {
    int[][] dirs = new int[][]{{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
    int numOnes;

    private DSU getDSU(int[][] grid) {
        DSU dsu = new DSU(numOnes + 1);
        int M = grid.length;
        int N = grid[0].length;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (grid[i][j] > 0) {
                    for (int[] ds : this.dirs) {
                        int ni = i + ds[0];
                        int nj = j + ds[1];
                        if (ni >= 0 && ni < M && nj >= 0 && nj < N && grid[ni][nj] > 0)
                            dsu.union(grid[i][j], grid[ni][nj]);
                    }
                }
            }
        }
        return dsu;
    }

    public int minDays(int[][] grid) {
        /*
         * LeetCode 1568
         *
         * This solution is based on the idea that given any grid, as long as
         * there are at least two cells, we can always remove two cells to
         * disconnect the island.
         *
         * Thus, the question becomes whether it is possible to remove zero or
         * one cell to disconnect the island.
         *
         * If the island already is disconnected, we remove zero cell.
         *
         * If by removing each cell and re-examine the island situation, we
         * can find one such cell that when it is removed the island becomes
         * disconnected, we return 1.
         *
         * Otherwise, we always return 2.
         *
         * O(M^2N^2 * UnionFind), 63 ms, faster than 5.30%
         */
        List<int[]> ones = new ArrayList<>();
        int idx = 1;
        int M = grid.length;
        int N = grid[0].length;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (grid[i][j] == 1) {
                    grid[i][j] = idx++;
                    ones.add(new int[]{i, j});
                }
            }
        }
        this.numOnes = ones.size();
        if (this.numOnes == 0 || this.numOnes == 1)
            return this.numOnes;
        // Examine if the original islands have already bene split.
        DSU dsu = this.getDSU(grid);
        if (dsu.numRegions - 1 > 1) // numRegion need to minus one to remove the unrelated region formed by index 0
            return 0;
        // Try to remove just one island and see if we can split into two.
        for (int[] one : ones) {
            int tmp = grid[one[0]][one[1]];
            grid[one[0]][one[1]] = 0;
            dsu = this.getDSU(grid);
            if (dsu.numRegions - 2 > 1) // not counting the region formed by index 0 and index tmp
                return 1;
            grid[one[0]][one[1]] = tmp;
        }
        // If we cannot break the island by removing just one cell, we can
        // always break the island by two cells
        return 2;
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
