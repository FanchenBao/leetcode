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
    public int longestIdealString(String s, int k) {
        /*
         * LeetCode 2370
         *
         * DP, where dp[i] is the length of the longest ideal string ending
         * at s[i].
         *
         * O(N * k), 29 ms, faster than 73.81%
         */
        int[] dp = new int[s.length()];
        int[] maxLenOnLetter = new int[26];
        int res = 0;
        for (int i = 0; i < s.length(); i++) {
            int cur = s.charAt(i) - 'a';
            for (int j = Math.min(25, cur + k); j >= Math.max(0, cur - k); j--)
                dp[i] = Math.max(dp[i], maxLenOnLetter[j] + 1);
            maxLenOnLetter[cur] = Math.max(maxLenOnLetter[cur], dp[i]);
            res = Math.max(res, dp[i]);
        }
        return res;
    }
}


class Solution2 {
    public int longestIdealString(String s, int k) {
        /*
         * LeetCode 2370
         *
         * One dp array is sufficient.
         * dp[i] is the length of the longest ideal string ending at a letter
         *
         * 21 ms, faster than 87.30%
         */
        int[] dp = new int[26];
        int res = 0;
        for (char c : s.toCharArray()) {
            int i = c - 'a';
            int cur = 0;
            for (int j = Math.min(25, i + k); j >= Math.max(0, i - k); j--)
                cur = Math.max(cur, dp[j] + 1);
            dp[i] = cur;
            res = Math.max(res, dp[i]);
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
