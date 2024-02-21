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
    public int rangeBitwiseAnd(int left, int right) {
        /*
         * LeetCode 201
         *
         * For the left, we have the total number of bits. If 1000...00 with
         * one more bit than left is within the range, then the result is zero.
         * 
         * Otherwise, we only need to keep the consecutive ones on the most
         * siginifcant bits of left. Then we do recursion on the remaining.
         *
         * Be careful about the overflowing situations.
         *
         * O(1) 3 ms, faster than 100.00%
         */
        if (right == 0)
            return 0;
        int l = left;
        int numBits = 0;
        int conseqBitCount = 0;
        while (l > 0) {
            numBits++;
            if (l % 2 == 1)
                conseqBitCount++;
            else
                conseqBitCount = 0;
            l >>= 1;
        }
        if (((long)1 << numBits) <= right)
            return 0;
        int res = (int)(((long)1 << conseqBitCount) - 1) << (numBits - conseqBitCount);
        return res | rangeBitwiseAnd(left ^ res, right ^ res);
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
