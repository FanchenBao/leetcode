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
    public void sortColors(int[] nums) {
        /*
         * LeetCode 75
         *
         * One pass with constant space. O(N)
         */
        int lo = 0;
        int hi = nums.length - 1;
        int i = 0;
        while (i <= hi) {
            if (nums[i] == 1) {
                i++;
            } else if (nums[i] == 0) {
                nums[i++] = nums[lo]; // we can move i forward because lo must be pointing to 1
                nums[lo++] = 0;
            } else {
                nums[i] = nums[hi];
                nums[hi--] = 2;
            }
        }
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
