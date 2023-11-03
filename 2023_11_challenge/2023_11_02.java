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
     int res = 0;
     
     private int[] dfs(TreeNode node) {
         if (node == null) return new int[]{0, 0};
         int[] ls = dfs(node.left); int[] rs = dfs(node.right);
         int total = node.val + ls[0] + rs[0];
         int cnt = 1 + ls[1] + rs[1];
         if (total / cnt == node.val) res++;
         return new int[]{total, cnt};
     }
     
    public int averageOfSubtree(TreeNode root) {
        /*
        LeetCode 2265
        
        Just DFS it. O(N) 0 ms, faster than 100.00% 
        */
        dfs(root);
        return res;
    }
}
