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
    private int getBitMask(String str) {
        int mask = 0;
        for (char c : str.toCharArray())
            mask |= (1 << c - 'a');
        return mask;
    }
    
    public int countConsistentStrings(String allowed, String[] words) {
        /*
         * LeetCode 1684
         *
         * Use bit mask to check for matching of letters.
         * If a string is consistent, its OR with allowed shall be allowed.
         * Otherwise, there will be extra set bits. Then if we XOR allowed,
         *
         * O(N * k), where N = len(words), k = average length of each word
         * in the words array. 6 ms, faster than 88.76% 
         */
        int allowedMask = getBitMask(allowed);
        int res = 0;
        for (String w : words)
            if (((getBitMask(w) | allowedMask) ^ allowedMask) == 0)
                res++;
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
