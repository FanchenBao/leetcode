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
    public int compareVersion(String version1, String version2) {
        /*
         * LeetCode 165
         *
         * Split the version and compare each position.
         * 1 ms, faster than 78.87%
         */
        int[] v1 = new int[500];
        int[] v2 = new int[500];
        String[] v1Strs = version1.split("\\.");
        String[] v2Strs = version2.split("\\.");
        for (int i = 0; i < v1Strs.length; i++)
            v1[i] = Integer.parseInt(v1Strs[i]);
        for (int i = 0; i< v2Strs.length; i++)
            v2[i] = Integer.parseInt(v2Strs[i]);
        for (int i = 0; i < 500; i++) {
            if (v1[i] < v2[i])
                return -1;
            if (v1[i] > v2[i])
                return 1;
        }
        return 0;
    }
}


class Solution2 {
    public int compareVersion(String version1, String version2) {
        /*
         * Let's use ArrayList and see what happens
         *
         * 2 ms, faster than 11.59%
         */
        Deque<Integer> v1 = new ArrayDeque<>();
        Deque<Integer> v2 = new ArrayDeque<>();
        for (String v : version1.split("\\."))
            v1.add(Integer.parseInt(v));
        for (String v : version2.split("\\."))
            v2.add(Integer.parseInt(v));
        while(!v1.isEmpty() && !v2.isEmpty()) {
            int v1Val = v1.removeFirst();
            int v2Val = v2.removeFirst();
            if (v1Val < v2Val)
                return -1;
            if (v1Val > v2Val)
                return 1;
        }
        while (!v1.isEmpty() && v1.peek() == 0)
            v1.removeFirst();
        while (!v2.isEmpty() && v2.peek() == 0)
            v2.removeFirst();
        if (v1.isEmpty() && v2.isEmpty())
            return 0;
        else if (v1.isEmpty())
            return -1;
        else
            return 1;
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
