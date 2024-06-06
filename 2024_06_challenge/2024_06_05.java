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
    public List<String> commonChars(String[] words) {
        /*
         * LeetCode 1002
         *
         * Count the frequency of letters in the first word. Then compare the
         * frequencies of all the other words and keep track of the minimum
         * frequencies.
         *
         * O(N * M) 3 ms, faster than 88.78%
         */
        int[] counter = new int[26];
        for (char c : words[0].toCharArray())
            counter[c - 'a']++;
        for (int i = 1; i < words.length; i++) {
            int[] tmp = new int[26];
            for (char c : words[i].toCharArray())
                tmp[c - 'a']++;
            for (int ii = 0; ii < 26; ii++) 
                counter[ii] = Math.min(counter[ii], tmp[ii]);
        }
        List<String> res = new ArrayList<>();
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < counter[i]; j++)
                res.add(String.valueOf((char)('a' + i)));
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
