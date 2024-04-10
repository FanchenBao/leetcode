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
    public int timeRequiredToBuy(int[] tickets, int k) {
        /*
         * LeetCode 2073
         *
         * We first compute the max possible amount of time needed to reduce
         * tickets[k] to zero. Then we go through all the tickets to find if
         * there have been any overCnt (an overCnt happens when tickets[i]
         * is reduced to zero but we continue decrement on it)
         *
         * O(N), 0 ms, faster than 100.00%
         */
        int N = tickets.length;
        int K = tickets[k];
        int maxTime = (K - 1) * N + k + 1;
        int overCnt = 0;
        for (int i = 0; i < N; i++) {
            tickets[i] -= K - 1;
            if (tickets[i] < 0)
                overCnt += tickets[i];
        }
        for (int i = 0; i <= k; i++) {
            if (tickets[i] <= 0)
                overCnt--;
        }
        return maxTime + overCnt;
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
