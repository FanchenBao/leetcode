import java.util.*;
import java.util.stream.Stream;

import sun.util.locale.provider.BreakIteratorProviderImpl;

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

class Solution1 {
    private boolean match (String[] s1, String[] s2, int i1, int i2) {
        // Compare s1[:i1 + 1] + s1[i2:] == s2
        // s1 is no shorter than s2
        for (int i = 0; i <= i1; i++) {
            if (!s1[i].equals(s2[i]))
                return false;
        }
        int j = i1 + 1;
        for (int i = i2; i < s1.length; i++) {
            if (!s1[i].equals(s2[j++]))
                return false;
        }
        return true;
    }

    public boolean areSentencesSimilar(String sentence1, String sentence2) {
        /*
         * LeetCode 1813
         *
         * Sliding window. We know the size of the window, so we try each
         * window on the longer sentence and compare whether the remaining
         * words, if concatenated, form a sentence that is equal to the smaller sentence.
         *
         * O(MN), 1 ms, faster than 96.43% 
         */
        String[] l = sentence1.split("\s");
        String[] s = sentence2.split("\s");
        if (l.length < s.length) {
            String[] tmp = l;
            l = s;
            s = tmp;
        }
        int i = 0;
        for (int j = l.length - s.length - 1; j < l.length; j++) {
            if (match(l, s, i++ - 1, j + 1))
                return true;
        }
        return false;
    }
}


class Solution {
    public boolean areSentencesSimilar(String sentence1, String sentence2) {
        /*
         * From the official solution. We can use two pointers. One check the
         * front and the other check the back. Whenever mismatches happen on
         * the front and the back, the middle part must be the potential
         * inserted element. Our job is to ensure after checking on both ends,
         * the smaller string is completely consumed.
         *
         * O(M + N), 1 ms, faster than 96.43%
         */
        String[] l = sentence1.split("\s");
        String[] s = sentence2.split("\s");
        if (l.length < s.length)
            return areSentencesSimilar(sentence2, sentence1);
        int il = 0;
        int is = 0;
        int jl = l.length - 1;
        int js = s.length - 1;
        while (il < l.length && is < s.length) {
            if (!l[il].equals(s[is]))
                break;
            il++;
            is++;
        }
        while (jl >= il && js >= is) {
            if (!l[jl].equals(s[js]))
                break;
            jl--;
            js--;
        }
        if (is - js == 1)
            return true;
        return false;
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
