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
    public int maxSatisfied(int[] customers, int[] grumpy, int minutes) {
        /*
         * LeetCode 1052
         *
         * Prefix sum + sliding window.
         *
         * O(N), 4 ms, faster than 48.61%
         */
        int N = customers.length;
        int[] presum = new int[N];
        presum[0] = grumpy[0] == 1 ? 0 : customers[0];
        for (int i = 1; i < N; i++)
            presum[i] = presum[i - 1] + (grumpy[i] == 1 ? 0 : customers[i]);
        int res = 0;
        int cur = 0;
        for (int i = 0; i < N; i++) {
            cur += customers[i];
            if (i >= minutes) {
                cur -= customers[i - minutes];
            }
            res = Math.max(res, cur + (i >= minutes ? presum[i - minutes] : 0) + presum[N - 1] - presum[i]);
        }
        return res;
    }
}


class Solution2 {
    public int maxSatisfied(int[] customers, int[] grumpy, int minutes) {
        /*
         * This is from the official solution. We just use sliding window to
         * find the max number of conversion from unsatisfied to satisfied.
         * Then we add the max conversion to the already satisfied.
         * O(N), 2 ms, faster than 100.00%
         */
        int N = customers.length;
        int alreadySat = 0;
        for (int i = 0; i < N; i++)
            alreadySat += (1 - grumpy[i]) * customers[i];
        int maxUnsat = 0;
        int cur = 0;
        for (int i = 0; i < N; i++) {
            cur += grumpy[i] * customers[i];
            if (i >= minutes) {
                cur -= grumpy[i - minutes] * customers[i - minutes];
            }
            maxUnsat = Math.max(maxUnsat, cur);
        }
        return alreadySat + maxUnsat;
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
