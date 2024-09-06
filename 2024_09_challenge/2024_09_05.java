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
    public int[] missingRolls(int[] rolls, int mean, int n) {
        /*
         * LeetCode 2028
         *
         * We can compute the sum of all the unknown rolls. If that sum is
         * smaller than the minimum sum producible by n rolls or larger than
         * the maximum sum producible by n rolls, it is impossible.
         *
         * Otherwise, we can even out the roll as much as we can by first
         * assigning the unknown rolls as remaining sum divided by n. Then we
         * can apply the remainders of the division evenly across all the
         * unknonw rolls.
         *
         * O(M + N), 5 ms, faster than 31.80%
         */
        int rem = mean * (n + rolls.length);
        for (int r : rolls)
            rem -= r;
        if (rem < n || rem > n * 6)
            return new int[0];
        int[] res = new int[n];
        Arrays.fill(res, rem / n);
        for (int i = 0; i < rem % n; i++)
            res[i]++;
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
