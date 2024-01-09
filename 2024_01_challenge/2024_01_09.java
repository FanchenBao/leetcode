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
    
    private void traverse(TreeNode node, List<Integer> leaves) {
        if (node != null) {
            traverse(node.left, leaves);
            if (node.left == null && node.right == null)
                leaves.add(node.val); // leaf
            traverse(node.right, leaves);
        }
    }
    
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        /*
        LeetCode 872
        
        Traverse the two trees to obtain their leaves.
        
        O(N + M), 0 ms, faster than 100.00%
        */
        List<Integer> leaves1 = new ArrayList<>();
        List<Integer> leaves2 = new ArrayList<>();
        traverse(root1, leaves1);
        traverse(root2, leaves2);
        return leaves1.equals(leaves2);
    }
}

