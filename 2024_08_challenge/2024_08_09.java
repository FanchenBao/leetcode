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
    private int isMagic(int[][] grid, int si, int sj) {
        int sum = 0;
        boolean[] seen = new boolean[10];
        // Check rows
        for (int i = si; i <= si + 2; i++) {
            int curSum = 0;
            for (int j = sj; j <= sj + 2; j++) {
                if (grid[i][j] == 0 || grid[i][j] > 9 || seen[grid[i][j]])
                    return 0;
                seen[grid[i][j]] = true;
                curSum += grid[i][j];
            }
            if (sum == 0)
                sum = curSum;
            else if (sum != curSum)
                return 0;
        }
        // Check cols
        for (int j = sj; j <= sj + 2; j++) {
            int curSum = 0;
            for (int i = si; i <= si + 2; i++)
                curSum += grid[i][j];
            if (sum != curSum)
                return 0;
        }
        // Check diagonal
        int tlbr = grid[si][sj] + grid[si + 1][sj + 1] + grid[si + 2][sj + 2];
        int trbl = grid[si][sj + 2] + grid[si + 1][sj + 1] + grid[si + 2][sj];
        if (tlbr != sum || trbl != sum)
            return 0;
        return 1;
    }

    public int numMagicSquaresInside(int[][] grid) {
        /*
         * LeetCode 840
         *
         * Since the input size is small, we can brute force this problem.
         *
         * O(MN*9), 0 ms, faster than 100.00%
         */
        int res = 0;
        int M = grid.length;
        int N = grid[0].length;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (i + 2 < M && j + 2 < N)
                    res += isMagic(grid, i, j);
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
