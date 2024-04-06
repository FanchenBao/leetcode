import java.util.*;
import java.util.stream.Collectors;
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
    public String makeGood(String s) {
        /*
         * LeetCode 1544
         *
         * Use stack
         */
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (!stack.isEmpty() && Math.abs(stack.peek() - c) == 32)
                stack.pop();
            else
                stack.push(c);
        }
        String res = "";
        for (char c : stack)
            res += c;
        return res;
    }
}


class Solution {
    public String makeGood(String s) {
        /*
         * LeetCode 1544
         *
         * Turn s into a char array and change in place
         *
         * Note that the string construction method used in solution 1 is very
         * slow. In the current solution, we simply return the string version
         * the char array. It's much much faster.
         *
         * 1 ms, faster than 100.00%
         */
        char[] chars = new char[100];
        int i = 0;
        for (int j = 0; j < s.length(); j++) {
            if (i > 0 && (s.charAt(j) - chars[i - 1] == 32 || s.charAt(j) - chars[i - 1] == -32))
                i--;
            else
                chars[i++] = s.charAt(j);
        }
        return String.valueOf(Arrays.copyOfRange(chars, 0, i));
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
