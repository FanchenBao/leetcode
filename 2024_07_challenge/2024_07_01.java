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
    public boolean threeConsecutiveOdds(int[] arr) {
        /*
         * LeetCode 1550
         */
        int oddCount = 0;
        for (int i = 0; i < arr.length; i++) {
            oddCount = arr[i] % 2 == 1 ? oddCount + 1 : 0;
            if (oddCount == 3)
                return true;
        }
        return false;
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
