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

class Solution {
    String word;
    char[][] board;
    boolean[][] seen;

    private boolean dp(int i, int j, int idx) {
        if (board[i][j] == word.charAt(idx)) {
            if (idx == word.length() - 1) {
                return true;
            } else {
                seen[i][j] = true;
                for (int[] nextPos : new int[][]{{i - 1, j}, {i + 1, j}, {i, j - 1}, {i, j + 1}}) {
                    if (nextPos[0] >= 0 && nextPos[0] < board.length && nextPos[1] >= 0 && nextPos[1] < board[0].length && !seen[nextPos[0]][nextPos[1]]) {
                        if (dp(nextPos[0], nextPos[1], idx + 1))
                            return true;
                    }
                } 
                seen[i][j] = false;
            }
        } 
        return false;
    }

    public boolean exist(char[][] board, String word) {
        /*
        * LeetCode 79
        
        Backtracking, no optimization. 242 ms, faster than 16.73%
        */
        this.word = word;
        this.board = board;
        this.seen = new boolean[board.length][board[0].length];

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (dp(i, j, 0))
                    return true;
            }
        }
        return false;
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
