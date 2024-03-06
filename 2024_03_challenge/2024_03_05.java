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
    public int minimumLength(String s) {
        /*
        LeetCode 1750
        
        Two pointers.
        
        O(N), 6 ms, faster than 24.76%
        */
        int i = 0;
        int j = s.length() - 1;
        while (i < j) {
            if (s.charAt(i) != s.charAt(j))
                return j - i + 1;
            while (i + 1 < j && s.charAt(i) == s.charAt(i + 1))
                i++;
            while (j - 1 > i && s.charAt(j) == s.charAt(j - 1))
                j--;
            i++;
            j--;
        }
        return j - i + 1;
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
