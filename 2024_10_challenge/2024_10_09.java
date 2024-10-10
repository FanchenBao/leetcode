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
    public int minAddToMakeValid(String s) {
        /*
         * LeetCode 921
         *
         * Count all the unmatched left and right parentheses while going
         * through string s as a stack.
         *
         * O(N), 0 ms, faster than 100.00%
         */
        int res = 0;
        int cntLeft = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') {
                cntLeft++;
            } else if (cntLeft > 0) {
                cntLeft--;
            } else {
                res++;
            }
        }
        return res + cntLeft;
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
