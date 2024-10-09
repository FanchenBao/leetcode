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
    public int minSwaps(String s) {
        /*
         * LeetCode 1963
         *
         * Use stack. Each time a right bracket is encountered when the stack
         * is empty, that right bracket must be swapped. A left bracket goes
         * to the stack by default. And matching pair (i.e., left bracket on
         * top of stack and right bracket as current character) would pop the
         * stack.
         *
         * O(N), 101 ms, faster than 18.13%
         */
        Stack<Character> stack = new Stack<>();
        int res = 0;
        for (char c : s.toCharArray()) {
            if (c == '[') {
                stack.add(c);
            } else if (stack.isEmpty()) {
                res++;
                stack.add('['); // swap
            } else {
                stack.pop(); // top of stack must be a left bracket
            }
        }
        return res;
    }
}


class Solution2 {
    public int minSwaps(String s) {
        /*
         * Same idea as Solution1 but without actually setting up the stack.
         * Since left bracket is the only element possible in the stack, we
         * just need to track the size of the stack to know if it is empty.
         *
         * 13 ms, faster than 93.08%
         */
        int stackSize = 0;
        int res = 0;
        for (char c : s.toCharArray()) {
            if (c == '[') {
                stackSize++;
            } else if (stackSize == 0) {
                res++;
                stackSize++;
            } else {
                stackSize--;
            }
        }
        return res;
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
