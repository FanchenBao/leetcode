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
    public int subarraysDivByK(int[] nums, int k) {
        /*
         * LeetCode 974
         *
         * Prefix sum and MOD k and get counter of all the remainders. For
         * all the repeats of the same remainder, we can choose any two from
         * them to for a subarray with sum divisible by k. An edge case is
         * when the remainder is zero, in which case, we need to add additional
         * count of the zero remainders.
         *
         * O(N), 20 ms, faster than 74.54%
         */
        Map<Integer, Integer> counter = new HashMap<>();
        int presum = 0;
        for (int n : nums) {
            presum += n;
            int r = (presum % k + k) % k;
            counter.put(r, counter.getOrDefault(r, 0) + 1);
        }
        int res = 0;
        for (int r : counter.keySet()) {
            int c = counter.get(r);
            res += (c - 1) * c / 2;
            if (r == 0)
                res += c;
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
