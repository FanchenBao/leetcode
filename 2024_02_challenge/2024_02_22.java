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
    public int findJudge(int n, int[][] trust) {
        /*
        LeetCode 997
        
        Count the indegree and outdegree of each node.
        
        O(N)
        */
        int[][] edgeCount = new int[n + 1][2]; // [indegree, outdegree]
        for (int[] rel : trust) {
            edgeCount[rel[1]][0] += 1;
            edgeCount[rel[0]][1] += 1;
        }
        for (int i = 1; i <= n; i++) {
            if (edgeCount[i][0] == n - 1 && edgeCount[i][1] == 0)
                return i;
        }
        return -1;
    }
}


class Solution {
    public int findJudge(int n, int[][] trust) {
        /*
         * Same idea as above BUT we only need to use a 1D array. We record
         * the indegrees, and each time a node has an outdegree, we decrement
         * its indegree. Thus, we only need to check for indegree equal to
         * n - 1 to find the town judge.
         *
         * 2 ms, faster than 99.85%
         */
        int[] indegrees = new int[n + 1];
        for (int[] rel : trust) {
            indegrees[rel[1]] += 1;
            indegrees[rel[0]] -= 1;
        }
        for (int i = 1; i <= n; i++) {
            if (indegrees[i] == n - 1)
                return i;
        }
        return -1;
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
