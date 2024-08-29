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
    int water;

    DSU(int N) {
        this.par = new int[N];
        for (int i = 0; i < N; i++)
            this.par[i] = i;
        this.rnk = new int[N];
        this.water = N + 1;
    }

    int find(int x) {
        if (this.par[x] != x && this.par[x] != this.water)
            this.par[x] = find(this.par[x]);
        return this.par[x];
    }

    boolean union(int x, int y) {
        int px = find(x);
        int py = find(y);
        if (px == py)
            return false;
        if (this.rnk[px] > this.rnk[py]) {
            this.par[py] = px;
        } else if (this.rnk[py] > this.rnk[px]) {
            this.par[px] = py;
        } else {
            this.par[py] = px;
            this.rnk[px]++;
        }
        return true;
    }
}

class Solution {
    int[][] DIRS = new int[][]{{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

    private DSU unionFind(int[][] grid, int M, int N) {
        DSU dsu = new DSU(M * N);
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (grid[i][j] == 0) {
                    dsu.par[i * N + j] = dsu.water;
                    continue;
                }
                for (int[] dir : DIRS) {
                    int ni = i + dir[0];
                    int nj = j + dir[1];
                    if (ni >= 0 && ni < M && nj >= 0 && nj < N && grid[ni][nj] == 1) 
                        dsu.union(i * N + j, ni * N + nj);
                }
            }
        }
        return dsu;
    }

    public int countSubIslands(int[][] grid1, int[][] grid2) {
        /*
         * LeetCode 1905
         *
         * Two rounds of union find to produce all the islands on grid1 and
         * grid2. Then we go through each island in grid2, and check whether
         * they all belong to the same island in grid1.
         *
         * Of course, one can also use DFS instead of union find to get all
         * the islands.
         *
         * O(MN * O(union-find)), 113 ms, faster than 5.60%
         */
        int M = grid1.length;
        int N = grid1[0].length;
        DSU dsu1 = unionFind(grid1, M, N);
        DSU dsu2 = unionFind(grid2, M, N);
        Map<Integer, List<Integer>> islands2 = new HashMap<>();
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                int p = dsu2.find(i * N + j);
                if (p == dsu2.water)
                    continue;
                islands2.putIfAbsent(p, new ArrayList<>());
                islands2.get(p).add(i * N + j);
            }
        }
        int res = 0;
        for (int p : islands2.keySet()) {
            int dsu1Par = -1;
            for (int island : islands2.get(p)) {
                int pp = dsu1.find(island);
                if (dsu1Par == -1 && pp != dsu1.water) {
                    dsu1Par = pp;
                } else if (pp == dsu1.water || dsu1Par != pp) {
                    dsu1Par = -1;
                    break;
                }
            }
            res += dsu1Par >= 0 ? 1 : 0;
        }
        return res;
    }
}


class Solution2 {
    int[][] DIRS = new int[][]{{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

    private void dfsFindIsland(int i, int j, int[][] grid, int island) {
        // DSF grid and distinguish each island in-place
        int M = grid.length;
        int N = grid[0].length;
        grid[i][j] = island;
        for (int[] dir : DIRS) {
            int ni = i + dir[0];
            int nj = j + dir[1];
            if (ni >= 0 && ni < M && nj >= 0 && nj < N && grid[ni][nj] == 1)
                dfsFindIsland(ni, nj, grid, island);
        }
    }

    private int dfsCheckIsland(int i, int j, int[][] grid1, int[][] grid2, int island1) {
        // DSF grid2 and check whether its island is contained within the
        // corresponding island in grid1. If yes, return true. Otherwise false
        int M = grid2.length;
        int N = grid2[0].length;
        grid2[i][j] = 0;
        int isSubIsland = grid1[i][j] == island1 ? 1 : 0;
        for (int[] dir : DIRS) {
            int ni = i + dir[0];
            int nj = j + dir[1];
            if (ni >= 0 && ni < M && nj >= 0 && nj < N && grid2[ni][nj] == 1)
                isSubIsland *= dfsCheckIsland(ni, nj, grid1, grid2, island1);
        }
        return isSubIsland;
    }


    private void findIslands(int[][] grid) {
        int M = grid.length;
        int N = grid[0].length;
        int island = 2;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (grid[i][j] == 1) {
                    dfsFindIsland(i, j, grid, island);
                    island++;
                }
            }
        }
    }

    public int countSubIslands(int[][] grid1, int[][] grid2) {
        /*
         * Use DFS to find islands. This should be faster than union find
         *
         * O(MN), 41 ms, faster than 13.62%
         */
        findIslands(grid1);
        int res = 0;
        for (int i = 0; i < grid2.length; i++) {
            for (int j = 0; j < grid2[0].length; j++) {
                if (grid2[i][j] == 1)
                    res += dfsCheckIsland(i, j, grid1, grid2, grid1[i][j] == 0 ? Integer.MAX_VALUE : grid1[i][j]);
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
