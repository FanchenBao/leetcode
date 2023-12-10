class Solution {
    List<Integer> res = new ArrayList<>();
    
    private void helper(TreeNode root) {
        if (root == null)
            return;
        helper(root.left);
        res.add(root.val);
        helper(root.right);
    }
    
    public List<Integer> inorderTraversal(TreeNode root) {
        /*
        LeetCode 94
        */
        helper(root);
        return res;
    }
}
