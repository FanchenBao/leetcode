import java.util.*;
import java.util.stream.Stream;

import javax.management.openmbean.ArrayType;

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
    private int dp(int l, int r, List<Character> ss, int[][] memo) {
        if (l > r)
            return 0;
        if (memo[l][r] == Integer.MAX_VALUE) {
            // scenario one
            memo[l][r] = 1 + dp(l + 1, r, ss, memo);
            // scenario two
            for (int k = l + 1; k <= r; k++) {
                if (ss.get(k) == ss.get(l)) {
                    memo[l][r] = Math.min(memo[l][r], dp(l, k - 1, ss, memo) + dp(k + 1, r, ss, memo));
                }
            }
        }
        return memo[l][r];
    }

    public int strangePrinter(String s) {
        /*
         * LeetCode 664, FAIL
         *
         * Very tough. I thought about it for 15 min and I was pretty sure
         * I couldn't solve it today. After checking my previous attempts, I
         * think I understood how it was done.
         *
         * dp(l, r) is the min prints to produce s[l:r + 1] with the first
         * print being s[l].
         *
         * There are two scenarios. First scenario is that we print s[l], and
         * then handle the remaining. In this case, dp(l, r) = 1 + dp(l + 1, r).
         *
         * Second scenario is that there are multiple letters in s[l:r + 1]
         * that are the same as s[l]. For each s[k] == s[l], the stretch
         * s[l:k + 1] can be produced by dp(l, k - 1). Then we only need to
         * add the remaining dp(k + 1, r). This works because it is only
         * sensible to print s[l] all the way to some s[k]. We don't know
         * what that s[k] is. Thus, we go through all possible s[k] to find
         * the optimum.
         *
         * The final optimization is that we don't have to use s directly.
         * Instead, we will preprocess s to remove any consecutive duplicates.
         * This is because all consecutive duplicates can be printed in one
         * go.
         *
         * O(N^3)
         */
        // ss is the preprocessed string with no consecutive duplicates
        List<Character> ss = new ArrayList<>();
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) != s.charAt(i - 1))
                ss.add(s.charAt(i - 1));
        }
        ss.add(s.charAt(s.length() - 1));
        int[][] memo = new int[ss.size()][ss.size()];
        for (int[] row : memo)
            Arrays.fill(row, Integer.MAX_VALUE);
        return dp(0, ss.size() - 1, ss, memo);
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
