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

class Solution1 {
    public int numSteps(String s) {
        /*
         * LeetCode 1404
         *
         * Pure analysis. If the last bit is 0, we shift the pointer left if
         * there is no carry. Otherwise, we add one to 0 and turn the last
         * bit to 1.
         *
         * If the last bit is 1, if there is no carry, we add 1 and create a
         * carry. This also makes the last bit into zero. If there is carry,
         * we automatically turn the bit into zero. In either case, the bit
         * will be discarded and a carry created.
         *
         * Follow these logic, we can reduce the s to just a single bit.
         *
         * O(N), 0 ms, faster than 100.00%
         * 
         */
        int res = 0;
        boolean hasCarry = false;
        int i = s.length() - 1;
        while (i > 0) {
            if (s.charAt(i) == '1') {
                if (!hasCarry)
                    hasCarry = true;
                else
                    i--;
                res++;
            } else {
                if (!hasCarry)
                    res++;
                else
                    res += 2;
                i--;
            }
        }
        return hasCarry ? res + 1 : res;
    }
}


class Solution2 {
    public int numSteps(String s) {
        /*
         * This is the solution from the official solution. It has the same
         * idea as Solution1, but with cleaner and more straightforward
         * implementation
         */
        int res = 0;
        int carry = 0;
        for (int i = s.length() - 1; i > 0; i--) {
            int bit = s.charAt(i) - '0' + carry;
            if (bit % 2 == 1) {
                res += 2;
                carry = 1;
            } else {
                res++;
            }
        }
        return res + carry;
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
