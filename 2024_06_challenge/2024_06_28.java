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
    public long maximumImportance(int n, int[][] roads) {
        /*
         * LeetCode 2285
         *
         * Sort the nodes by the number of edges. Their order is their
         * importance.
         *
         * O(NlogN), 7 ms, faster than 87.57%
         */
        int[] counter = new int[n];
        for (int[] e : roads) {
            counter[e[0]]++;
            counter[e[1]]++;
        }
        Arrays.sort(counter);
        long res = 0;
        for (int i = 0; i < n; i++)
            res += (long)(i + 1) * (long)counter[i]; 
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
