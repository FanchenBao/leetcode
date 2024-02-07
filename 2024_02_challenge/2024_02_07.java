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
    public String frequencySort(String s) {
        /*
        LeetCode 451
        
        Get the frequencies of each letter, sort them, and then produce
        a new string with frequencies in reverse order.
        
        O(N), 9 ms, faster than 88.41%
        */
        int[][] sortedFreq = new int[128][2];
        for (int i = 0; i < s.length(); i++) {
            sortedFreq[s.charAt(i)][0]++;
            sortedFreq[s.charAt(i)][1] = s.charAt(i);
        }
        // Sort frequency decreasing
        Arrays.sort(sortedFreq, (a, b) -> Integer.compare(b[0], a[0]));
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < sortedFreq.length; i++) {
            if (sortedFreq[i][0] == 0)
                break;
            res.append(Character.toString(sortedFreq[i][1]).repeat(sortedFreq[i][0]));
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
