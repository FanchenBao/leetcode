import java.math.*;
import java.util.*;
import java.util.stream.Stream;

/**
 * Definition for a binary tree node.
 */
// class TreeNode {
// int val;
// TreeNode left;
// TreeNode right;
// TreeNode() {}
// TreeNode(int val) { this.val = val; }
// TreeNode(int val, TreeNode left, TreeNode right) {
// this.val = val;
// this.left = left;
// this.right = right;
// }
// }

class Solution {
    public int minimumTime(int[][] grid) {
        /*
         * LeetCode 2577
         *
         * First observation is that the only situation where it is not possible
         * to go from top left to bottom right is if the two adjacent cells of
         * top left both have time requirements bigger than 1. Otherwise, it
         * is always possible to reach bottom right, because we can go back and
         * forth to accumulate time.
         *
         * The rest of the algorithm is Dijkstra. We keep track of the min time
         * to reach each cell. If the next cell's time requirement is smaller
         * than its parent's min reach time, then its min reach time is its
         * parent's min reach time plus 1. Otherwise, we find the difference
         * between the current cell's time requirement and its parent cell's
         * min reach time. If the difference is odd, the current cell will be
         * reached at exactly its time requirement. Otherwise, it will be
         * reached at its time requirement plus one.
         *
         * O(MNlog(MN)), 147 ms, faster than 58.82%
         */
        int MAX = 1000000;
        if (grid[0][1] > 1 && grid[1][0] > 1)
            return -1;
        int M = grid.length;
        int N = grid[0].length;
        int[][] dirs = new int[][] { { 0, 1 }, { 1, 0 }, { -1, 0 }, { 0, -1 } };
        int[][] minTimes = new int[M][N];
        for (int[] row : minTimes)
            Arrays.fill(row, MAX);
        PriorityQueue<int[]> queue = new PriorityQueue<>(
                (a, b) -> Integer.compare(a[0], b[0])); // [time, i, j]
        queue.add(new int[] { 0, 0, 0 });
        minTimes[0][0] = 0;
        while (!queue.isEmpty()) {
            int[] ele = queue.poll();
            if (minTimes[ele[1]][ele[2]] != ele[0])
                continue;
            if (ele[1] == M - 1 && ele[2] == N - 1)
                break;
            for (int[] dir : dirs) {
                int ni = ele[1] + dir[0];
                int nj = ele[2] + dir[1];
                if (ni >= 0 && ni < M && nj >= 0 && nj < N) {
                    int nextTime;
                    if (grid[ni][nj] <= ele[0]) {
                        nextTime = ele[0] + 1;
                    } else {
                        nextTime = grid[ni][nj] + 1 - (grid[ni][nj] - ele[0]) % 2;
                    }
                    if (nextTime < minTimes[ni][nj]) {
                        minTimes[ni][nj] = nextTime;
                        queue.add(new int[] { nextTime, ni, nj });
                    }
                }
            }
        }
        return minTimes[M - 1][N - 1];
    }
}

class Main {
    public static void main(String[] args) {
        String s = "acbbaca";
        String t = "aba";
        Solution sol = new Solution();
        System.out.println(sol.minWindow(s, t));
    }
}
