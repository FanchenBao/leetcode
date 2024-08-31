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
    int MAX = 2000000000;
    
    private int dijkstra(int[][] graph, int src, int des) {
        // We return the min dist from src to des
        int N = graph.length;
        PriorityQueue<int[]> queue = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        int[] dists = new int[N];
        Arrays.fill(dists, Integer.MAX_VALUE);
        dists[src] = 0;
        queue.add(new int[]{0, src});
        while (!queue.isEmpty()) {
            int[] tmp = queue.poll();
            int curDist = tmp[0];
            int curNode = tmp[1];
            if (curDist != dists[curNode])
                continue;
            if (curNode == des)
                break;
            for (int child = 0; child < N; child++) {
                int newDist = curDist + graph[curNode][child];
                if (graph[curNode][child] > 0 && dists[child] > newDist) {
                    dists[child] = newDist;
                    queue.add(new int[]{newDist, child});
                }
            }
        }
        return dists[des];
    }

    public int[][] modifiedGraphEdges(int n, int[][] edges, int source, int destination, int target) {
        /*
         * LeetCode 2699 (Fail)
         *
         * Although I still failed to solve this problem, I was close. We use
         * Dijkstra to first find the min dist without any modifiable edges.
         * If that min dist is already smaller than target, there is no way
         * to modify the edges to reach target.
         *
         * Otherwise, we modify the edges one by one (this is where I failed
         * to realize). If, by modifying the edge to 1, the min dist is still
         * larger than target, we leave it as is and move on to the next edge.
         * Otherwise, we can adjust the edge to force the min dist to equal
         * target, and the rest of the modifiable edges can be assigned the
         * MAX value.
         *
         * O(E(E + V)logV), where (E + V)logV is the time complexity of Dijkstra
         *
         * 124 ms, faster than 78.89%
         */
        int[][] graph = new int[n][n];
        for (int[] edge : edges) {
            graph[edge[0]][edge[1]] = edge[2];
            graph[edge[1]][edge[0]] = edge[2];
        }
        // not possible because the original edges already produces a min dist
        // shorter than target.
        int oriMinDist = dijkstra(graph, source, destination);
        if (oriMinDist < target)
            return new int[0][];
        // Set each negative edge to 1 and check min dist. If min dist is still
        // larger than target, move on to the next edge. Otherwise, adjust the
        // edge weight to match target. The rest of the modifiable edges can
        // be set to MAX
        boolean success = oriMinDist == target;
        for (int[] edge : edges) {
            if (edge[2] < 0) {
                if (!success) {
                    graph[edge[0]][edge[1]] = 1;
                    graph[edge[1]][edge[0]] = 1;
                    int curMinDist = dijkstra(graph, source, destination);
                    if (curMinDist <= target) {
                        graph[edge[0]][edge[1]] += target - curMinDist;
                        graph[edge[1]][edge[0]] += target - curMinDist;
                        success = true;
                    }
                } else {
                    graph[edge[0]][edge[1]] = this.MAX;
                    graph[edge[1]][edge[0]] = this.MAX;
                }
            }
        }
        if (!success)
            return new int[0][];
        int[][] res = new int[edges.length][3];
        for (int i = 0; i < edges.length; i++) {
            int[] edge = edges[i];
            res[i] = new int[]{edge[0], edge[1], graph[edge[0]][edge[1]]};
        }
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
