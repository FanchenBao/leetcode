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
    public String makeFancyString(String s) {
        /*
         * LeetCode 1957
         *
         * O(N) 45 ms, faster than 37.21%
         */
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (res.length() >= 2 && c == res.charAt(res.length() - 1) && c == res.charAt(res.length() - 2))
                continue;
            res.append(c);
        }
        return res.toString();
    }
}


class Solution {
    public String makeFancyString(String s) {
        /*
         * In-place two pointer approach
         * O(N), 16 ms, faster than 100.00%
         */
        char[] arr = s.toCharArray();
        int i = 0;
        for (int j = 0; j < arr.length; j++) {
            if (i > 1 && arr[j] == arr[i - 1] && arr[j] == arr[i - 2])
                continue;
            arr[i++] = arr[j];
        }
        return new String(arr, 0, i);
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
