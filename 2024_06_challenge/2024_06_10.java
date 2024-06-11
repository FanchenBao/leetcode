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
    public int heightChecker(int[] heights) {
        /*
         * LeetCode 1051
         * 
         * Sort heights and then compare with the original.
         *
         * O(NlogN), 2 ms, faster than 88.93%
         */
        int[] copy = new int[heights.length];
        for (int i = 0; i < heights.length; i++)
            copy[i] = heights[i];
        Arrays.sort(copy);
        int res = 0;
        for (int i = 0; i < heights.length; i++)
            res += heights[i] == copy[i] ? 0 : 1;
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
