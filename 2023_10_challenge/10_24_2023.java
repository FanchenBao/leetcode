/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> largestValues(TreeNode root) {
        /*
        LeetCode 515
        
        BFS. Don't forget to check a null root.
        
        O(N), 2 ms, faster than 82.84%
        */
        List<Integer> res = new ArrayList<>();
        if (root == null) return res;
        List<TreeNode> queue = new ArrayList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            List<TreeNode> tmp = new ArrayList<>();
            int max = Integer.MIN_VALUE;
            for (TreeNode node : queue) {
                max = Math.max(max, node.val);
                if (node.left != null) tmp.add(node.left);
                if (node.right != null) tmp.add(node.right);
            }
            res.add(max);
            queue = tmp;
        }
        return res;
    }
}


class Solution {
    List<Integer> res = new ArrayList<>();
    
    private void dfs(TreeNode node, int lvl) {
        if (node == null) return;
        if (res.size() == lvl) res.add(node.val);
        else res.set(lvl, Math.max(res.get(lvl), node.val));
        dfs(node.left, lvl + 1);
        dfs(node.right, lvl + 1);
    }
    
    public List<Integer> largestValues(TreeNode root) {
        /*
        DFS
        
        O(N), 1 ms, faster than 98.83%
        */
        dfs(root, 0);
        return res;
    }
}
