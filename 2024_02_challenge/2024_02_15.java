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
    public long largestPerimeter(int[] nums) {
        /*
        LeetCode 2971
        
        Sort the array and then prefix sum
        
        O(NlogN) time, O(1) space, 29 ms, faster than 69.56%
        */
        Arrays.sort(nums);
        long res = -1;
        long pre = 0;
        for (int n : nums) {
            if (pre > n) {
                res = pre + n;
            }
            pre += n;
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
