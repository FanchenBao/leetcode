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
    public int findDuplicate(int[] nums) {
        /*
         * LeetCode 287
         *
         * This solution does not satisfy the requirement because it is O(N)
         * in extra space.
         *
         * 1 ms, faster than 100.00%
         */
        boolean[] seen = new boolean[nums.length];
        for (int n : nums) {
            if (seen[n])
                return n;
            seen[n] = true;
        }
        return -1;
    }
}


class Solution {
    public int findDuplicate(int[] nums) {
        /*
         * The O(N) time and O(1) space solution is hare and tortoise to find
         * the starting position of a cycle in a linked list.
         *
         * 4 ms, faster than 85.61%
         */
        int slow = 0;
        int fast = 0;
        while (slow != fast || slow == 0) {
            fast = nums[nums[fast]];
            slow = nums[slow];
        }
        slow = 0;
        while (slow != fast) {
            fast = nums[fast];
            slow = nums[slow];
        }
        return slow;
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
