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
    public int maximalRectangle(char[][] matrix) {
        /*
         * LeetCode 85
         *
         * Classic hard problem that I think I have solved multiple times.
         * However, this time I still needed a little hint. We use monotonic
         * increasing array for each row with regards to the height at each
         * position. When the top of the stack gets popped, it is guaranteed
         * that all the hights between it and the current are hgiher. And all
         * the heights between it and the new top of stack are also higher.
         * These can form a rectangle with the popped as its height.
         *
         * O(MN), 23 ms, faster than 32.81%
         */
        int M = matrix.length;
        int N = matrix[0].length;
        int[] heights = new int[N + 1];
        int res = 0;
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < M; i++) {
            stack.clear();
            stack.add(-1);
            for (int j = 0; j <= N; j++) {
                heights[j] = (j == N || matrix[i][j] == '0') ? 0 : heights[j] + 1;
                while (stack.peek() != -1 && heights[j] <= heights[stack.peek()]) {
                    res = Math.max(res, heights[stack.pop()] * (j - stack.peek() - 1));
                }
                stack.add(j);
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
