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
    List<TreeNode> res = new ArrayList<>();

    private void dfs(TreeNode node, TreeNode par, boolean isLeft, Set<Integer> toDelete) {
        if (node == null)
            return;
        if (toDelete.contains(node.val)) {
            if (par != null) {
                if (isLeft)
                    par.left = null;
                else
                    par.right = null;
            }
            dfs(node.left, null, true, toDelete);
            dfs(node.right, null, false, toDelete);
        } else {
            if (par == null)
                this.res.add(node);
            dfs(node.left, node, true, toDelete);
            dfs(node.right, node, false, toDelete);
        }
    }

    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        /*
         * LeetCode 1110
         *
         * DFS. Each time we process a node, we also take into consideration
         * its parent and whether it is a left or right node. We can make
         * deletion by setting its par.left or par.right to null. We can
         * determine whether the current node is a new root of a tree by
         * checking whether its parent is null.
         *
         * O(N), 1 ms, faster than 97.28% 
         */
        Set<Integer> toDelete = new HashSet<>();
        for (int d : to_delete)
            toDelete.add(d);
        dfs(root, null, true, toDelete);
        return this.res;
    }
}


class Solution2 {
    List<TreeNode> res = new ArrayList<>();

    private TreeNode dfs(TreeNode node, Set<Integer> toDelete) {
        if (node != null) {
            node.left = dfs(node.left, toDelete);
            node.right = dfs(node.right, toDelete);
            if (toDelete.contains(node.val)) {
                if (node.left != null)
                    this.res.add(node.left);
                if (node.right != null)
                    this.res.add(node.right);
                node = null;
            }
        }
        return node;
    }

    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        /*
         * This is from the official solution. It is a better implementation
         * of DFS. Instead of pre-order, we can do post-order. The benefit
         * of post-order is that when the current node is under consideration,
         * its children have already been handled. Thus, if the current node
         * needs to be deleted, and it has legitmitate children, the children
         * will definitely become new roots in the forest.
         *
         * 1 ms, faster than 97.28%
         */
        Set<Integer> toDelete = new HashSet<>();
        for (int d : to_delete)
            toDelete.add(d);
        if (dfs(root, toDelete) != null)
            this.res.add(root);
        return this.res;
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
