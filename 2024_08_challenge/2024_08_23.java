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
    private int gcd(int a, int b) {
        return a == 0 ? b : gcd(b % a, a);
    }

    private int[] add(int[] frac1, int[] frac2) {
        // Note that we intentionally keep the sign attached to the numerator
        // and keep the denominator always positive.
        int den = frac1[1] * frac2[1];
        int num = frac1[0] * frac2[1] + frac2[0] * frac1[1];
        num = den * num >= 0 ? Math.abs(num) : -Math.abs(num);
        den = Math.abs(den);
        int g = gcd(den, Math.abs(num));
        return new int[]{num / g, den / g};
    }

    public String fractionAddition(String expression) {
        /*
         * LeetCode 592
         *
         * Not a difficult one, but need to be very careful when parsing the
         * expression and performing the addition.
         *
         * 3 ms, faster than 85.78%
         */
        int sign = 1;
        int n = 0;
        int[] sum = new int[]{0, 1};
        int[] cur = new int[2];
        for (int i = 0; i < expression.length(); i++) {
            char c = expression.charAt(i);
            if (c == '-') {
                cur[1] = n == 0 ? 1 : n;
                sum = add(sum, cur);
                sign = -1;
                n = 0;
            } else if (c == '+') {
                cur[1] = n;
                sum = add(sum, cur);
                sign = 1;
                n = 0;
            } else if (c == '/') {
                cur[0] = sign * n;
                n = 0;
            } else {
                // just a digit
                n = n * 10 + c - '0';
            }
        }
        cur[1] = n;
        sum = add(sum, cur);
        return String.format("%d/%d", sum[0], sum[1]);
    }
}


class Solution {
    private int gcd(int a, int b) {
        return a == 0 ? b : gcd(b % a, a);
    }

    public String fractionAddition(String expression) {
        /*
         * Using the very smart regex to split expression and end up with only
         * the numbers WITH signs attached to the numerator.
         *
         * 8 ms, faster than 45.87%
         */
        String[] splitted = expression.split("/|(?=[+-])");
        int num = Integer.parseInt(splitted[0]);
        int den = Integer.parseInt(splitted[1]);
        for (int i = 2; i < splitted.length; i += 2) {
            int n = Integer.parseInt(splitted[i]);
            int d = Integer.parseInt(splitted[i + 1]);
            num = num * d + n * den;
            den *= d;
        }
        int g = Math.abs(gcd(num, den));
        return String.format("%d/%d", num / g, den / g);
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
