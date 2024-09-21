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
    private int[] getLPS(String s) {
        int N = s.length();
        int[] lps = new int[N];
        int len = 0;
        int i = 1;
        while (i < N) {
            if (s.charAt(i) == s.charAt(len))
                lps[i++] = ++len;
            else if (len == 0)
                i++;
            else
                len = lps[len - 1];
        }
        return lps;
    }

    public String shortestPalindrome(String s) {
        /*
         * LeetCode 214
         *
         * We will try the longest prefix suffix array of KMP algorithm to find
         * the longest palindrom starting from s[0]. We need to do this
         * because the shortest palindrome to form based on s depends on the
         * longest palindrom starting from s[0].
         *
         * We first find the LPS of the original string. Then we find the LPS
         * of the reversed string using the original string as prefix. Then
         * the longest palindrome starting from s[0] is the LPS value of the
         * final char in the reversed string.
         *
         * The rest is easy.
         *
         * Note that for the reverse LPS, we don't have to use an array,
         * because we only care about the LPS value of the final char in the
         * reversed string, and because the construction of the reverse LPS
         * only depend on the forward LPS, which we will create beforehand.
         *
         * O(N)
         *
         * Update: we don't even need to physically reverse the string. We
         * just need to produce the reverse LPS by iterating the original s
         * from right to left.
         *
         * 3 ms, faster than 96.27%
         */
        int N = s.length();
        if (N == 0)
            return "";
        int[] lps = getLPS(s);
        int revLps = 0;
        int i = N - 1;
        int len = 0;
        while (i >= 0) {
            if (s.charAt(i) == s.charAt(len)) {
                revLps = ++len;
                i--;
            } else if (len == 0) {
                i--;
            } else {
                len = lps[len - 1];
            }
        }
        String prefix = new StringBuilder(s.substring(revLps, N)).reverse().toString();
        return prefix + s;
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
