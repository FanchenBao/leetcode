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
    public String customSortString(String order, String s) {
        /*
        LeetCode 791
        
        Custome sort by assigning an index value to each letter in order.
        
        O(NlogN), 4 ms, faster than 24.18%
        */
        // Create order index
        int[] orderIdx = new int[26];
        Arrays.fill(orderIdx, 26);
        for (int i = 0; i < order.length(); i++)
            orderIdx[order.charAt(i) - 97] = i;
        
        // Convert s to Character array
        Character[] sArr = new Character[s.length()];
        for (int i = 0; i < s.length(); i++)
            sArr[i] = s.charAt(i);
        
        // Custom sort Character array
        Arrays.sort(sArr, (s1, s2) -> orderIdx[s1 - 97] - orderIdx[s2 - 97]);
        
        // Convert back to string
        StringBuilder res = new StringBuilder();
        for (char c : sArr)
            res.append(c);
        return res.toString();
    }
}


class Solution2 {
    public String customSortString(String order, String s) {
        /*
         * First produce the frequencies of s, and then build the sorted string
         * directly by going from left to right on order.
         *
         * O(N), 0 ms, faster than 100.00%
         */
        int[] freq = new int[26];
        StringBuilder res = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (order.indexOf(c) < 0)
                res.append(c);
            else
                freq[c - 97]++;
        }
        for (char c : order.toCharArray()) {
            for (int i = 0; i < freq[c - 97]; i++)
                res.append(c);
        }
        return res.toString();
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
