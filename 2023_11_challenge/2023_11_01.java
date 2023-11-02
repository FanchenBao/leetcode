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
     Map<Integer, Integer> counter = new HashMap<>();

     private void dfs(TreeNode node) {
         if (node != null) {
             counter.put(node.val, counter.getOrDefault(node.val, 0) + 1);
             dfs(node.left);
             dfs(node.right);
         }
     }

    public int[] findMode(TreeNode root) {
        /*
        LeetCode 501
        
        Cannot figure out how to solve this problem without extra space.
        
        This solution uses extra space to count the number of nodes, which
        essentially does not use the binary search tree clue.
        
        O(N), 5 ms, faster than 53.57%
        */
        dfs(root);
        List<Integer> modes = new ArrayList<>();
        int maxCount = 0;
        for (Map.Entry<Integer, Integer> entry : counter.entrySet()) {
            if (entry.getValue() > maxCount) {
                maxCount = entry.getValue();
                modes.clear();
                modes.add(entry.getKey());
            } else if (entry.getValue() == maxCount) {
                modes.add(entry.getKey());
            }
        }
        int[] res = new int[modes.size()]; for (int i = 0; i < modes.size(); i++) res[i] = modes.get(i);
        return res;
    }
}


class Solution {
     List<Integer> modes = new ArrayList<>();
     int maxCount = 0;
     int curCount = 0;
     int pre = Integer.MIN_VALUE;

     private void dfs(TreeNode node) {
         if (node != null) {
             dfs(node.left);
             if (node.val != pre) {
                 if (curCount > maxCount) {
                     maxCount = curCount;
                     modes.clear();
                     modes.add(pre);
                 } else if (curCount == maxCount) {
                     modes.add(pre);
                 }
                 pre = node.val;
                 curCount = 0;
             }
             curCount++;
             dfs(node.right);
         }
     }

    public int[] findMode(TreeNode root) {
        /*
        I cannot believe I forgot about one of the most important
        characteristics of binary search tree: inorder traversal =>
        sorted values.
        
        We can keep counting the number of repeats in a sorted fashion
        when performing inorder traversal. In this case, we do not need
        any extra space except for the space needed to record the
        current modes.
        
        O(N), 0 ms, faster than 100.00%
        */
        dfs(root);
        if (curCount > maxCount) return new int[]{pre};
        else if (curCount == maxCount) modes.add(pre);
        int[] res = new int[modes.size()];
        for (int i = 0; i < modes.size(); i++) res[i] = modes.get(i);
        return res;
    }
}