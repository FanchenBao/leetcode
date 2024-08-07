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
    public int minimumPushes(String word) {
        /*
         * LeetCode 3016
         *
         * Counter the frequencies of all the letters in word. The top 8
         * letters are assigned positions to a single button press, the next 8
         * two presses, etc.
         *
         * O(N), 9 ms, faster than 61.15%
         */
        int[] counter = new int[26];
        for (char c : word.toCharArray())
            counter[c - 'a']--; // to facilitate sort in reverse
        Arrays.sort(counter);
        int res = 0;
        int presses = 0;
        for (int i = 0; i < counter.length && counter[i] != 0; i++) {
            if (i % 8 == 0)
                presses++;
            res -= counter[i] * presses;
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
