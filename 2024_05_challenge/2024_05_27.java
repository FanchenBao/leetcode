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
    public int specialArray(int[] nums) {
        /*
         * LeetCode 1608
         *
         * Sort nums and count from right to left.
         *
         * O(NlogN), 2 ms, faster than 47.70%
         */
        Arrays.sort(nums);
        int cnt;
        for (int i = nums.length - 1; i >= 0; i--) {
            cnt = nums.length - i;
            if ((i == 0 || nums[i - 1] < cnt) && (nums[i] >= cnt))
                return cnt;
        }
        return -1;
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
