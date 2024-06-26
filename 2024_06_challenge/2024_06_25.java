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
    private int bfs(TreeNode node, int preSum) {
        /*
         * LeetCode 1038
         *
         * During BFS, we hit right subtree first and get the sum of all its
         * nodes.
         *
         * Then we update the current node's value. Pay attention that the
         * current node needs also to inherit value from its parent, if it is
         * the left child.
         *
         * Finally, we return the total sum of the current subtree.
         *
         * 0 ms, faster than 100.00%
         */
        if (node == null)
            return 0;
        int rsum = bfs(node.right, preSum);
        node.val += preSum + rsum;
        return node.val - preSum + bfs(node.left, node.val);
    }

    public TreeNode bstToGst(TreeNode root) {
        bfs(root, 0);
        return root;
    }
}


class Solution2 {
    int rsum = 0;

    private void bfs(TreeNode node) {
        /*
         * This is the official solution, where we keep track of the sum of
         * all the right nodes at the moment.
         */
        if (node == null)
            return;
        bfs(node.right);
        this.rsum += node.val;
        node.val = this.rsum;
        bfs(node.left);
    }

    public TreeNode bstToGst(TreeNode root) {
        bfs(root);
        return root;
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
