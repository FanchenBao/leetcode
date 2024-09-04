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
    public int getLucky(String s, int k) {
        /*
         * LeetCode 1945
         *
         * 1 ms, faster than 88.60%
         */
        StringBuilder numStr = new StringBuilder();
        for (char c : s.toCharArray())
            numStr.append(c - 'a' + 1);
        int cur = 0;
        int res = 0;
        String tmp = numStr.toString();
        while (k > 0) {
            for (char c : tmp.toCharArray())
                cur += c - '0';
            tmp = String.valueOf(cur);
            k--;
            res = cur;
            cur = 0;
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
