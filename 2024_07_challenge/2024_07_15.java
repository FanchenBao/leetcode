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
    public TreeNode createBinaryTree(int[][] descriptions) {
        /*
         * LeetCode 2196
         *
         * Construct the tree with the help of a hash map which maps the value
         * of the tree node to the actual TreeNode. We use another hash map
         * to keep track of the root value
         * 
         * O(N), 67 ms, faster than 59.60%
         */
        Map<Integer, TreeNode> nodeMap = new HashMap<>();
        Map<Integer, Boolean> isChild = new HashMap<>();
        for (int[] d : descriptions) {
            nodeMap.putIfAbsent(d[0], new TreeNode(d[0]));
            nodeMap.putIfAbsent(d[1], new TreeNode(d[1]));
            if (d[2] == 1)
                nodeMap.get(d[0]).left = nodeMap.get(d[1]);
            else
                nodeMap.get(d[0]).right = nodeMap.get(d[1]);
            isChild.put(d[1], true);
        }
        for (int[] d : descriptions) {
            if (!isChild.getOrDefault(d[0], false))
                return nodeMap.get(d[0]);
        }
        return null;
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
