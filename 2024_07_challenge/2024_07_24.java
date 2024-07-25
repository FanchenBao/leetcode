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
    private int convert(int ori, int[] mapping) {
        int mul = 1;
        int res = 0;
        if (ori == 0)
            return mapping[ori];
        while (ori > 0) {
            res += (mapping[ori % 10]) * mul;
            ori /= 10;
            mul *= 10;
        }
        return res;
    }

    public int[] sortJumbled(int[] mapping, int[] nums) {
        /*
         * LeetCode 2191
         *
         * Convert the numbers and then sort them
         * O(NlogN), 93 ms, faster than 77.45%
         */
        int[][] tmp = new int[nums.length][2];
        for (int i = 0; i < nums.length; i++)
            tmp[i] = new int[]{convert(nums[i], mapping), i};
        Arrays.sort(tmp, (a, b) -> {
            if (a[0] == b[0])
                return Integer.compare(a[1], b[1]);
            return Integer.compare(a[0], b[0]);
        });
        int[] res = new int[nums.length];
        for (int i = 0; i < nums.length; i++)
            res[i] = nums[tmp[i][1]];
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
