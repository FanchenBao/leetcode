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

class Solution1 {
    public int countSubstrings(String s) {
        /*
        LeetCode 647
        
        Standard DP solution.
        
        O(N^2), 11 ms, faster than 35.85%
        */
        List<Integer> pre = null;
        int res = 0;
        for (int i = 0; i < s.length(); i++) {
            List<Integer> cur = new ArrayList<>();
            cur.add(i);
            if (pre != null) {
                for (int j : pre) {
                    if (j - 1 >= 0 && s.charAt(j - 1) == s.charAt(i))
                        cur.add(j - 1);
                }
            }
            if (i - 1 >= 0 && s.charAt(i - 1) == s.charAt(i))
                cur.add(i - 1);
            res += cur.size();
            pre = cur;
        }
        return res;
    }
}


class Solution {

    private int expandPalindrome(String s, int left, int right) {
        int count = 0;
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
            count++;
        }
        return count;
    }

    public int countSubstrings(String s) {
        /*
         * This method is inspired by https://leetcode.com/problems/palindromic-substrings/discuss/105689/Java-solution-8-lines-extendPalindrome
         *
         * It takes one char from s and tries to expand on both sides. Whenever
         * a palindrome shows up that way, we increment the count.
         *
         * O(N^2), 2 ms, faster than 96.29%. This is faster than Solution1
         * because there is no overhead of creating array list.
         */
        int res = 0;
        for (int i = 0; i < s.length(); i++) {
            res += expandPalindrome(s, i, i); // odd length palindrome
            res += expandPalindrome(s, i, i + 1); // even length palindrome
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
