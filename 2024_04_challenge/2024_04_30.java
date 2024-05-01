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
    public long wonderfulSubstrings(String word) {
        /*
         * LeetCode 1915
         *
         * Use bitmask to represent the frequency of the parity of each letter
         * among substrings ending at each letter in word.
         * When a new letter is encountered, we update the frequencies, and
         * then accumulate the count of the frequencies whose bit representation
         * contains at most one set bit.
         *
         * O(N * 1024) TLE
         */
        Map<Integer, Integer> bitmask = new HashMap<>();
        int res = 0;
        for (char c : word.toCharArray()) {
            int pos = 1 << (c - 'a');
            Map<Integer, Integer> tmp = new HashMap<>();
            for (int b : bitmask.keySet()) {
                int mask = b ^ pos;
                tmp.put(mask, tmp.getOrDefault(mask, 0) + bitmask.get(b));
            }
            tmp.put(pos, tmp.getOrDefault(pos, 0) + 1);
            for (int b : tmp.keySet())
                res += Integer.bitCount(b) <= 1 ? tmp.get(b) : 0;
            bitmask = tmp;
        }
        return res;
    }
}


class Solution2 {
    public long wonderfulSubstrings(String word) {
        /*
         * Similar idea as above, but we actively search for the possible
         * frequencies to use for the current letter. This avoids
         * calling bitCount repeatedly.
         * 
         * Also, we use an array instead of HashMap
         *
         * O(N * 1024), 1837 ms, faster than 5.66%
         */
        long[] bitmask = new long[1024];
        long res = 0;
        for (char c : word.toCharArray()) {
            int pos = 1 << (c - 'a');
            // All possible previous states that can lead to
            // the current char being the end of a new wonderful
            // substring
            for (int i = 0; i < 10; i++)
                res += bitmask[pos | (1 << i)];
            res += bitmask[0];
            res += 1; // the current char by itself
            // Creating the frequencies of parity of the new substrings
            // ending at the current char
            long[] tmp = new long[1024];
            for (int b = 0; b < 1024; b++) {
                int mask = b ^ pos;
                tmp[mask] += bitmask[b];
            }
            tmp[pos] += 1;
            bitmask = tmp;
        }
        return res;
    }
}


class Solution3 {
    public long wonderfulSubstrings(String word) {
        /*
         * Active search + hashmap
         */
        Map<Integer, Long> bitmask = new HashMap<>();
        long res = 0;
        for (char c : word.toCharArray()) {
            int pos = 1 << (c - 'a');
            // All possible previous states that can lead to
            // the current char being the end of a new wonderful
            // substring
            for (int i = 0; i < 10; i++)
                res += bitmask.getOrDefault(pos | (1 << i), 0);
            res += bitmask.getOrDefault(0, 0);
            res += 1; // the current char by itself

            Map<Integer, Long> tmp = new HashMap<>();
            for (int b : bitmask.keySet()) {
                int mask = b ^ pos;
                tmp.put(mask, tmp.getOrDefault(mask, 0) + bitmask.get(b));
            }
            tmp.put(pos, tmp.getOrDefault(pos, 0) + 1);
            bitmask = tmp;
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
