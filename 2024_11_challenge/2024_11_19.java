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
    public long maximumSubarraySum(int[] nums, int k) {
        /*
         * LeetCode 2461
         *
         * Use a counter to keep track of the frequencies of elements in each
         * subarray of size k. The size of the counter is the number of uniques
         * in the subarray.
         *
         * O(N), 71 ms, faster than 5.91%
         */
        Map<Integer, Integer> counter = new HashMap<>();
        int i = 0;
        long res = 0;
        long s = 0;
        for (int j = 0; j < nums.length; j++) {
            s += (long)nums[j];
            counter.put(nums[j], counter.getOrDefault(nums[j], 0) + 1);
            if (j - i + 1 > k) {
                s -= (long)nums[i];
                counter.put(nums[i], counter.get(nums[i]) - 1);
                if (counter.get(nums[i]) == 0)
                    counter.remove(nums[i]);
                i++;
            }
            if (counter.size() == k)
                res = Math.max(res, s);
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
