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
    public int[] decrypt(int[] code, int k) {
        /*
         * LeetCode 1652
         *
         * Prefix sum. The idea is simple, but the implementation requires some
         * thought.
         *
         * O(N), 0 ms, faster than 100.00%
         */
        int N = code.length;
        int[] psum = new int[N];
        psum[0] = code[0];
        for (int i = 1; i < N; i++)
            psum[i] = psum[i - 1] + code[i];
        int[] res = new int[N];
        if (k == 0)
            return res;
        for (int i = 0; i < N; i++) {
            if (k > 0) {
                int end = i + k;
                if (end < N)
                    res[i] = psum[end] - psum[i];
                else
                    res[i] = psum[N - 1] - psum[i] + psum[end - N];
            } else {
                int st = i + k;
                if (st >= 0)
                    res[i] = psum[i - 1] - (st == 0 ? 0 : psum[st - 1]);
                else
                    res[i] = (i == 0 ? 0 : psum[i - 1]) + psum[N - 1] - psum[N + st - 1];
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
