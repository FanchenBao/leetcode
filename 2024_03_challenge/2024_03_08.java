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
    public int maxFrequencyElements(int[] nums) {
        /*
         * LeetCode 3005
         *
         * 1 ms, faster than 99.64%
         */
        int[] counter = new int[101];
        for (int n : nums)
            counter[n]++;
        int max = 0;
        int res = 0;
        for (int i = 1; i <= 100; i++) {
            if (counter[i] == max) {
                res += max;
            } else if (counter[i] > max) {
                max = counter[i];
                res = max;
            }
        }
        return res;
    }
}


class Solution1 {
    public int maxFrequencyElements(int[] nums) {
        /*
         * Let's try one pass
         */
        int[] counter = new int[101];
        int max = 0;
        int res = 0;
        for (int n : nums) {
            counter[n]++;
            if (counter[n] == max) {
                res += max;
            } else if (counter[n] > max) {
                max = counter[n];
                res = max;
            }
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
