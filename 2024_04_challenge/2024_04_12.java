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
    public int trap(int[] height) {
        /*
        * LeetCode 42.
        
        Classic problem. Use monotonic decreaseing array to solve.
        */
        int res = 0;
        int prePop = -1;
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < height.length; i++) {
            while (!stack.isEmpty() && height[i] >= height[stack.peek()]) {
                int curPop = stack.pop();
                int d = i - curPop - 1;
                int h = height[curPop] - (prePop >= 0 ? height[prePop] : 0);
                res += d * h;
                prePop = curPop;
            }
            if (!stack.isEmpty() && prePop >= 0) {
                res += (height[i] - height[prePop]) * (i - stack.peek() - 1);
            }
            stack.add(i);
            prePop = -1;
        }
        return res;
    }
}


class Solution2 {
    public int trap(int[] height) {
        /*
         * A better implementation of monotonic decreasing array
         *
         * 6 ms, faster than 12.13% o
         */
        int res = 0;
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < height.length; i++) {
            while (!stack.isEmpty() && height[i] > height[stack.peek()]) {
                int j = stack.pop();
                // compute amount of water between i and stack[-1] above
                // height[j]
                if (!stack.isEmpty()) {
                    res += (Math.min(height[i], height[stack.peek()]) - height[j]) * (i - stack.peek() - 1);
                }
            }
            stack.add(i);
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
