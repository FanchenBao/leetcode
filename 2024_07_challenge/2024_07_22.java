import java.util.*;
import java.util.stream.Stream;

import java.math.*;

/**
 * Definition for a binary tree node.
 */
//class TreeNode {
//    int val;
//    TreeNode left;
//    TreeNode right;
//    TreeNode() {}
//    TreeNode(int val) { this.val = val; }
//    TreeNode(int val, TreeNode left, TreeNode right) {
//        this.val = val;
//        this.left = left;
//        this.right = right;
//    }
//}

class Solution1 {
    public String[] sortPeople(String[] names, int[] heights) {
        /*
         * LeetCode 2418
         *
         * It took a while to figure out how to get custom sort working in
         * java.
         *
         * O(NlogN), 11 ms, faster than 42.70%
         */
        List<Integer> indices = new ArrayList<>();
        for (int i = 0; i < names.length; i++)
            indices.add(i);
        indices.sort(Comparator.comparingInt(a -> -heights[a]));
        String[] res = new String[names.length];
        int j = 0;
        for (int i : indices)
            res[j++] = names[i];
        return res;
    }
}


class Solution2 {
    public String[] sortPeople(String[] names, int[] heights) {
        /*
         * A new idea to avoid using ArrayList
         *
         * 9 ms, faster than 53.75%
         */
        int[][] his = new int[heights.length][2];
        for (int i = 0; i < heights.length; i++)
            his[i] = new int[]{heights[i], i};
        Arrays.sort(his, (a, b) -> b[0] - a[0]);
        String[] res = new String[names.length];
        int i = 0;
        for (int[] h : his)
            res[i++] = names[h[1]];
        return res;
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
