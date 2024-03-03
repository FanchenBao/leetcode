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
    public int[] sortedSquares(int[] nums) {
        /*
         * LeetCode 977
         *
         * Use merge sort to achieve o(N) time complexity.
         
         1 ms, faster than 100.00%
         */
        int k = 0;
        int j = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] >= 0 && j == 0 && k == 0) {
                k = i - 1;
                j = i;
            }
            nums[i] = nums[i] * nums[i];
        }
        if (j == 0 && k == 0) {
            if (nums[0] >= nums[nums.length - 1]) {
                // all numbers are negative
                k = nums.length - 1; j = nums.length;
            } else {
                k = -1; j = 0;
            }
        }
            
        int[] res = new int[nums.length];
        int i = 0;
        // merge sort
        while (k >= 0 && j < nums.length) {
            if (nums[k] < nums[j])
                res[i] = nums[k--];
            else
                res[i] = nums[j++];
            i++;
        }
        while (k >= 0 && i < nums.length)
            res[i++] = nums[k--];
        while (j < nums.length && i < nums.length)
            res[i++] = nums[j++];
        return res;
    }
}



class Solution {
    public int[] sortedSquares(int[] nums) {
        /*
         * A two pointer solution inspired by the solution from the previous
         * submission
         *
         */
        int N = nums.length;
        int i = 0;
        int j = N - 1;
        int[] res = new int[N];
        int k = N - 1;
        while (i <= j) {
            int sqi = nums[i] * nums[i];
            int sqj = nums[j] * nums[j];
            if (sqi < sqj) {
                res[k--] = sqj;
                j--;
            } else {
                res[k--] = sqi;
                i++;
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
