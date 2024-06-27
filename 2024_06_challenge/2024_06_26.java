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

class Solution {
    private void traverse(TreeNode node, List<Integer> lst) {
        if (node == null)
            return;
        traverse(node.left, lst);
        lst.add(node.val);
        traverse(node.right, lst);
    }

    private TreeNode createBalancedBST(List<Integer> lst, int lo, int hi) {
        if (lo > hi)
            return null;
        if (lo == hi)
            return new TreeNode(lst.get(lo));
        int mid = (lo + hi) / 2;
        return new TreeNode(lst.get(mid), createBalancedBST(lst, lo, mid - 1), createBalancedBST(lst, mid + 1, hi));

    }

    public TreeNode balanceBST(TreeNode root) {
        /*
         * LeetCode 1382
         *
         * This solution feels like a cheat because we are not rearranging the
         * original tree. Instead, we obtain the sorted values of the original
         * BST and recreate a new one that is balanced.
         *
         * O(N), 2 ms, faster than 96.27%
         */
        List<Integer> lst = new ArrayList<>();
        traverse(root, lst);
        return createBalancedBST(lst, 0, lst.size() - 1);
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
