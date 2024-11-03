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
    public boolean isCircularSentence(String sentence) {
        /*
         * LeetCode 2490
         *
         * 1 ms, faster than 96.81%
         */
        int N = sentence.length();
        if (sentence.charAt(0) != sentence.charAt(N - 1))
            return false;
        for (int i = 0; i < N; i++) {
            if (sentence.charAt(i) == ' ' && sentence.charAt(i - 1) != sentence.charAt(i + 1))
                return false;
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
