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
    public int[][] construct2DArray(int[] original, int m, int n) {
        /*
         * LeetCode 2022
         *
         * O(MN),  5 ms, faster than 54.86%
         */
        if (m * n != original.length)
            return new int[0][];
        int[][] res = new int[m][n];
        for (int k = 0; k < original.length; k++)
            res[k / n][k % n] = original[k];
        return res;
    }
}


class Solution2 {
    public int[][] construct2DArray(int[] original, int m, int n) {
        /*
         * Without using division or modulo, 4 ms, faster than 71.26%
         */
        if (m * n != original.length)
            return new int[0][];
        int[][] res = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++)
                res[i][j] = original[i * n + j];
        }
        return res;
    }
}


class Solution3 {
    public int[][] construct2DArray(int[] original, int m, int n) {
        /*
         * Without any arithmetic, 3 ms, faster than 97.73% 
         */
        if (m * n != original.length)
            return new int[0][];
        int[][] res = new int[m][n];
        int k = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++)
                res[i][j] = original[k++];
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
