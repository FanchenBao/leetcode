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
    public int minimumDeletions(String s) {
        /*
         * LeetCode 1653
         *
         * Go through string s one by one. If the current char is 'b', it is
         * in the correct position; thus we don't need to make any change. The
         * min deletion will follow the previous value.
         *
         * If the current char is 'a', there are two options. Either we delete
         * 'a', or we delete all the 'b's before. We choose the smaller of the
         * two.
         *
         * O(N), 18 ms, faster than 99.16%
         */
        int minDel = 0;
        int cntB = 0;
        for (char c : s.toCharArray()) {
            if (c == 'b')
                cntB++;
            else
                minDel = Math.min(minDel + 1, cntB);
        }
        return minDel;
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
