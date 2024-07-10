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
    public double averageWaitingTime(int[][] customers) {
        /*
         * LeetCode 1701
         *
         * Keep track of the end time after each customer has been served.
         * From this we can compute the customer's wait time and know the
         * starting time of the next customer.
         *
         * O(N), 3 ms, faster than 93.06%
         */
        double total = 0;
        double end = 0;
        for (int[] c : customers) {
            end = Math.max(end, c[0]) + (double)c[1];
            total += end - c[0];
        }
        return total / (double)customers.length;
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
