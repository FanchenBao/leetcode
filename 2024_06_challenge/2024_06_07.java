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
    String str;
    TrieNode[] children;
    TrieNode() {
        this.str = null;
        this.children = new TrieNode[26];
        Arrays.fill(this.children, null);
    }
}

class Solution {
    public String replaceWords(List<String> dictionary, String sentence) {
        /*
         * LeetCode 648
         *
         * Create a trie for dictionary, then go through each word in sentence
         * and search its root in the trie. If a root exists, use it. Otherwise
         * use the original word.
         *
         * O(MP + NQ), where M = len(dictionary), N = len(sentence), and P is
         * the average length of the word in the dictionary, and Q is the
         * average length of the word in the sentence.
         *
         * 35 ms, faster than 48.55%
         */
        TrieNode root = new TrieNode();
        for (String dict : dictionary) {
            TrieNode node = root;
            for (char c : dict.toCharArray()) {
                int idx = c - 'a';
                if (node.children[idx] == null)
                    node.children[idx] = new TrieNode();
                node = node.children[idx];
            }
            node.str = dict;
        }
        List<String> resList = new ArrayList<>();
        for (String s : sentence.split("\\s+")) {
            TrieNode node = root;
            for (int i = 0; i < s.length() && node != null && node.str == null; i++)
                node = node.children[s.charAt(i) - 'a'];
            if (node != null && node.str != null)
                resList.add(node.str);
            else
                resList.add(s);
        }
        return String.join(" ", resList);
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
