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
    public String kthDistinct(String[] arr, int k) {
        /*
         * LeetCode 2053
         *
         * Use hashmap
         *
         * O(N) 6 ms, faster than 91.98%
         */
        Map<String, Integer> counter = new HashMap<>();
        for (String s : arr)
            counter.put(s, counter.getOrDefault(s, 0) + 1);
        int j = 0;
        for (String s : arr) {
            if (counter.get(s) == 1) {
                j++;
                if (j == k)
                    return s;
            }
        }
        return "";
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
