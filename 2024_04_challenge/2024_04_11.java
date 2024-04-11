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
    public String removeKdigits(String num, int k) {
        /*
        LeetCode 402
        
        Monotonic increasing array.
        O(N), 3 ms, faster than 99.15%
        */
        char[] arr = num.toCharArray();
        int i = 0;
        for (int j = 1; j < arr.length; j++) {
            while (i >= 0 && arr[j] < arr[i] && k > 0) {
                i--;
                k--;
            }
            arr[++i] = arr[j];
        }
        // If there is more k left, we always remove from the
        // right, because arr[:i + 1] is already non-decreasing
        i -= k;
        // remove the leading zeros
        int j = 0;
        while (j <= i && arr[j] == '0')
            j++;
        if (j > i)
            return "0";
        return new String(arr, j, i - j + 1);
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
