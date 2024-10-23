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
    public long kthLargestLevelSum(TreeNode root, int k) {
        /*
         * LeetCode 2583
         *
         * Use BFS
         *
         * O(N + NlogN), 38 ms, faster than 36.86% 
         */
        List<TreeNode> queue = new ArrayList<>();
        queue.add(root);
        List<Long> levelSums = new ArrayList<>();
        while (!queue.isEmpty()) {
            List<TreeNode> tmp = new ArrayList<>();
            long s = 0;
            for (TreeNode node : queue) {
                s += (long)node.val;
                if (node.left != null)
                    tmp.add(node.left);
                if (node.right != null)
                    tmp.add(node.right);
            }
            levelSums.add(s);
            queue = tmp;
        }
        if (k > levelSums.size())
            return -1;
        levelSums.sort((a, b) -> Long.compare(a, b));
        return levelSums.get(levelSums.size() - k); 
    }
}

class Solution2 {
    public long kthLargestLevelSum(TreeNode root, int k) {
        /*
         * Use priority queue to speed up the sorting
         * O(N + NlogK)
         */
        List<TreeNode> queue = new ArrayList<>();
        queue.add(root);
        PriorityQueue<Long> levelSums = new PriorityQueue<>((a, b) -> Long.compare(a, b));
        while (!queue.isEmpty()) {
            List<TreeNode> tmp = new ArrayList<>();
            long s = 0;
            for (TreeNode node : queue) {
                s += (long)node.val;
                if (node.left != null)
                    tmp.add(node.left);
                if (node.right != null)
                    tmp.add(node.right);
            }
            levelSums.add(s);
            if (levelSums.size() > k)
                levelSums.poll();
            queue = tmp;
        }
        if (k > levelSums.size())
            return -1;
        return levelSums.poll();
    }
}

class Solution {
    public long kthLargestLevelSum(TreeNode root, int k) {
        /*
         * No need to use a tmp queue. Use a queue directly and
         * simply iterate through the current level.
         *
         * 32 ms, faster than 65.40%
         */
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        PriorityQueue<Long> levelSums = new PriorityQueue<>((a, b) -> Long.compare(a, b));
        while (!queue.isEmpty()) {
            long s = 0;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                s += (long)node.val;
                if (node.left != null)
                    queue.add(node.left);
                if (node.right != null)
                    queue.add(node.right);
            }
            levelSums.add(s);
            if (levelSums.size() > k)
                levelSums.poll();
        }
        if (k > levelSums.size())
            return -1;
        return levelSums.poll();
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
