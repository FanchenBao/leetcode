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
    int[][] land;
    int[][] dir = new int[][]{{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
    int M;
    int N;

    private void dfs(int i, int j, int[] group) {
        land[i][j] = 0;
        group[0] = Math.min(group[0], i);
        group[1] = Math.min(group[1], j);
        group[2] = Math.max(group[2], i);
        group[3] = Math.max(group[3], j);
        for (int[] dd : dir) {
            int ni = i + dd[0];
            int nj = j + dd[1];
            if (ni >= 0 && ni < this.M && nj >= 0 && nj < this.N && this.land[ni][nj] == 1)
                dfs(ni, nj, group);
        }
    }

    public int[][] findFarmland(int[][] land) {
        /*
        * LeetCode 1992
        *
        * DFS, O(MN), 15 ms, faster than 51.33%
        */
        this.land = land;
        this.M = land.length;
        this.N = land[0].length;
        List<int[]> res = new ArrayList<>();
        for (int i = 0; i < this.M; i++) {
            for (int j = 0; j < this.N; j++) {
                if (land[i][j] == 1) {
                    res.add(new int[]{301, 301, -1, -1});
                    dfs(i, j, res.get(res.size() - 1));
                }
            }
        }
        int[][] resArr = new int[res.size()][4];
        for (int i = 0; i < res.size(); i++)
            resArr[i] = res.get(i);
        return resArr;
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
