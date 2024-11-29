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
    public int minimumObstacles(int[][] grid) {
        /*
         * LeetCode 2290
         *
         * Consider this a Dijkstra problem. The goal is to find the min cost
         * going from (0, 0) to (M - 1, N - 1). Each time we pass through an
         * obstacle, the cost increments by 1.
         *
         * O(MNlog(MN)), 154 ms, faster than 26.88%
         */
        int MAX = 1000000;
        int[][] dirs = new int[][]{{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
        PriorityQueue<int[]> queue = new PriorityQueue<>((a, b) -> Integer.compare(a[1], b[1])); // [1D pos, costs]
        int M = grid.length;
        int N = grid[0].length;
        int[] minCosts = new int[M * N];
        Arrays.fill(minCosts, MAX);
        queue.add(new int[]{0, 0});
        minCosts[0] = 0;
        while (!queue.isEmpty()) {
            int[] ele = queue.poll();
            if (minCosts[ele[0]] != ele[1])
                continue;
            if (ele[0] == M * N - 1) // early exit
                return ele[1];
            int i = ele[0] / N;
            int j = ele[0] % N;
            for (int[] dir : dirs) {
                int ni = i + dir[0];
                int nj = j + dir[1];
                int nidx = ni * N + nj;
                if (ni >= 0 && ni < M && nj >= 0 && nj < N) {
                    int nCost = ele[1] + (grid[ni][nj] == 1 ? 1 : 0);
                    if (nCost < minCosts[nidx]) {
                        minCosts[nidx] = nCost;
                        queue.add(new int[]{nidx, nCost});
                    }
                }
            }
        }
        return minCosts[M * N - 1];
    }
}


class Solution2 {
    public int minimumObstacles(int[][] grid) {
        /*
         * This is from the official solution, which uses 0-1 BFS. It is
         * essentially Dijkstra, but since there are only two costs for any
         * edges, we can simplify the "priority queue" step by always putting
         * the 0 cost neightbor at the front of the queue and the 1 cost
         * neighbor at the end of the queue. This will guarantee that the
         * queue is always sorted without having to go through priority queue.
         *
         * O(MN), 54 ms, faster than 87.50%
         */
        int MAX = 1000000;
        int[][] dirs = new int[][]{{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
        Deque<int[]> queue = new ArrayDeque<>(); // [1D pos, costs]
        int M = grid.length;
        int N = grid[0].length;
        int[] minCosts = new int[M * N];
        Arrays.fill(minCosts, MAX);
        queue.add(new int[]{0, 0});
        minCosts[0] = 0;
        while (!queue.isEmpty()) {
            int[] ele = queue.poll();
            if (minCosts[ele[0]] != ele[1])
                continue;
            if (ele[0] == M * N - 1) // early exit
                return ele[1];
            int i = ele[0] / N;
            int j = ele[0] % N;
            for (int[] dir : dirs) {
                int ni = i + dir[0];
                int nj = j + dir[1];
                int nidx = ni * N + nj;
                if (ni >= 0 && ni < M && nj >= 0 && nj < N && ele[1] + grid[ni][nj] < minCosts[nidx]) {
                    minCosts[nidx] = ele[1] + grid[ni][nj];
                    if (grid[ni][nj] == 1)
                        queue.addLast(new int[]{nidx, minCosts[nidx]});
                    else
                        queue.addFirst(new int[]{nidx, minCosts[nidx]});
                }
            }
        }
        return minCosts[M * N - 1];
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
