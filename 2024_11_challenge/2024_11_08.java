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
    public int[] getMaximumXor(int[] nums, int maximumBit) {
        /*
         * LeetCode 1829
         *
         * We can prefix XOR nums as we go, and the k we find each time will
         * be filled from right to left on the result array.
         *
         * For the current prefix XOR, the potential k that can make it max
         * is the inverse of prefix XOR. And since we have a cap on the size
         * of k, we need to do ~xor & mask, where mask is the largest number
         * we can use.
         *
         * O(N), 2 ms, faster than 100.00%
         */
        int xor = 0;
        int[] res = new int[nums.length];
        int mask = (1 << maximumBit) - 1;
        for (int i = 0; i < nums.length; i++) {
            xor ^= nums[i];
            res[nums.length - 1 - i] = ~xor & mask;
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
