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
    public int maxSubarrayLength(int[] nums, int k) {
        /*
         * LeetCode 2958
         *
         * This is almost exactly the same problem as yesterday. Sliding
         * window
         *
         * O(N) 65 ms, faster than 84.80%
         */
        Map<Integer, Integer> counter = new HashMap<>();
        int res = 0;
        int i = 0;
        for (int j = 0; j < nums.length; j++) {
            counter.put(nums[j], counter.getOrDefault(nums[j], 0) + 1);
            while (i < j && counter.get(nums[j]) > k) {
                counter.put(nums[i], counter.get(nums[i]) - 1);
                i++;
            }
            res = Math.max(res, j - i + 1);
        }
        return res;
    }
}


class Solution2 {
    public int maxSubarrayLength(int[] nums, int k) {
        /*
         * The official solution offers a very cool alternative.
         *
         * We always expand on the right. Once we hit some number that gets
         * its frequency above k, instead of shrinking the window, we slide
         * the entire window to the right. Basically, once we have found some
         * window size of a good array, we never shrink it but only expand it.
         * The condition of expanding is that there is no number whose freq
         * is above k. If there is, we slide the entire window, and as we
         * slide, we decrement the count on the left hand side.
         *
         * At the end, the window will always represent the longest good
         * subarray
         
         O(N), 66 ms, faster than 81.05%
         */
        Map<Integer, Integer> counter = new HashMap<>();
        int i = 0;
        int j = 0;
        int numberOfBad = 0;
        for (; j < nums.length; j++) {
            counter.put(nums[j], counter.getOrDefault(nums[j], 0) + 1);
            if (counter.get(nums[j]) > k)
                numberOfBad++;
            if (numberOfBad > 0) {
                counter.put(nums[i], counter.get(nums[i]) - 1);
                if (counter.get(nums[i]) + 1 > k)
                    numberOfBad--;
                i++;
            }
        }
        return j - i;
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
