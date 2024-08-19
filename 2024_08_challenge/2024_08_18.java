import java.util.*;
import java.util.stream.Stream;

import jdk.javadoc.internal.doclets.toolkit.util.Comparators;

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
    public int nthUglyNumber(int n) {
        /*
         * LeetCode 264
         *
         * I tried brute force where each integer is checked for its ugliness.
         * It times out of course.
         *
         * Then another idea occurred to me that all the ugly numbers must be
         * the result of some previous ugly number multiplied by 2, 3 or 5.
         * Thus, we can use a priority queue to keep track of the smallest
         * ugly number so far, and from there we can produce new ugly numbers.
         *
         * We have to pay attention to two things. First, duplicates. Second
         * integer overflow.
         *
         * O(NlogN), 53 ms, faster than 14.05%
         */
        PriorityQueue<Long> queue = new PriorityQueue<>((a, b) -> Long.compare(a, b));
        queue.add((long)1);
        long res = 0;
        int[] allowed = new int[]{2, 3, 5};
        Set<Long> seen = new HashSet<>();
        seen.add((long)1);
        while (n > 0) {
            res = queue.poll();
            for (int a : allowed) {
                if (!seen.contains(res * a)) {
                    queue.add(res * a);
                    seen.add(res * a);
                }
            }
            n--;
        }
        return (int)res;
    }
}


class Solution2 {
    public int nthUglyNumber(int n) {
        /*
         * This is the official solution using DP. We will use three pointers
         * for multiples of 2, 3, and 5. The pointer that produces the smallest
         * current ugly number gets to increment to the next. This guarantees
         * that all ugly numbers are produced by previous ugly numbers multiplied
         * by 2, 3 or 5. And since each time we are selecting the min, the
         * produced values are always in order and unique.
         *
         * O(N), 7 ms, faster than 29.91%
         */
        List<Integer> uglies = new ArrayList<>();
        uglies.add(1);
        int[] factors = new int[]{2, 3, 5};
        int[] pointers = new int[3];
        int[] vals = new int[3];
        while (uglies.size() < n) {
            int minVal = Integer.MAX_VALUE;
            for (int i = 0; i < 3; i++) {
                vals[i] = uglies.get(pointers[i]) * factors[i];
                minVal = Math.min(vals[i], minVal);
            }
            for (int i = 0; i < 3; i++) {
                // Crucial step. We need to update any pointer that can achieve
                // the same min val at the current step. This is to avoid duplicates
                if (vals[i] == minVal)
                    pointers[i]++;
            }
            uglies.add(minVal);
        }
        return uglies.get(uglies.size() - 1);
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
