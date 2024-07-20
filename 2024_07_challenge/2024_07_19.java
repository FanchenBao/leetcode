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
    public List<Integer> luckyNumbers (int[][] matrix) {
        /*
         * LeetCode 1380
         *
         * O(MN)
         */
        List<Integer> res = new ArrayList<>();
        int M = matrix.length;
        int N = matrix[0].length;
        for (int i = 0; i < M; i++) {
            int min = 100001;
            int minJ = -1;
            for (int j = 0; j < N; j++) {
                if (matrix[i][j] < min) {
                    min = matrix[i][j];
                    minJ = j;
                } 
            }
            int max = -1;
            for (int k = 0; k < M; k++) {
                if (matrix[k][minJ] > max)
                    max = matrix[k][minJ];
            }
            if (min == max)
                res.add(min);
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
