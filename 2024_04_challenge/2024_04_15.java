import java.util.*;
import java.util.stream.Stream;
import java.math.*;

/**
 * Definition for a binary tree node.
 */
class TreeNode {
   int val;
   TreeNode left;
   TreeNode right;
   TreeNode() {}
   TreeNode(int val) { this.val = val; }
   TreeNode(int val, TreeNode left, TreeNode right) {
       this.val = val;
       this.left = left;
       this.right = right;
   }
}

class Solution1 {
    int[] powerOfTen = new int[]{1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000};

    private List<int[]> helper(TreeNode node) {
        List<int[]> res = new ArrayList<>();
        if (node == null)
            return res;
        if (node.left == null && node.right == null) {
            // leaf
            res.add(new int[]{node.val, 1});
            return res;
        }
        for (int[] tup : helper(node.left))
            res.add(new int[]{tup[0] + node.val * powerOfTen[tup[1]], tup[1] + 1});
        for (int v : helper(node.right))
            res.add(new int[]{tup[0] + node.val * powerOfTen[tup[1]], tup[1] + 1});
        return res;
    }
    public int sumNumbers(TreeNode root) {
        /*
        LeetCode 129
        
        DFS to build a list of tuples, where tuple[0] is the number formed by
        the childen and tuple[1] is the number of digits.

        0 ms, faster than 100.00%
        */
        int res = 0;
        for (int[] tup : helper(root))
            res += tup[0];
        return res;
    }
}


class Solution2 {
    private int helper(TreeNode node, int preVal) {
        if (node == null)
            return 0;
        int cur = preVal * 10 + node.val;
        if (node.left == null && node.right == null)
            return cur;
        return helper(node.left, cur) + helper(node.right, cur);
    }

    public int sumNumbers(TreeNode root) {
        /*
         * Much better implementation of DFS
         *
         * 0 ms, faster than 100.00%
         */
        return helper(root, 0);    
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
