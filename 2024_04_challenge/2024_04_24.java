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
    public int tribonacci(int n) {
        /*
        LeetCode 1137
        
        0 ms, faster than 100.00%
        */
        int t0 = 0;
        int t1 = 1;
        int t2 = 1;
        if (n == 0)
            return t0;
        if (n == 1)
            return t1;
        if (n == 2)
            return t2;
        int tmp = 0;
        for (int i = 3; i <= n; i++) {
            tmp = t0 + t1 + t2;
            t0 = t1;
            t1 = t2;
            t2 = tmp;
        }
        return tmp;
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
