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
    List<Integer>[][] memo;

    private int op(char operator, int a, int b) {
        switch (operator) {
            case '+':
                return a + b;
            case '*':
                return a * b;
            case '-':
                return a - b;
            default:
                return 0; // should not reach here
        }
    }

    private List<Integer> dp(int lo, int hi, String expression) {
        if (this.memo[lo][hi] != null)
            return this.memo[lo][hi];
        this.memo[lo][hi] = new ArrayList<>();
        for (int i = lo; i <= hi; i++) {
            char c = expression.charAt(i);
            if (c >= '0' && c <= '9')
                continue;
            for (int lv : dp(lo, i - 1, expression)) {
                for (int rv : dp(i + 1, hi, expression))
                    this.memo[lo][hi].add(op(c, lv, rv));
            }
        }
        if (this.memo[lo][hi].isEmpty())
            this.memo[lo][hi].add(Integer.parseInt(expression.substring(lo, hi + 1)));
        return this.memo[lo][hi];
    } 

    public List<Integer> diffWaysToCompute(String expression) {
        /*
         * LeetCode 241 (Fail!)
         *
         * Two days in a row I failed to solve the problem. What's even worse
         * is that I solved both of them the first time, although those
         * solutions were not optimal.
         *
         * I was trying many recursion ideas but I either end up with one
         * fewer result or one more result than the expected answer. And I was
         * stuck at how the recursion should be.
         *
         * I then tried to find a way to thoroughly add parenthesis, but that
         * turned out also very difficult.
         *
         * What I didn't do was analyzing based on the operator. The key idea
         * here is that no matter how you group the numbers and operators,
         * there will always be one operator that is executed at the end.
         * Using this as the constant anchor, we can exhaustively divide the
         * expression into the left half and right half.
         *
         * O(N* 2^N) 1 ms, faster than 99.68%
         */
        this.memo = new ArrayList[expression.length()][expression.length()];
        return dp(0, expression.length() - 1, expression);
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
