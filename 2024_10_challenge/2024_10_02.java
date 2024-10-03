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
    public int[] arrayRankTransform(int[] arr) {
        /*
         * LeetCode 1331
         *
         * Just pay attention that the repeated values do not consume extra
         * rank. In other words, if we have sorted arr as [1,1,2], the rank for
         * 2 is 2, instead of 3.
         *
         * O(NlogN), 21 ms, faster than 98.60%
         */
        int[] tmp = new int[arr.length];
        for (int i = 0; i < arr.length; i++)
            tmp[i] = arr[i];
        Arrays.sort(tmp);
        Map<Integer, Integer> ranks = new HashMap<>();
        int r = 1;
        for (int t : tmp) {
            if (!ranks.containsKey(t))
                ranks.put(t, r++);
        }
        for (int i = 0; i < arr.length; i++)
            tmp[i] = ranks.get(arr[i]);
        return tmp;
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
