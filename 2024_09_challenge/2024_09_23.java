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

class TrieNode {
    boolean isWord;
    Map<Character, TrieNode> children;
    TrieNode() {
        this.isWord = false;
        this.children = new HashMap<>();
    }
}

class Solution {
    int[] memo;
    int MAX = 1000;

    private int dp(int idx, String s, TrieNode root) {
        if (idx >= s.length())
            return 0;
        if (this.memo[idx] < MAX)
            return this.memo[idx];
        // split here
        this.memo[idx] = Math.min(this.memo[idx], 1 + dp(idx + 1, s, root));
        // try not to split
        int i = idx;
        TrieNode node = root;
        while (i < s.length() && node.children.containsKey(s.charAt(i))) {
            node = node.children.get(s.charAt(i));
            if (node.isWord)
                this.memo[idx] = Math.min(this.memo[idx], dp(i + 1, s, root));
            i++;
        }
        return this.memo[idx];
    }

    public int minExtraChar(String s, String[] dictionary) {
        /*
         * LeetCode 2707
         *
         * Build a Trie out of the dictionary, and then break up s at each
         * possible substring match to the Trie. We can use DP to memoize some
         * of the intermediate results.
         *
         * O(M + N^2), where M is the total number of chars in dictionary, and
         * N is the length of s.
         *
         * 14 ms, faster than 89.12%
         */
        this.memo = new int[s.length()];   
        Arrays.fill(this.memo, MAX);
        TrieNode root = new TrieNode();
        for (String dict : dictionary) {
            TrieNode node = root;
            for (char c : dict.toCharArray()) {
                node.children.putIfAbsent(c, new TrieNode());
                node = node.children.get(c);
            }
            node.isWord = true;
        }
        dp(0, s, root);
        System.out.println(Arrays.toString(this.memo));
        return this.memo[0];
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
