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
    public boolean lemonadeChange(int[] bills) {
        /*
         * LeetCode 860
         *
         * Simulate the entire transaction
         * O(N), 2 ms, faster than 95.27%
         */
        int[] counter = new int[21];
        for (int b : bills) {
            if (b == 5) {
                counter[5]++;
            } else if (b == 10 && counter[5] > 0) {
                counter[10]++;
                counter[5]--;
            } else if (b == 20) {
                if (counter[5] > 0 && counter[10] > 0) {
                    counter[10]--;
                    counter[5]--;
                } else if (counter[5] >= 3) {
                    counter[5] -= 3;
                }
                counter[20]++;
            } else {
                return false;
            }
        }
        return true;
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
