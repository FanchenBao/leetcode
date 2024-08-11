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

    DSU(int N) {
        this.rnk = new int[N];
        this.par = new int[N];
        for (int i = 0; i < N; i++)
            this.par[i] = i;
    } 

    int find(int x) {
        if (this.par[x] != x)
            this.par[x] = this.find(this.par[x]);
        return this.par[x];
    }

    boolean union(int x, int y) {
        int px = this.find(x);
        int py = this.find(y);
        if (px != py) {
            if (this.rnk[px] > this.rnk[py]) {
                this.par[py] = px;
            } else if (this.rnk[px] < this.rnk[py]) {
                this.par[px] = py;
            } else {
                this.par[py] = px;
                this.rnk[px]++;
            }
            return true;
        }
        return false;
    }
}


class Solution1 {
    public int regionsBySlashes(String[] grid) {
        /*
         * LeetCode 959 (Fail)
         *
         * I couldn't figure out any reasonable solution. So I read the answer
         * and this Union-Find solution is quite brilliant. It breaks down the
         * grid into triangle components (i.e., each cell consists of four
         * triangles and they are all considered separate initially)
         *
         * When we iterate through each cell, if there is no slash in the cell,
         * all four triangles are unioned. If there is a slash, two of the
         * triangles are unioned.
         *
         * As we transition from one cell to the next, the triangle in the
         * previous cell that shares the vertical or horizontal edge with the
         * current triangle shall also be unioned.
         *
         * We will index the triangles by numbering them as
         *   0
         * 1   3
         *   2
         *
         * O(N^2 * UnionFind) 11 ms, faster than 17.77% 
         */
        int N = grid.length;
        DSU dsu = new DSU(N * N * 4);
        for (int i = 0; i < N; i++) {
            String row = grid[i];
            for (int j = 0; j < N; j++) {
                int[] tris = new int[4];
                tris[0] = (i * N + j) * 4; // top triangle
                for (int t = 1; t <= 3; t++)
                    tris[t] = tris[0] + t;
                if (row.charAt(j) == ' ') {
                    for (int t = 1; t <= 3; t++)
                        dsu.union(tris[0], tris[t]);
                } else if (row.charAt(j) == '/') {
                    dsu.union(tris[0], tris[1]);
                    dsu.union(tris[2], tris[3]);
                } else {
                    dsu.union(tris[0], tris[3]);
                    dsu.union(tris[2], tris[1]);
                }
                if (i > 0) {
                    // union with previous triangles that share horizontal edge
                    int pht = ((i - 1) * N + j) * 4 + 2;
                    dsu.union(tris[0], pht);
                }
                if (j > 0) {
                    // union with previous triangles that share vertical edge
                    int pvt = (i * N + j - 1) * 4 + 3; 
                    dsu.union(tris[1], pvt);
                }
            }
        }
        Set<Integer> regions = new HashSet<>();
        for (int t = 0; t < N * N * 4; t++)
            regions.add(dsu.find(t));
        return regions.size();
    }
}


class Solution2 {
    public int regionsBySlashes(String[] grid) {
        /*
         * This is another approach using Union Find. We mark the vertices of
         * the grid. A slashes connects two vertices. We union them. If these
         * two vertices are already unioned, then the slash creates a new
         * region and the answer increments.
         *
         * Initially, we union all the vertices along the boundaries.
         *
         * The vertices are labeled as such (for a 3 x 3 grid)
         *
         * 0   1   2   3
         * 4   5   6   7
         * 8   9  10  11
         * 12 13  14  15
         *
         * O(N^2 * UnionFind) 2 ms, faster than 100.00%
         */
        int N = grid.length + 1; // the length of the vertices
        DSU dsu = new DSU(N * N);
        // Union all the vertices along the boundaries
        for (int j = 1; j < N; j++) {
            dsu.union(0, j);
            dsu.union(N * (N - 1), j + N * (N - 1));
        }
        for (int i = 1; i < N; i++) {
            dsu.union(0, i * N);
            dsu.union(N - 1, N - 1 + i * N);
        }
        int res = 1; // the boundaries form the initial region
        // Union all the vertices connected by slash
        for (int i = 0; i < N - 1; i++) {
            String row = grid[i];
            for (int j = 0; j < N - 1; j++) {
                int tl = i * N + j; // index of top left vertex
                int bl = (i + 1) * N + j; // index of bottom left vertex
                if (row.charAt(j) == '/')
                    res += dsu.union(tl + 1, bl) ? 0 : 1;
                else if (row.charAt(j) == '\\')
                    res += dsu.union(tl, bl + 1) ? 0 : 1;
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
