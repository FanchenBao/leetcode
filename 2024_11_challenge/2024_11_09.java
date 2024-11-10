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
    public long minEnd(int n, int x) {
        /*
         * LeetCode 3133
         *
         * First find out the number of 0 bits in x. Say there are three zero
         * bits. Then these zero bits will go from 000, 001, 010, 011, 100,
         * 101, 110, 111. While keeping the set bits of x intact, we will use
         * this order to fill in the zero bits for each number in the array
         * in order.
         *
         * If n > (1 << numZeros), then we need to append set bit to the left
         * of x. The first set bit will have no zero between it and the left
         * most bit of x. If that is still not enough to fill out n, we will
         * move the set bit to the left and try again, until we hit n.
         *
         * 1 ms, faster than 87.50%
         */
        int totalBits = (int)(Math.log(x) / Math.log(2) + 1);
        int numZeros = totalBits - Integer.bitCount(x);
        int leftMostPos = totalBits- 1;
        if (n > (1 << numZeros)) {
            n -= (1 << numZeros);
            leftMostPos++;
            while (n > (1 << numZeros)) {
                leftMostPos++;
                n -= (1 << numZeros);
                numZeros++;
            }    
        }
        n--; // this is the largest number the zero bits in x can form
        long res = (long)x;
        int i = 0;
        while (n > 0) {
            if ((res & ((long)1 << i)) == 0) {
                if ((n & 1) > 0)
                    res |= ((long)1 << i);
                n >>= 1;
            }
            i++;
        }
        res |= ((long)1 << leftMostPos);
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
