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
    public int maxEqualRowsAfterFlips(int[][] matrix) {
        /*
         * LeetCode 1072
         *
         * For each row, find the pattern of Keep or Flip. The rows with the
         * same pattern can become equal rows after flips. Thus the question
         * becomes finding the max count of the same Keep or Flip pattern.
         *
         * O(MN), 29 ms, faster than 64.04% 
         */
        Map<String, Integer> patterns = new HashMap<>();
        int res = 0;
        for (int [] row : matrix) {
            StringBuilder pat0 = new StringBuilder();
            StringBuilder pat1 = new StringBuilder();
            for (int e : row) {
                if (e == 1) {
                    pat0.append('F');
                    pat1.append('K');
                } else {
                    pat0.append('K');
                    pat1.append('F');
                }
            }
            String pat0Str = pat0.toString();
            String pat1Str = pat1.toString();
            patterns.put(pat0Str, patterns.getOrDefault(pat0Str, 0) + 1);
            patterns.put(pat1Str, patterns.getOrDefault(pat1Str, 0) + 1);
            res = Math.max(res, patterns.get(pat0Str));
        }
        return res;
    }
}


class Solution2 {
    public int maxEqualRowsAfterFlips(int[][] matrix) {
        /*
         * This is from the official solution, which has the same idea but
         * slightly better implementation as it does not require two patterns
         * to be built. We only need to build one, which is to always keep the
         * row the same as the first element of the row.
         *
         * 18 ms, faster than 95.51%
         */
        Map<String, Integer> patterns = new HashMap<>();
        int res = 0;
        for (int [] row : matrix) {
            StringBuilder pat = new StringBuilder();
            for (int i = 0; i < row.length; i++)
                pat.append(row[i] == row[0] ? 'K' : 'F');
            String patStr = pat.toString();
            patterns.put(patStr, patterns.getOrDefault(patStr, 0) + 1);
            res = Math.max(res, patterns.get(patStr));
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
