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
    public long maximumHappinessSum(int[] happiness, int k) {
        /*
         * LeetCode 3075
         *
         * Sort happiness and go from the largest to the smallest. Each time
         * a happiness value is encountered, update its value by deducting
         * the number of children already taken.
         *
         * O(NlogN), 34 ms, faster than 97.44%
         */
        Arrays.sort(happiness);
        long res = 0;
        int N = happiness.length;
        for (int i = 0; i < k; i++) {
            int val = happiness[N - i - 1];
            val = Math.max(0, val - i);
            res += (long)val;
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
