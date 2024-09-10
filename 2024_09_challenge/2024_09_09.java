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

/**
 * Definition for singly-linked list.
 */
 class ListNode {
     int val;
     ListNode next;
     ListNode() {}
     ListNode(int val) { this.val = val; }
     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 }
 
class Solution {
    public int[][] spiralMatrix(int m, int n, ListNode head) {
        /*
         * LeetCode 2326
         *
         * Initialize the result matrix with -1; then simulate the process.
         * Each time we hit a cell that has been filled before, we do a clock-
         * wise turn. We keep filling until the entire linked list has been
         * exhausted.
         *
         * O(MN), 10 ms, faster than 16.00%
         */
        int[][] res = new int[m][n];
        for (int[] row : res)
            Arrays.fill(row, -1);
        ListNode node = head;
        int[][] dirs = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int i = 0;
        int j = 0;
        int dirIdx = 0;
        while (node != null) {
            if (i >= 0 && i < m && j >= 0 && j < n && res[i][j] == -1) {
                res[i][j] = node.val;
                node = node.next;
                i += dirs[dirIdx][0];
                j += dirs[dirIdx][1];
            } else {
                i -= dirs[dirIdx][0];
                j -= dirs[dirIdx][1];
                dirIdx = (dirIdx + 1) % 4;
                i += dirs[dirIdx][0];
                j += dirs[dirIdx][1];
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
