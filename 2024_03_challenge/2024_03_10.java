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
    public int[] intersection(int[] nums1, int[] nums2) {
        /*
         * LeetCode 349
         *
         * O(N), 2 ms, faster than 94.84%
         */
        int[] indicator = new int[1001];
        for (int n : nums1) {
            if (indicator[n] == 0)
                indicator[n] = 1;
        }
        List<Integer> resList = new ArrayList<>();
        for (int n : nums2) {
            if (indicator[n] == 1) {
                resList.add(n);
                indicator[n] = 0;
            }
        }
        return resList.stream().mapToInt(Integer::intValue).toArray();
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
