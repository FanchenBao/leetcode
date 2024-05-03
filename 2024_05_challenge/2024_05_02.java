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
    public int findMaxK(int[] nums) {
        /*
         * LeetCode 2441
         *
         * O(N), 2 ms, faster than 96.21%
         */
        int[] seen = new int[1001];
        int res = -1;
        for (int n : nums) {
            int abs = Math.abs(n);
            if (seen[abs] + n == 0)
                res = Math.max(res, abs);
            else
                seen[abs] = n;
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
