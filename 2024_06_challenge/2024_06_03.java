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
    public int appendCharacters(String s, String t) {
        /*
         * LeetCode 2486
         *
         * Greedily match everything in t to s. Whatever cannot be matched
         * needs to be appended to the end of s.
         *
         * O(N), 6 ms, faster than 66.26%
         */
        int j = 0; // index for t
        for (int i = 0; i < s.length() && j < t.length(); i++) {
            if (s.charAt(i) == t.charAt(j))
                j++;
        }
        return t.length() - j;
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
