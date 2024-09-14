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
    public int[] xorQueries(int[] arr, int[][] queries) {
        /*
         * LeetCode 1310
         *
         * Prefix XOR
         *
         * O(N + M), 2 ms, faster than 100.00%
         */
        int[] preXor = new int[arr.length];
        preXor[0] = arr[0];
        for (int i = 1; i < arr.length; i++)
            preXor[i] = preXor[i - 1] ^ arr[i];
        int[] res = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int p = queries[i][0]; int q = queries[i][1];
            if (p == 0)
                res[i] = preXor[q];
            else
                res[i] = preXor[q] ^ preXor[p - 1];
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
