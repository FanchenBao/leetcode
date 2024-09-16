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
    public int findTheLongestSubstring(String s) {
        /*
         * LeetCode 1371
         *
         * Use prefix XOR to mark the parity of all vowels in s. Our goal is
         * to find the longest subarray of the prefix XOR whoes XOR is equal
         * to zero. We can keep track of the first time any vowel bitmask
         * appears. Then when the same bitmask appears again, we know the
         * subarray bounded by the two appearances have the bitmask equal to
         * zero.
         *
         * The bitmask is a way to mark the parity. For instance, given the
         * positions of the vowel as aeiou, a bit mask of 11001 means that
         * letters a, e, and u appear odd number of times, whereas letters i
         * and o appear even number of times.
         *
         * O(N), 12 ms, faster than 78.29%
         */
        // bitmaskPos records the index of first appearance of all possible
        // vowel bitmasks.
        int[] bitmaskPos = new int[1 << 5];        
        Arrays.fill(bitmaskPos, -1);
        int mask = 0;
        int res = 0;
        // letter position records which position in the bitmask a vowel
        // corresponds to.
        int[] letterPos = new int[26];
        Arrays.fill(letterPos, -1);
        String vowels = "aeiou";
        for (int i = 0; i < vowels.length(); i++)
            letterPos[vowels.charAt(i) - 'a'] = i;
        for (int i = 0; i < s.length(); i++) {
            char c= s.charAt(i);
            int shift = letterPos[c - 'a'];
            if (shift >= 0)
                mask ^= (1 << shift);
            if (mask == 0)
                res = i + 1;
            else if (bitmaskPos[mask] >= 0)
                res = Math.max(res, i - bitmaskPos[mask]);
            else
                bitmaskPos[mask] = i;
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
