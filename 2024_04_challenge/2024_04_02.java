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
    public boolean isIsomorphic(String s, String t) {
        /*
         * LeetCode 205
         *
         * Convert s and t to their pattern.
         */
        int[] spat = new int[26];
        int[] tpat = new int[26];
        StringBuilder sp = new StringBuilder();
        StringBuilder tp = new StringBuilder();
        int spp = 1;
        int tpp = 1;
        for (int i = 0; i < s.length(); i++) {
            if (spat[s.charAt(i) - 97] == 0)
                spat[s.charAt(i) - 97] = spp++;
            if (tpat[t.charAt(i) - 97] == 0)
                tpat[t.charAt(i) - 97] = tpp++;
            sp.append(spat[s.charAt(i) - 97]);
            tp.append(tpat[t.charAt(i) - 97]);
        }
        return sp.equals(tp);
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
