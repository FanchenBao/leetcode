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
    public List<List<Integer>> subsets(int[] nums) {
        /*
         * LeetCode 78
         *
         * Use bitmask to produce all combinations of nums.
         *
         * 0 ms, faster than 100.00%
         */
        int N = nums.length;
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < (1 << N); i++) {
            List<Integer> tmp = new ArrayList<>();
            for (int j = 0; j < N; j++) {
                if ((i & (1 << j)) > 0)
                    tmp.add(nums[j]);
            }
            res.add(tmp);
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
