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
    public int numWaterBottles(int numBottles, int numExchange) {
        /*
         * LeetCode 1518
         *
         * 0 ms, faster than 100.00%
         */
        int res = numBottles;
        int cur = numBottles;
        while (cur >= numExchange) {
            int full = cur / numExchange;
            res += full;
            cur = cur % numExchange + full;
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
