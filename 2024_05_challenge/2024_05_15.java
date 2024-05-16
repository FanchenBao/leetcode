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
    private boolean existPath(int lowLim, int N, int[][] dir, int[][] minDists) {
        if (minDists[0][0] < lowLim || minDists[N - 1][N - 1] < lowLim)
            return false;
        if (N == 1) // edge case
            return true;
        boolean[][] seen = new boolean[N][N];
        Deque<int[]> queue = new ArrayDeque<>();
        queue.addLast(new int[]{0, 0});
        seen[0][0] = true;
        while (!queue.isEmpty()) {
            int[] cur = queue.removeFirst();
            for (int[] dd : dir) {
                int ni = dd[0] + cur[0];
                int nj = dd[1] + cur[1];
                if (ni == N - 1 && nj == N - 1)
                    return true;
                if (ni >= 0 && ni < N && nj >= 0 && nj < N && minDists[ni][nj] >= lowLim && !seen[ni][nj]) {
                    queue.addLast(new int[]{ni, nj});
                    seen[ni][nj] = true;
                }
            }
        }
        return false;
    }

    public int maximumSafenessFactor(List<List<Integer>> grid) {
        /*
         * LeetCode 2812
         *
         * First use BFS to compute the min manhanttan distance from any cell
         * to all the thieves.
         *
         * Then use binary search to find the max min safeness factor of any
         * path from (0, 0) to (N - 1, N - 1)
         *
         * O(N^2log(N)) 166 ms, faster than 44.26%
         */
        int N = grid.size();
        int MAX = 800;
        int[][] minDists = new int[N][N];
        for (int[] row : minDists)
            Arrays.fill(row, MAX);
        int[][] dir = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        // Fill the min manhantan distance from any cell towards a thief
        Deque<int[]> queue = new ArrayDeque<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (grid.get(i).get(j) == 1) {
                    queue.addLast(new int[]{i, j, 0});
                    minDists[i][j] = 0;
                }
            }
        }
        while (!queue.isEmpty()) {
            int[] cur = queue.removeFirst();
            if (minDists[cur[0]][cur[1]] < cur[2])
                continue;
            for (int[] dd : dir) {
                int ni = dd[0] + cur[0];
                int nj = dd[1] + cur[1];
                if (ni >= 0 && ni < N && nj >= 0 && nj < N && cur[2] + 1 < minDists[ni][nj]) {
                    minDists[ni][nj] = cur[2] + 1;
                    queue.addLast(new int[]{ni, nj, cur[2] + 1});
                }
            }
        }
        // Binary search to find the path with the max min manhantan dist
        int lo = 0;
        int hi = MAX;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            boolean ver = existPath(mid, N, dir, minDists);
            if (ver)
                lo = mid + 1;
            else
                hi = mid;
        }
        return lo - 1;
    }
}


class Solution2 {
    public int maximumSafenessFactor(List<List<Integer>> grid) {
        /*
         * Use Dijkstra 
         *
         * 131 ms, faster than 61.89%
         */
        int N = grid.size();
        int MAX = 800;
        int[][] minDists = new int[N][N];
        for (int[] row : minDists)
            Arrays.fill(row, MAX);
        int[][] dir = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        // Fill the min manhantan distance from any cell towards a thief
        Deque<int[]> queue = new ArrayDeque<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (grid.get(i).get(j) == 1) {
                    queue.addLast(new int[]{i, j, 0});
                    minDists[i][j] = 0;
                }
            }
        }
        while (!queue.isEmpty()) {
            int[] cur = queue.removeFirst();
            if (minDists[cur[0]][cur[1]] < cur[2])
                continue;
            for (int[] dd : dir) {
                int ni = dd[0] + cur[0];
                int nj = dd[1] + cur[1];
                if (ni >= 0 && ni < N && nj >= 0 && nj < N && cur[2] + 1 < minDists[ni][nj]) {
                    minDists[ni][nj] = cur[2] + 1;
                    queue.addLast(new int[]{ni, nj, cur[2] + 1});
                }
            }
        }
        // Dijkstra to find the path with max min manhattan
        int[][] safeness = new int[N][N];
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(-a[0], -b[0]));
        pq.add(new int[]{minDists[0][0], 0, 0});
        safeness[0][0] = minDists[0][0];
        while (!pq.isEmpty()) {
            int[] cur = pq.remove();
            if (cur[0] != safeness[cur[1]][cur[2]])
                continue;
            if (cur[1] == N - 1 && cur[2] == N - 1)
                return cur[0];
            for (int[] dd : dir) {
                int ni = dd[0] + cur[1];
                int nj = dd[1] + cur[2];
                if (ni >= 0 && ni < N && nj >= 0 && nj < N) {
                    int nextSafe = Math.min(cur[0], minDists[ni][nj]);
                    if (nextSafe > safeness[ni][nj]) {
                        safeness[ni][nj] = nextSafe;
                        pq.add(new int[]{nextSafe, ni, nj});
                    }
                }
            }
        }
        return 0;
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
