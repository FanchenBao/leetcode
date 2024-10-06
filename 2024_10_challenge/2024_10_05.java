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
    private boolean match(int[] cnt1, int[] cnt2) {
        for (int i = 0; i < cnt1.length; i++) {
            if (cnt1[i] != cnt2[i])
                return false;
        }
        return true;
    }

    public boolean checkInclusion(String s1, String s2) {
        /*
         * LeetCode 567
         *
         * Sliding window and compare the frequency of all substring of the
         * same length as s1 in s2 with s1.
         *
         * O(N), 5 ms, faster than 96.14%
         */
        int[] s1cnt = new int[26];
        for (char c : s1.toCharArray())
            s1cnt[c - 'a']++;
        int[] s2cnt = new int[26];
        int i = 0;
        for (int j = 0; j < s2.length(); j++) {
            s2cnt[s2.charAt(j) - 'a']++;
            if (j - i + 1 == s1.length()) {
                if (match(s1cnt, s2cnt))
                    return true;
                s2cnt[s2.charAt(i++) - 'a']--;
            }
        }
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
