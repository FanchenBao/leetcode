class Solution {
    public String tree2str(TreeNode root) {
        /*
        LeetCode 606

        Recursion. O(N), 15 ms, faster than 20.31%
         */
       if (root == null)
           return "";
       String l = tree2str(root.left);
       String r = tree2str(root.right);
       if (l.isEmpty() && r.isEmpty())
           return Integer.toString(root.val);
       return root.val + "(" + l + ")" + (r.isEmpty() ? "" : "(" + r + ")");
    }
}
