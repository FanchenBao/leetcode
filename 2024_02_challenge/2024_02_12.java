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
    public int majorityElement(int[] nums) {
        /*
         * LeetCode 169
         *
         * Use the Boyer-Moore voting algorithm
         *
         * O(N), 1 ms, faster than 99.82%
         */
        int cand = nums[0];
        int vote = 1;
        for (int i = 1; i < nums.length; i++) {
            vote += (nums[i] == cand ? 1 : -1);
            if (vote == 0) {
                cand = nums[i];
                vote = 1;
            }
        }
        return cand;
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
