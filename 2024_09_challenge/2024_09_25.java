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
    int cnt = 0;
    TrieNode[] children = new TrieNode[26];
}

class Solution {
    public int[] sumPrefixScores(String[] words) {
        /*
         * LeetCode 2416
         *
         * A solution purely based on Trie. Build the trie from words and keep
         * count the number of times each trie node is encountered. Then
         * traverse the trie again as we go through the words list again, add
         * up all the counts.
         *
         * O(NK), where N is the length of words and K is the average length
         * of each word.
         *
         * 374 ms, faster than 20.00%
         */
        TrieNode root = new TrieNode();
        for (String w : words) {
            TrieNode node = root;
            for (char c : w.toCharArray()) {
                if (node.children[c - 'a'] == null)
                    node.children[c - 'a'] = new TrieNode();
                node = node.children[c - 'a'];
                node.cnt++;
            }
        }
        int[] res = new int[words.length];
        for (int i = 0; i < words.length; i++) {
            TrieNode node = root;
            for (char c : words[i].toCharArray()) {
                node = node.children[c - 'a'];
                res[i] += node.cnt;
            }
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
