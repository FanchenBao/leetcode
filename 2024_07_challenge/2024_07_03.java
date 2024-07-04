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
    public int minDifference(int[] nums) {
        /*
         * LeetCode 1509
         *
         * If size of nums is smaller or equal to 4, we can always make all
         * the values identical within 3 moves.
         *
         * Otherwise, we sort nums and perform a sliding window of size
         * len(nums) - 3. The answer would be the smallest max - min for all
         * the sliding windows.
         *
         * O(NlogN), 15 ms, faster than 96.06%
         */
        int N = nums.length;
        if (N <= 4)
            return 0;
        Arrays.sort(nums);        
        int res = Integer.MAX_VALUE;
        for (int i = N - 3 - 1; i < N; i++)
            res = Math.min(res, nums[i] - nums[i - (N - 3) + 1]);
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
