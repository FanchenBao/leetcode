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
    private int getCount(int[] nums, int idx, int tgt) {
        // count the number of values in nums that are no more than tgt larger
        // then nums[idx]
        int i = Arrays.binarySearch(nums, nums[idx] + tgt);
        while (i >= 0 && i < nums.length && nums[i] == nums[idx] + tgt)
            i++;
        if (i < 0)
            i = -(i + 1);
        return i - idx - 1;
    }

    public int smallestDistancePair(int[] nums, int k) {
        /*
         * LeetCode 719
         *
         * Binary search to find the kth smallest diff. We suppose the target
         * diff is mid; then we count the number of pairs with diff smaller or
         * equal to mid and smaller or equal to mid - 1. Based on these two
         * data points, we will know whether mid is the kth smallest diff.
         * If not, we decide whether to search with the upper half or lower half.
         *
         * O(NlogN), 55 ms, faster than 19.73%
         */
        Arrays.sort(nums);
        int N = nums.length;
        int lo = 0;
        int hi = nums[N - 1] - nums[0] + 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            int cntIncludeMid = 0;
            int cntNotIncludeMid = 0;
            for (int i = 0; i < N; i++) {
                cntIncludeMid += getCount(nums, i, mid);
                cntNotIncludeMid += getCount(nums, i, mid - 1);
            }
            if (cntIncludeMid < k) {
                lo = mid + 1;
            } else if (cntNotIncludeMid >= k) {
                hi = mid;
            } else {
                lo = mid;
                break;
            }
        }
        return lo;
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
