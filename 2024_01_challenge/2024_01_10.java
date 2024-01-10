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

    Stack<TreeNode> path = new Stack<>();
    int tgt;

    int bfs(TreeNode node) {
        if (node == null)
            return 0;
        Deque<TreeNode> queue = new ArrayDeque<>();
        queue.add(node);
        int lvl = -1;
        while (!queue.isEmpty()) {
            int N = queue.size();
            for (int i = 0; i < N; i++) {
                TreeNode cur = queue.poll();
                if (cur != null && cur.left != null)
                    queue.add(cur.left);
                if (cur != null && cur.right != null)
                    queue.add(cur.right);
            }
            lvl++;
        }
        return lvl;
    }

    boolean dfs(TreeNode node) {
        // This function finds the path that goes from root to the starting point
        if (node == null)
            return false;
        this.path.push(node);
        if (node.val == this.tgt || dfs(node.left) || dfs(node.right))
            return true;
        this.path.pop();
        return false;
    }

    public int amountOfTime(TreeNode root, int start) {
        /*
        LeetCode 2385
        
        Find the path that leads to the start node, reverse the
        edges for each node on the path, and then perform two
        BFS to find the height, one starting at the start node and
        the other starting at the last node that leads to the start node.
        
        The answer is the bigger of the two heights.
        
        O(N), 37 ms, faster than 79.07%
        */
        this.tgt = start;
        dfs(root);
        TreeNode startNode = this.path.pop();
        TreeNode secondNode = this.path.isEmpty() ? null : this.path.peek();
        TreeNode next = startNode;
        while (!this.path.isEmpty()) {
            TreeNode cur = this.path.pop();
            if (cur.left == next) {
                if (!this.path.isEmpty())
                    cur.left = this.path.peek();
                else 
                    cur.left = null;
            } else {
                if (!this.path.isEmpty())
                    cur.right = this.path.peek();
                else 
                    cur.right = null;
            }
            next = cur;
        }
        return Math.max(bfs(startNode), secondNode == null ? 0 : 1 + bfs(secondNode));
    }
}

