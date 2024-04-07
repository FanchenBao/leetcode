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
    public String minRemoveToMakeValid(String s) {
        /*
        LeetCode 1249
        
        Use stack to identify the wrongly placed parentheses.
        Then reconstruct the string by skipping the wrongly
        placed parentheses.
        
        16 ms, faster than 81.21%
        */
        Stack<Integer> stack = new Stack<>();
        char[] chars = s.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == '(') {
                stack.push(i);
            } else if (chars[i] == ')') {
                if (!stack.isEmpty())
                    stack.pop();
                else
                    chars[i] = '#';
            }
        }
        for (int i : stack)
            chars[i] = '#';
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] != '#')
                res.append(chars[i]);
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
