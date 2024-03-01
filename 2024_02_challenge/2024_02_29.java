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


class Solution {
    public boolean isEvenOddTree(TreeNode root) {
        /*
        LeetCode 1609
        
        BFS, O(N), 14 ms, faster than 43.75%
        */
        List<TreeNode> queue = new ArrayList<>();
        queue.add(root);
        int lvl = 0;
        boolean isInc = true;
        while (!queue.isEmpty()) {
            List<TreeNode> tmp = new ArrayList<>();
            for (int i = 0; i < queue.size(); i++) {
                TreeNode node = queue.get(i);
                boolean parityOk = ((node.val ^ lvl) & 1) == 1;
                boolean trendOk = i == 0 || (node.val > queue.get(i - 1).val && isInc) || (node.val < queue.get(i - 1).val && !isInc); 
                if (parityOk && trendOk) {
                    if (node.left != null)
                        tmp.add(node.left);
                    if (node.right != null)
                        tmp.add(node.right);
                } else {
                    return false;
                }
            }
            queue = tmp;
            lvl++;
            isInc = !isInc;
        }
        return true;
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
