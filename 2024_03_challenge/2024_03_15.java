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
    public int[] productExceptSelf(int[] nums) {
        /*
         * LeetCode 238
         *
         * As required, this solution is O(N), without the use of division,
         * and with O(1) extra space.
         * 2 ms, faster than 73.94%
         */
        int N = nums.length;
        int[] res = new int[N];
        res[N - 1] = nums[N - 1];
        for (int i = nums.length - 2; i >= 0; i--) {
            res[i] = res[i + 1] * nums[i];
        }
        int preprod = 1;
        for (int i = 0; i < N - 1; i++) {
            res[i] = preprod * res[i + 1];
            preprod *= nums[i];
        }
        res[N - 1] = preprod;
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
