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
    private void reverse(List<Character> arr, int lo, int hi) {
         while (lo < hi) {
            char tmp = arr.get(lo);
            arr.set(lo, arr.get(hi));
            arr.set(hi, tmp);
            lo++;
            hi--;
        }
    }

    public String reverseParentheses(String s) {
        /*
         * LeetCode 1190
         *
         * Using an array to keep track of all the letters. Use a leftPos to
         * keep track of the indices of left paren.
         *
         * When a right paren is encountered, reverse the substring between
         * the last left paren and the current end of array.
         *
         * O(N^2), 1 ms, faster than 99.49%
         */
        List<Character> arr = new ArrayList<>();
        List<Integer> leftPos = new ArrayList<>();
        int idx = 0;
        for (char c : s.toCharArray()) {
            if (c == ')') {
                // reverse the substring by swapping
                reverse(arr, leftPos.remove(leftPos.size() - 1), --idx);
                arr.remove(arr.size() - 1); // pop left parenthesis
            } else {
                arr.add(c);
                if (c == '(')
                    leftPos.add(idx);
                idx++;
            }
        }
        StringBuilder res = new StringBuilder(arr.size());
        for (char c : arr)
            res.append(c);
        return res.toString();
    }
}


class Solution2 {
    public String reverseParentheses(String s) {
        /*
         * This is the official solution using wormhole jumping. Each time we
         * hit a paren, we jump to its paring paren and change the direction
         * of iteration.
         *
         * O(N), 1 ms, faster than 99.49%
         */
        int N = s.length();
        int[] pairs = new int[N];
        StringBuilder res = new StringBuilder();
        Stack<Integer> leftPos = new Stack<>();
        for (int i = 0; i < N; i++) {
            if (s.charAt(i) == '(') {
                leftPos.add(i);
            } else if (s.charAt(i) == ')') {
                int li = leftPos.pop();
                pairs[li] = i;
                pairs[i] = li;
            }
        }
        int dir = 1;
        int idx = 0;
        while (idx >= 0 && idx < N) {
            if (s.charAt(idx) == '(' || s.charAt(idx) == ')') {
                dir *= -1;
                idx = pairs[idx];
                idx += dir;
            } else if (idx >= 0 && idx < N) {
                res.append(s.charAt(idx));
                idx += dir;
            }
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
