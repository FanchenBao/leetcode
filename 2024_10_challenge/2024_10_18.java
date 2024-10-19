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
    private int getArrOr(int[] nums, int mask) {
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            if ((mask & (1 << i)) != 0)
                res |= nums[i];
        }
        return res;
    }

    public int countMaxOrSubsets(int[] nums) {
        /*
         * LeetCode 2044
         *
         * Since the length of nums is no more than 16, we are confident that
         * the solution is brute force. So we find all possible subsets of
         * nums, compute their array bitwise OR, and find the frequency of the
         * max bitwise OR.
         *
         * O(2^N * N), 77 ms, faster than 22.86%
         */
        int N = nums.length;
        int res = 0;
        int maxOr = 0;
        for (int m = 1; m <= (1 << N) - 1; m++) {
            int curOr = getArrOr(nums, m);
            if (curOr > maxOr) {
                maxOr = curOr;
                res = 1;
            } else if (curOr == maxOr) {
                res++;
            }
        }
        return res;
    }
}


class Solution2 {
    private int count(int[] nums, int idx, int curOr, int maxOr) {
        if (idx == nums.length)
            return curOr == maxOr ? 1 : 0;
        // Either include the current num or not
        return count(nums, idx + 1, curOr | nums[idx], maxOr) + count(nums, idx + 1, curOr, maxOr);
    }

    public int countMaxOrSubsets(int[] nums) {
        /*
         * I did not realize that the max array OR is deterministic. It is the
         * result of ORing everything in nums. Thus we can use recursion to
         * do this problem.
         *
         * 8 ms, faster than 86.00%
         */
        int maxOr = 0;
        for (int n : nums)
            maxOr |= n;
        return count(nums, 0, 0, maxOr);
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
