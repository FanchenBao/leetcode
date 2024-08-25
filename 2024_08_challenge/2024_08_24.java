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
    public String nearestPalindromic(String n) {
        /*
        LeetCode 564
        
        A lot of trial and error. Three options, one is to intentionally make the
        palindrome smaller by reducing the values from the middle. One is to create
        the palindrome directly. And the last is to intentionally make the palindrome
        bigger by increasing the values from the middle.
        */
        int len = n.length();
        // option 1, reduce the number from the middle
        char[] op1 = n.toCharArray();
        int i = (len - 1) / 2;
        while (op1[i] == '0')
            i--;
        op1[i]--;
        // position from which we need to assign 9
        if (op1[0] == '0') {
            for (int j = i + 1; j < len; j++)
                op1[j] = '9';
        } else {
            for (int j = i + 1; j <= (len - 1) / 2; j++)
                op1[j] = '9';
            i = len / 2 - 1;
            // produce palindrome
            for (int j = (len + 1) / 2; j < len; j++)
                op1[j] = op1[i--];
        }
        String op1Str = String.valueOf(op1);

        // option 2, use the left half to create palindrome
        String lh = n.substring(0, len / 2);
        String op2Str = lh + n.substring(len / 2, (len + 1) / 2) + new StringBuilder(lh).reverse().toString();
        
        // option 3, increase the number from the middle
        char[] op3 = n.toCharArray();
        i = (len - 1) / 2;
        while (i >= 0 && op3[i] == '9')
            i--;
        // position from which we need to assign 0
        if (op3[0] == '9') {
            op3 = new char[len + 1];
            for (int j = 1; j < len; j++)
                op3[j] = '0';
            op3[0] = '1';
            op3[len] = '1';
        } else {
            op3[i]++;
            for (int j = i + 1; j <= (len - 1) / 2; j++)
                op3[j] = '0';
            i = len / 2 - 1;
            // produce palindrome
            for (int j = (len + 1) / 2; j < len; j++)
                op3[j] = op3[i--];
        }
        String op3Str = String.valueOf(op3);

        // Compare which option is better
        long N = Long.parseLong(n);
        List<Long> ops = Arrays.asList(Long.parseLong(op1Str), Long.parseLong(op2Str), Long.parseLong(op3Str));
        ops.sort((a, b) -> Long.compare(Math.abs(N - a), Math.abs(N - b)));
        return N == ops.get(0) ? String.valueOf(ops.get(1)) : String.valueOf(ops.get(0));
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
