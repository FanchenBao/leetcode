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
    public int longestPalindrome(String s) {
        /*
         * LeetCode 409
         *
         * Count the frequencies of all the letters. Include all the even
         * counts and include the largest odd count, if available. Once
         * the largest odd count has been included, decrement all the
         * odds by one.
         *
         * O(NlogN), 2 ms, faster than 86.01%
         */
        int[] counter = new int[58];
        for (char c : s.toCharArray())
            counter[c - 'A']++;
        Arrays.sort(counter);
        int res = 0;
        boolean oddIncluded = false;
        for (int i = counter.length - 1; i >= 0; i--) {
            int c = counter[i];
            if (c % 2 == 0) {
                res += c;
            } else if (!oddIncluded) {
                res += c;
                oddIncluded = true;
            } else {
                res += c - 1;
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
