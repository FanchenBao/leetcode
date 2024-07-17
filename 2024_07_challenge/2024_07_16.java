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
    int[][] startPath;
    int[][] destPath;
    int startValue;
    int destValue;

    private void dfs(TreeNode node, List<int[]> path, boolean isLeft) {
        if (node == null)
            return;
        path.add(new int[]{node.val, isLeft ? 1 : 0});
        if (node.val == this.startValue) {
            this.startPath = new int[path.size()][2];
            for (int i = 0; i < path.size(); i++)
                startPath[i] = path.get(i);
        }
        if (node.val == this.destValue) {
            this.destPath = new int[path.size()][2];
            for (int i = 0; i < path.size(); i++)
                destPath[i] = path.get(i);
        }
        dfs(node.left, path, true);
        dfs(node.right, path, false);
        path.remove(path.size() - 1);
    }

    public String getDirections(TreeNode root, int startValue, int destValue) {
        /*
         * LeetCode 2096
         *
         * First of all, find the path from root to startValue and destValue,
         * recording also the passage of left or right branches.
         *
         * Then locate the lowest common ancestor of start and dest. We can
         * use their path to quickly identify it.
         *
         * Finally, go through the path from lca to start to identify the 'U's
         * and go through the path from lca to dest to identify the 'L's or
         * 'R's.
         *
         * O(N), 39 ms, faster than 25.34%
         */
        this.startValue = startValue;
        this.destValue = destValue;
        dfs(root, new ArrayList<>(), true);
        int lcaIdx = 0;
        while (lcaIdx < this.startPath.length && lcaIdx < this.destPath.length && this.startPath[lcaIdx] == this.destPath[lcaIdx])
            lcaIdx++;
        lcaIdx--;
        StringBuilder res = new StringBuilder();
        for (int i = lcaIdx; i < this.startPath.length - 1; i++)
            res.append('U');
        for (int i = lcaIdx + 1; i < this.destPath.length; i++)
            res.append(this.destPath[i][1] == 1 ? 'L' : 'R');
        return res.toString();
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
