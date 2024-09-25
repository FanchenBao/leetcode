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
    public int longestCommonPrefix(int[] arr1, int[] arr2) {
        /*
         * LeetCode 3043
         *
         * Create a Trie for one of the arrays, and use the other array to
         * match the Trie. Keep count of the matching prefixes.
         *
         * O(M + N), where M is the total number of characters in arr1 and
         * N is the total number of characters in arr2.
         *
         * 102 ms, faster than 36.94%
         */
        TrieNode root = new TrieNode();
        for (int a : arr1) {
            String s = String.valueOf(a);
            TrieNode node = root;
            for (char c : s.toCharArray()) {
                node.children.putIfAbsent(c, new TrieNode());
                node = node.children.get(c);
            }
            node.isWord = true;
        }
        int res = 0;
        for (int a : arr2) {
            String s = String.valueOf(a);
            TrieNode node = root;
            int cnt = 0;
            for (char c : s.toCharArray()) {
                if (node.children.containsKey(c)) {
                    node = node.children.get(c);
                    cnt++;
                } else {
                    break;
                }
                res = Math.max(res, cnt);
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
