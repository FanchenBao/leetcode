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
    public int matrixScore(int[][] grid) {
        /*
         * LeetCode 861
         *
         * Greedy. We must turn the left most bit to one. Then for the remaining
         * positions, we only modify them column-wise. We flip if there
         * are more zeros than ones in a column.
         *
         * Left most bit must be set to one. And once they are set to one, we
         * cannot make further changes row-wise.
         *
         * There are different ways to set the left most bit to one, but their
         * net effect on the grid is the same. Thus, we only need to choose one
         * way to set the left most bit to one.
         *
         * O(MN), 0 ms, faster than 100.00% 
         */
        int M = grid.length;
        int N = grid[0].length;
        for (int i = 0; i < M; i++) {
            if (grid[i][0] == 0) {
                for (int j = 0; j < N; j++) {
                    grid[i][j] = grid[i][j] == 0 ? 1 : 0;
                }
            }
        }
        int res = 3;
        for (int j = 1; j < N; j++) {
            int maxOnes = 0;
            for (int i = 0; i < M; i++)
                maxOnes += grid[i][j];
            maxOnes = Math.max(maxOnes, M - maxOnes);
            res = res * 2 + maxOnes;
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
