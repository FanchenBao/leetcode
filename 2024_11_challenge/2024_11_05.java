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
    public int minChanges(String s) {
        /*
         * LeetCode 2914
         *
         * We go from left to right, the first two letters have to the same.
         * If they are not, we must perform one change. Once they are settled,
         * we need to move on to the next two letters, so on and so forth.
         * Thus the problem can be simplified as finding the number of pairs
         * in s that are not the same.
         *
         * O(N), 3 ms, faster than 97.78%
         */
        int res = 0;
        for (int i = 1; i < s.length(); i += 2) {
            if (s.charAt(i) != s.charAt(i - 1))
                res++;
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
