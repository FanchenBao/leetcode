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
    public int minDays(int[] bloomDay, int m, int k) {
        /*
         * LeetCode 1482
         *
         * Binary search. Given a number of days, try to see if we can form
         * m bouquets with k consecutive flowers per bouquet on the available
         * flowers in bloomDay.
         *
         * O(NlogN) 22 ms, faster than 36.36%
         */
        if ((long)m * k > bloomDay.length)
            return -1;
        long lo = 1000000001;
        long hi = 0;
        for (int b : bloomDay) {
            lo = Math.min(b, lo);
            hi = Math.max(b, hi);
        }
        hi++;
        while (lo < hi) {
            long mid = (lo + hi) / 2;
            int conseqCnt = 0;
            int bouq = 0;
            for (int b : bloomDay) {
                if (b <= mid) {
                    conseqCnt++;
                } else {
                    bouq += conseqCnt / k;
                    conseqCnt = 0;
                }
            }
            bouq += conseqCnt / k;
            if (bouq >= m)
                hi = mid;
            else
                lo = mid + 1;
        }
        return (int)lo;
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
