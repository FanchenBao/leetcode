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
    private List<Integer> getLevelSum(TreeNode root) {
        List<Integer> levelSum = new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            int s = 0;
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                s += node.val;
                if (node.left != null)
                    queue.add(node.left);
                if (node.right != null)
                    queue.add(node.right);
            }
            levelSum.add(s);
        }
        return levelSum;
    }

    private void helper(TreeNode node, int lvl, List<Integer> levelSum) {
        if (lvl + 1 == levelSum.size())
            return;
        int oriLeftVal = node.left == null ? 0 : node.left.val;
        int oriRightVal = node.right == null ? 0 : node.right.val;
        if (node.left != null) {
            node.left.val = levelSum.get(lvl + 1) - oriLeftVal - oriRightVal;
            helper(node.left, lvl + 1, levelSum);
        }
        if (node.right != null) {
            node.right.val = levelSum.get(lvl + 1) - oriLeftVal - oriRightVal;
            helper(node.right, lvl + 1, levelSum);
        }
    }

    public TreeNode replaceValueInTree(TreeNode root) {
        /*
         * LeetCode 2641
         *
         * Produce level sum and then DFS to update the original tree.
         *
         * O(N), 25 ms, faster than 57.20%
         */
        List<Integer> levelSum = getLevelSum(root);
        root.val = 0;
        helper(root, 0, levelSum);
        return root; 
    }
}


class Solution2 {
    public TreeNode replaceValueInTree(TreeNode root) {
        /*
         * This solution is inspired by the official solution where there is
         * only one pass BFS.
         *
         * As we go through the current level, we compute the total sum of
         * the next level. Then as we go through the next level, we can use
         * the previously stored level sum to compute the cousin sum.
         *
         * The one trick is that as we go through the current level, we add
         * the sibling value to the current node's children. This way, when
         * we go through the next level, we only need to do level sum minus
         * the node value to obtain the cousin sum.
         *
         * O(N), 14 ms, faster than 96.61% 
         */
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        int curLvlSum = root.val;
        int nexLvlSum = 0;
        while (!queue.isEmpty()) {
            nexLvlSum = 0;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                node.val = curLvlSum - node.val;
                int leftVal = node.left == null ? 0 : node.left.val;
                int rightVal = node.right == null ? 0 : node.right.val;
                nexLvlSum += leftVal + rightVal;
                if (node.left != null) {
                    node.left.val = leftVal + rightVal; // this is the trick
                    queue.add(node.left);
                }
                if (node.right != null) {
                    node.right.val = leftVal + rightVal; // this is the trick
                    queue.add(node.right);
                }
            }
            curLvlSum = nexLvlSum;
        }
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
