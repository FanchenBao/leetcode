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
    public int minHeightShelves(int[][] books, int shelfWidth) {
        /*
         * LeetCode 1105 (fail)
         *
         * Use dp[i] to represent the min height of shelving books[:i + 1]
         * We try to fit books[j:i + 1] in one shelf, where 0 <= j <= i
         * Then the total height is dp[j - 1] + cur_height. We will pick the
         * smallest among all these possibilities as dp[i]
         *
         * O(N^2), 1 ms, faster than 76.60%
         */
        int N = books.length;
        int[] dp = new int[N];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = books[0][1];
        for (int i = 1; i < N; i++) {
            int cur_width = 0;
            int cur_height = 0;
            for (int j = i; j >= 0; j--) {
                cur_width += books[j][0];
                if (cur_width > shelfWidth)
                    break;
                cur_height = Math.max(cur_height, books[j][1]);
                dp[i] = Math.min(dp[i], (j == 0 ? 0 : dp[j - 1]) + cur_height);
            }
        }
        return dp[N - 1];
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
