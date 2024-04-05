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


class Solution2 {
    String word;
    char[][] board;

    private boolean dp(int i, int j, int idx) {
        if (board[i][j] == word.charAt(idx)) {
            if (idx == word.length() - 1) {
                return true;
            } else {
                board[i][j] = '.';
                for (int[] nextPos : new int[][]{{i - 1, j}, {i + 1, j}, {i, j - 1}, {i, j + 1}}) {
                    if (nextPos[0] >= 0 && nextPos[0] < board.length && nextPos[1] >= 0 && nextPos[1] < board[0].length && board[nextPos[0]][nextPos[1]] != '.') {
                        if (dp(nextPos[0], nextPos[1], idx + 1))
                            return true;
                    }
                } 
                seen[i][j] = word.charAt(idx);
            }
        } 
        return false;
    }

    public boolean exist(char[][] board, String word) {
        /*
        * Same solution as Solution1, but we do not create a separate array
        * to verify whether a cell has been visited. We make the note in-place
        * inside the board.
        *
        * Turns out it is not any faster than Solution1
        * 244 ms, faster than 16.52%
        */
        this.word = word;
        this.board = board;

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (dp(i, j, 0))
                    return true;
            }
        }
        return false;
    }
}


class Solution3 {
    String word;
    char[][] board;

    private boolean dp(int i, int j, int idx) {
        if (board[i][j] == word.charAt(idx)) {
            if (idx == word.length() - 1) {
                return true;
            } else {
                board[i][j] = '.';
                for (int[] nextPos : new int[][]{{i - 1, j}, {i + 1, j}, {i, j - 1}, {i, j + 1}}) {
                    if (nextPos[0] >= 0 && nextPos[0] < board.length && nextPos[1] >= 0 && nextPos[1] < board[0].length && board[nextPos[0]][nextPos[1]] != '.') {
                        if (dp(nextPos[0], nextPos[1], idx + 1))
                            return true;
                    }
                } 
                board[i][j] = word.charAt(idx);
            }
        } 
        return false;
    }

    private boolean precheck() {
        int[] bc = new int[256];
        int[] wc = new int[256];
        for (char[] row : board) {
            for (char c : row)
                bc[c]++;
        }
        for (char c : word.toCharArray())
            bc[c]++;
        for (int i = 0; i < 256; i++) {
            if (wc[i] > bc[i])
                return false;
        }
        return true;
    }

    public boolean exist(char[][] board, String word) {
        /*
        * Same as solution2, but we add a pre-check before starting backtracking
        * 
        * But this is not any faster: 252 ms, faster than 15.97%
        */
        this.word = word;
        this.board = board;
        
        if (!precheck())
            return false;

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
