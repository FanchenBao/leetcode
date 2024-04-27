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

// class Solution {
//     int[][] memo;
//     int M;
//     int N;
//     int MAX = 1000000000;
//     String ring;
//     String key;
//
//     private int dp(int i, int j) {
//         if (j == N)
//             return -1; // need to undo the unnecessary extra ring rotation
//         if (memo[i][j] > 0)
//             return memo[i][j];
//         memo[i][j] = MAX;
//         if (ring.charAt(i) == key.charAt(j)) {
//             int moveR = 1 + dp((i + 1) % M, j + 1); 
//             int moveL = 1 + dp((i - 1 + M) % M, j + 1);
//             int stay = dp(i, j + 1);
//             memo[i][j] = 1 + Math.min(memo[i][j], Math.min(Math.min(moveR, moveL), stay));
//         }
//         memo[i][j] = Math.min(memo[i][j], 1 + Math.min(dp((i + 1) % M, j), dp((i - 1 + M) % M, j)));
//         return memo[i][j];
//     }
//
//     public int findRotateSteps(String ring, String key) {
//         /*
//          * LeetCode 514
//          *
//          * dp(i, j) is the min steps to fulfill key[j:] when the current
//          * position in ring is at index i.
//          *
//          * We can always move one step clockwise or counter-clockwise without
//          * considering the current letter.
//          *
//          * If ring[i] == key[j], then there is another possibility of recognizing
//          * the current letter and then move forward.
//          *
//          * Notice that when j goes out of bound, we need to return minus one
//          * to undo the unnecessary last rotation.
//          *
//          * O(M^2N)
//          */
//         M = ring.length();
//         N = key.length();
//         memo = new int[M][N];
//         this.ring = ring;
//         this.key = key;
//         return dp(0, 0);
//     }
// }
//


class Solution {
    public int findRotateSteps(String ring, String key) {
        /*
        * BFS with DP.
        *
        * DP[i][j + 1] is the min step to reach ring[i] with the attempt to match
        * key[j], starting from right to left on the key.
        *
        * Notice that we handle the logic of when to append a new node to the queue
        * not in the main body of BFS, but in the condition. This is to avoid
        * unnecessary addition of nodes whose have been added before but not visited.
        *
        * 32 ms, faster than 39.81%
        */
        int M = ring.length();
        int N = key.length();
        int[][] dp = new int[M][N + 1];
        for (int[] row : dp)
            Arrays.fill(row, 1000000000);
        Deque<int[]> queue = new ArrayDeque<>();
        for (int i = 0; i < M; i++) {
            if (ring.charAt(i) == key.charAt(N - 1)) {
                queue.add(new int[]{i, N - 1, 0});
                dp[i][N] = 0;
            }
        }
        while (!queue.isEmpty()) {
            int[] tup = queue.removeFirst();
            int i = tup[0];
            int j = tup[1];
            int step = tup[2];
            int r = (i + 1) % M;
            int l = (i - 1 + M) % M;
            if (j >= 0 && ring.charAt(i) == key.charAt(j)) {
                if (j >= 0 && step + 1 < dp[r][j]) { // for dp, the next j is j - 1 + 1
                    dp[r][j] = step + 1;
                    queue.addLast(new int[]{r, j - 1, step + 1});
                }
                if (j >= 0 && step + 1 < dp[l][j]) {
                    dp[l][j] = step + 1;
                    queue.addLast(new int[]{l, j - 1, step + 1});
                }
                if (j >= 0 && step < dp[i][j]) {
                    dp[i][j] = step;
                    queue.addLast(new int[]{i, j - 1, step});
                }
            } else {
                if (step + 1 < dp[r][j + 1]) {
                    dp[r][j + 1] = step + 1;
                    queue.addLast(new int[]{r, j, step + 1});
                }
                if (step + 1 < dp[l][j + 1]) {
                    dp[l][j + 1] = step + 1;
                    queue.addLast(new int[]{l, j, step + 1});
                }
            }
        }
        return dp[0][0] + N;
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
