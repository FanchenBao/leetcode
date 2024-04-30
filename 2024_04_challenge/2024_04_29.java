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
    public int minOperations(int[] nums, int k) {
        /*
         * LeetCode 2997
         *
         * XOR everything and count the bits in the final outcome. Each set
         * bit represents one flipping operation.
         *
         * O(N) 1 ms, faster than 100.00%
         */
        int xor = k;
        for (int n : nums)
            xor ^= n;
        return Integer.bitCount(xor);
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
