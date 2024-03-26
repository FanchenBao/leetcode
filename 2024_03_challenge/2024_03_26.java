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
    public int firstMissingPositive(int[] nums) {
        /*
         * LeetCode 41
         *
         * This is O(NlogN), does not satisfy the requirement of O(N) time.
         *
         * 13 ms, faster than 21.82%
         */
        Arrays.sort(nums);
        int res = 1;
        for (int n : nums) {
            if (n == res)
                res++;
            else if (n > res)
                break;
        }
        return res;
    }
}


class Solution2 {
    public int firstMissingPositive(int[] nums) {
        /*
         * This is O(N) time and O(1) extra space.
         * Use swaps. If nums[i] = i for all the values in nums, then
         * the first missing positive integer is nums.length.
         * Otherwise, the missing positive integer is the first index
         * i such that nums[i] != i (i > 0).
         
         In the implementation, we need to first decrement all the values
         such that we can fit the positive integers from the start of
         the array.
         
         1 ms, faster than 98.00%
         */
        for (int i = 0; i < nums.length; i++)
            nums[i]--;
        int cur = 0;
        int tmp = 0;
        for (int i = 0; i < nums.length; i++) {
            cur = nums[i];
            while (cur < nums.length && cur >= 0 && nums[cur] != cur) {
                tmp = nums[cur];
                nums[cur] = cur;
                cur = tmp;
            }
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != i)
                return i + 1;
        }
        return nums.length + 1;
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
