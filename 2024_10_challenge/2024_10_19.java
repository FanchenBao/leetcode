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
    public char findKthBit(int n, int k) {
        /*
         * LeetCode 1545
         *
         * Pure recursion. If k belongs to the first half of the string, it
         * would be the same as calling f(n - 1, k). If k belongs to the half
         * point, it must be '1'. If k belongs to the second half, we can
         * compute which position it should be without reversing, and recurse
         * with the smaller string. We just have to remember to invert it
         * when returning the result.
         *
         * O(N), 0 ms, faster than 100.00%
         */
        if (n == 1)        
            return '0';
        int preLen = 1 << (n - 1);
        if (k < preLen)
            return findKthBit(n - 1, k);
        if (k == preLen)
            return '1';
        // k > preLen
        char tmp = findKthBit(n - 1, (1 << n) - k);
        return tmp == '0' ? '1' : '0';
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
