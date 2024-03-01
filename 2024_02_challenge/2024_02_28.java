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
    public int findBottomLeftValue(TreeNode root) {
        /*
        LeetCode 513
        
        BFS and record the first value of each level.
        
        O(N)
        */
        int res = 0;
        List<TreeNode> queue = new ArrayList<>();
        queue.add(root);
        while(!queue.isEmpty()) {
            List<TreeNode> tmp = new ArrayList<>();
            res = queue.get(i).val;
            for (int i = 0; i < queue.size(); i++) {
                TreeNode node = queue.get(i);
                if (node.left != null)
                    tmp.add(node.left);
                if (node.right != null)
                    tmp.add(node.right);
            }
            queue = tmp;
        }
        return res;
    }
}


class Solution {
    private int[] traverse(TreeNode node) {
        int[] left = new int[]{0, -2};
        int[] right = new int[]{0, -2};
        if (node.left != null)
            left = traverse(node.left);
        if (node.right != null)
            right = traverse(node.right);
        left[1]++; right[1]++;
        if (left[1] < 0 && right[1] < 0)
            return new int[]{node.val, 0};
        if (left[1] >= right[1])
            return left;
        return right;
    }

    public int findBottomLeftValue(TreeNode root) {
        /*
         * Let's try DFS
         
         1 ms, faster than 70.27% 
         */
        return traverse(root)[0];
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
