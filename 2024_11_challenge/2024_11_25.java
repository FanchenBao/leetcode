import java.util.*;
import java.util.stream.Stream;

import java.math.*;
import javafx.util.Pair;

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
    // Constants
    int M = 2;
    int N = 3;
    int[][] dirs = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    private String getStateFromBoard(int[][] board) {
        StringBuilder state = new StringBuilder();
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++)
                state.append(board[i][j]);
        }
        return state.toString();
    }

    public int slidingPuzzle(int[][] board) {
        /*
         * LeetCode 773
         *
         * If this solution works, which I don't think why not, the problem
         * itself is not difficult. We just need to see the problem as a
         * BFS finding the shortest path. The difficult is to find a way to
         * represent the current state of the board, and then do the swaps
         * to generate the next state.
         *
         * O((M*N)!)
         */
        String state = getStateFromBoard(board);
        if (state.equals("123450"))
            return 0;
        Set<String> seen = new HashSet<>();
        seen.add(state);
        Deque<Pair<String, Integer>> queue = new ArrayDeque<>();
        queue.add(new Pair<>(state, 0));
        while (!queue.isEmpty()) {
            Pair<String, Integer> cur = queue.poll();
            String curState = cur.getKey();
            int steps = cur.getValue();
            // System.out.println(curState);
            if (curState.equals("123450"))
                return steps;
            int idx = curState.indexOf('0');
            int i = idx / this.N;
            int j = idx % this.N;
            // System.out.println(String.format("idx=%d, i=%d, j=%d", idx, i, j));
            for (int[] dir : this.dirs) {
                int ni = i + dir[0];
                int nj = j + dir[1];
                if (ni >= 0 && ni < this.M && nj >= 0 && nj < this.N) {
                    char[] nextStateArr = curState.toCharArray();
                    int k = ni * this.N + nj;
                    nextStateArr[idx] = nextStateArr[k];
                    nextStateArr[k] = '0';
                    String nextState = new String(nextStateArr);
                    // System.out.println(String.format("inner: %s", nextState));
                    if (!seen.contains(nextState)) {
                        seen.add(nextState);
                        queue.add(new Pair<>(nextState, steps + 1));
                    }
                }
            }
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
