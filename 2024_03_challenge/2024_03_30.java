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
    public int subarraysWithKDistinct(int[] nums, int k) {
        /*
         * LeetCode 992
         *
         * Sliding window with two pointers.
         *
         * O(N), 38 ms, faster than 67.21%
         */
        int i = 0;
        int pre = -1;
        int res = 0;
        Map<Integer, Integer> counter = new HashMap<>();
        for (int j = 0; j < nums.length; j++) {
            counter.put(nums[j], counter.getOrDefault(nums[j], 0) + 1);
            while (counter.size() > k && i < j) {
                counter.put(nums[i], counter.get(nums[i]) - 1);
                if (counter.get(nums[i]) == 0) {
                    counter.remove(nums[i]);
                    pre = i;
                }
                i++;
            }
            while (counter.get(nums[i]) > 1 && i < j) {
                counter.put(nums[i], counter.get(nums[i]) - 1);
                i++;
            }
            if (counter.size() == k)
                res += i - pre;
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
