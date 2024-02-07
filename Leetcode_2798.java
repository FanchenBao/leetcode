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

class Solution1 {
    public int numberOfEmployeesWhoMetTarget(int[] hours, int target) {
        /*
         * This is the very first Java one-liner solution I have ever written.
         *
         * Kind of slow though. 4 ms, faster than 10.51%
         */
        return Arrays.stream(hours).reduce(0, (partial, hour) -> partial + (hour >= target ? 1 : 0));
    }
}

class Solution2 {
    public int numberOfEmployeesWhoMetTarget(int[] hours, int target) {
        /*
         * Much faster: 0 ms, faster than 100.00%
         */
        int res = 0;
        for (int h : hours)
            res += h >= target ? 1 : 0;
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
