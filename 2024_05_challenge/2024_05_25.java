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
    boolean isEnd;
    TrieNode[] children;
    TrieNode() {
        this.isEnd = false;
        this.children = new TrieNode[26];
        Arrays.fill(this.children, null);
    }
}

class Solution {
    List<String> res = new ArrayList<>();

    private void backtrack(int idx, TrieNode root, List<String> cur, String s) {
        if (idx == s.length()) {
            res.add(String.join(" ", cur));
        } else {
            TrieNode node = root;
            for (int i = idx; i < s.length(); i++) {
                TrieNode next = node.children[s.charAt(i) - 'a'];
                if (next != null) {
                    node = next;
                    if (node.isEnd) {
                        cur.add(s.substring(idx, i + 1));
                        backtrack(i + 1, root, cur, s);
                        // backtracking
                        cur.remove(cur.size() - 1);
                    }
                } else {
                    break;
                }
            }
        }
    }
    
    public List<String> wordBreak(String s, List<String> wordDict) {
        /*
         * LeetCode 140
         *
         * If you know backtracking and Trie, this is not very hard.
         *
         * O(2^N) 1 ms, faster than 94.29%
         */
        TrieNode root = new TrieNode();
        for (String word : wordDict) {
            TrieNode node = root;
            for (char c : word.toCharArray()) {
                if (node.children[c - 'a'] == null)
                    node.children[c - 'a'] = new TrieNode();
                node = node.children[c - 'a'];
            }
            node.isEnd = true;
        }
        backtrack(0, root, new ArrayList<>(), s);
        return this.res;
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
