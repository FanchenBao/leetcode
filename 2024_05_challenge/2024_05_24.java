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
    int[] counter = new int[26];
    int[] score;
    String[] words;

    private boolean canUseWord(String word) {
        int[] req = new int[26];
        for (char c : word.toCharArray())
            req[c - 'a']++;
        for (char c : word.toCharArray()) {
            if (req[c - 'a'] > this.counter[c - 'a'])
                return false;
        }
        return true;
    }

    private int backtrack(int idx) {
        if (idx == this.words.length)
            return 0;
        // do not use the current word
        int res = backtrack(idx + 1);
        if (canUseWord(this.words[idx])) {
            // use word
            int cur = 0;
            for (char c : this.words[idx].toCharArray()) {
                cur += this.score[c - 'a'];
                this.counter[c - 'a']--;
            }
            res = Math.max(res, cur + backtrack(idx + 1));
            // backtrack
            for (char c : this.words[idx].toCharArray())
                this.counter[c - 'a']++;
        }
        return res;
    }

    public int maxScoreWords(String[] words, char[] letters, int[] score) {
        /*
         * LeetCode 1255
         *
         * Since the length of words is no more than 14, we can use O(2^N)
         * strategy for this problem. It is essentially knapsack problem.
         *
         * 1 ms, faster than 80.58%
         */
        for (char c : letters)
            this.counter[c - 'a']++;
        this.score = score;
        this.words = words;
        return backtrack(0);
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
