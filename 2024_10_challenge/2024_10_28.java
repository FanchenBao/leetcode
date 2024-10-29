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
    public int longestSquareStreak(int[] nums) {
        /*
         * LeetCode 2501
         *
         * Sort nums and then use a set to keep track of which number exists
         * in nums. Then go from the smallest num, try its square to see if
         * it is in nums. If it is, continue, otherwise break out.
         *
         * Each number can only be tried once.
         *
         * To speed up, instead of sorting and using a set, we use a boolean
         * array of max size. This way the run time can be O(N)
         *
         * 20 ms, faster than 90.63%
         */
        int MAX = 100001;
        boolean[] eligible = new boolean[MAX];
        for (int n : nums)
            eligible[n] = true;
        int res = 0;
        for (int i = 2; i < MAX; i++) {
            int cnt = 0;
            int j = i;
            while (j >= 0 && j < MAX && eligible[j]) {
                cnt++;
                eligible[j] = false;
                j *= j;
            }
            if (cnt >= 2)
                res = Math.max(res, cnt);
        }
        return res == 0 ? -1 : res;
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
