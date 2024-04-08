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
    public boolean checkValidString(String s) {
        /*
         * LeetCode 678
         *
         * O(N), 0 ms, faster than 100.00%
         */
        int stack = 0;
        int cnt = 0;
        // left to right, check on right parenthesis
        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack++;
            } else if (c == ')') {
                if (stack == 0) {
                    if (cnt == 0)
                        return false;
                    cnt--;
                } else {
                    stack--;
                }
            } else {
                cnt++;
            }
        }
        // right to left, check on left parenthesis
        stack = 0;
        cnt = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            char c = s.charAt(i);
            if (c == ')') {
                stack++;
            } else if (c == '(') {
                if (stack == 0) {
                    if (cnt == 0)
                        return false;
                    cnt--;
                } else {
                    stack--;
                }
            } else {
                cnt++;
            }
        }
        return true;
    }
}


class Solution2 {
    public boolean checkValidString(String s) {
        /*
         * This is from the official solution. It has the same idea as
         * solution1, but with a much simpler implementation.
         *
         * It only requires one pass.
         */
        int openCnt = 0;
        int closeCnt = 0;
        for (int i = 0; i < s.length(); i++) {
            // equivalent to going left to right and check on right paren
            if (s.charAt(i) == '(' || s.charAt(i) == '*')
                openCnt++;
            else
                openCnt--;
            // equivalent to going right to left and check on left paren
            if (s.charAt(s.length() - i - 1) == ')' || s.charAt(s.length() - i - 1) == '*')
                closeCnt++;
            else
                closeCnt--;
            if (openCnt < 0 || closeCnt < 0)
                return false;
        }
        return true;
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
