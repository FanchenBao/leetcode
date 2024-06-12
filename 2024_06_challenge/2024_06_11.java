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
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        /*
         * LeetCode 1122
         *
         * User a counter on arr1. Follow arr2 to fill out the result, and
         * then fill out the rest of the result with the untouched members in
         * the counter.
         *
         * O(N), 0 ms, faster than 100.00%
         */
        int[] counter = new int[1001];
        for (int a : arr1)
            counter[a]++;
        int[] res = new int[arr1.length];
        int i = 0;
        for (int a : arr2) {
            for (int j = 0; j < counter[a]; j++)
                res[i++] = a;
            counter[a] = 0;
        }
        for (int j = 0; j < counter.length; j++) {
            if (counter[j] > 0) {
                for (int l = 0; l < counter[j]; l++)
                    res[i++] = j;
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
