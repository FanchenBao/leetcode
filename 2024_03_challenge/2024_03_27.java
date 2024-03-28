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
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        /*
        LeetCode 713
        
        Two pointers with sliding window.
        O(N)  6 ms, faster than 20.98%
        */
        int j = 0;
        int res = 0;
        int cur = 1;
        for (int i = 0; i < nums.length; i++) {
            j = Math.max(j, i);
            while (j < nums.length) {
                if (cur * nums[j] >= k)
                    break;
                else
                    cur *= nums[j++];
            }
            res += j - i;
            if (j > i)
                cur /= nums[i];
        }
        return res;
    }
}


class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        /*
         * There is a right way to do sliding window. Solution 1 is NOT the
         * right way. This is the right way.
         
         4 ms, faster than 100.00% 
        */
        int i = 0;
        int res = 0;
        int cur = 1;
        for (int j = 0; j < nums.length; j++) {
            cur *= nums[j];
            while (cur >= k && i <= j)
                cur /= nums[i++];
            res += j - i + 1;
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
