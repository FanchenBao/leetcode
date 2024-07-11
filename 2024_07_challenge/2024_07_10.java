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
    public int minOperations(String[] logs) {
        /*
         * LeetCode 1598
         *
         * Use an integer to represen the depath of the file tree.
         *
         * O(N), 1 ms, faster than 99.42%
         */
        int folders = 1;
        String backup = "../";
        String stay = "./";
        for (String l : logs) {
            if (l.equals(backup))
                folders -= (folders > 1 ? 1 : 0);
            else if (!l.equals(stay))
                folders++;
        }
        return folders - 1;
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
