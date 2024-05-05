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
    public int numRescueBoats(int[] people, int limit) {
        /*
         * LeetCode 881
         *
         * Sort people and then greedy. Two pointers. The largest weight always
         * try to pair with the smallest.
         *
         * O(N), 16 ms, faster than 97.17%
         */
        Arrays.sort(people);
        int i = 0;
        int res = 0;
        for (int j = people.length - 1; j >= i; j--) {
            if (people[j] + people[i] <= limit)
                i++;
            res++;
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
