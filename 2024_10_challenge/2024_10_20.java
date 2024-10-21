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
    private int operate(char op, int state) {
        switch (op) {
            case '&':
                return state == 2 ? 2 : 1;
            case '|':
                return state == 1 ? 1 : 2;
            case '!':
                return state == 1 ? 2 : 1;
            default:
                return 0; // should not reach here
        }
    }

    public boolean parseBoolExpr(String expression) {
        /*
         * LeetCode 1106
         * 
         * Use stack. One stack to track the operators and the other stack
         * to track the number of ts and fs under each operator. We also use
         * a dummy operator up front to capture any stray ts and fs.
         *
         * O(N), 8 ms, faster than 71.28%
         */
        Stack<Character> stackOp = new Stack<>();
        stackOp.add('*'); // dummy
        Stack<Integer> stackState = new Stack<>(); // each integer is a bit state where 1 => only f, 2 => only t, and 3 => mixture
        stackState.add(0);
        for (char c : expression.toCharArray()) {
            switch (c) {
                case 't':
                    stackState.add(stackState.pop() | 2);
                    break;
                case 'f':
                    stackState.add(stackState.pop() | 1);
                    break;
                case '&':
                case '|':
                case '!':
                    stackOp.add(c);
                    stackState.add(0);
                    break;
                case ')':
                    int newState = operate(stackOp.pop(), stackState.pop());
                    stackState.add(stackState.pop() | newState);
                    break;
                default:
                    break;
            }
        }
        return stackState.pop() == 2;
    }
}


class Solution2 {
    public boolean parseBoolExpr(String expression) {
        /*
         * This is the solution from myself five years ago. I think it was
         * better than the one I am using this time.
         */
        Stack<Character> stack = new Stack<>();
        for (char c : expression.toCharArray()) {
            if (c == ',' || c == '(')
                continue;
            if (c == ')') {
                int tf = 0;  // bit manipulation, 1 => only f, 2 => only t, 3 => mixture
                while (!stack.isEmpty() && (stack.peek() == 't' || stack.peek() == 'f'))
                    tf = stack.pop() == 't' ? (tf | 2) : (tf | 1);
                switch (stack.pop()) {
                    case '!':
                        stack.add(tf == 1 ? 't' : 'f');
                        break;
                    case '|':
                        stack.add(tf == 1 ? 'f' : 't');
                        break;
                    case '&':
                        stack.add(tf == 2 ? 't' : 'f');
                        break;
                    default:
                        break;
                }
            } else {
                stack.add(c);
            }
        }
        return stack.pop() == 't';
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
