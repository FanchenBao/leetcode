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
    private void swap(char[] arr, int i, int j) {
        char tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    public int maximumSwap(int num) {
        /*
         * LeetCode 670
         *
         * The idea is to find the last occurrence of the max digit in num
         * and swap it with the first non-max digit.
         *
         * We can achieve this using monotonic decreasing stack on the digits
         * of num. After the stack is created, we can go through num and
         * compare the digit with the stack. The first mismatching index in
         * num is the non-max digit to be swapped. Then we just need to find
         * the last occurrence of the max digit, do the swap, and we are done.
         *
         * O(N), 1 ms, faster than 30.39%
         */
        char[] numArr = String.valueOf(num).toCharArray();
        // fill the monotonic decreasing stack
        Stack<Integer> monStack = new Stack<>();
        for (int i = 0; i < numArr.length; i++) {
            while (!monStack.isEmpty() && numArr[monStack.peek()] < numArr[i])
                monStack.pop();
            monStack.add(i);
        }
        // Check for the indices to swap
        int leftIdx = 0;
        int monIdx = 0;
        while (monIdx < monStack.size() && leftIdx < numArr.length && leftIdx == monStack.get(monIdx)) {
            leftIdx++;
            monIdx++;
        }
        if (leftIdx == numArr.length) // no swap needed
            return num;
        while (monIdx + 1 < monStack.size() && numArr[monStack.get(monIdx + 1)] == numArr[monStack.get(monIdx)])
            monIdx++;
        int rightIdx = monStack.get(monIdx);
        swap(numArr, leftIdx, rightIdx);
        return Integer.parseInt(String.valueOf(numArr));
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
