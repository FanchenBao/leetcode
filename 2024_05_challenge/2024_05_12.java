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
    public int[][] largestLocal(int[][] grid) {
        /*
         * LeetCode 2373
         *
         * Brute force. O(N^2), 3 ms
         */
        int N = grid.length;
        int[][] res = new int[N - 2][N - 2];
        for (int i = 0; i < N - 2; i++) {
            for (int j = 0; j < N - 2; j++) {
                int max = 0;
                for (int k = i; k <= i + 2; k++) {
                    for (int p = j; p <= j + 2; p++) {
                        max = Math.max(grid[k][p], max);
                    }
                }
                res[i][j] = max;
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
