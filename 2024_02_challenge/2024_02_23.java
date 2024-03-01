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
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        int MAX = 300000000;
        Map<Integer, List<int[]>> graph = new HashMap<>(); // the inner array is [dest, price]
        for (int[] f : flights) {
            graph.putIfAbsent(f[0], new ArrayList<>());
            graph.get(f[0]).add(new int[]{f[1], f[2]});
        }

        // prices[i][j] = lowest price to reach node i with it being the jth stop
        int[][] prices = new int[n][k + 1];
        for (int[] row : prices)
            Arrays.fill(row, MAX);

        List<int[]> queue = new ArrayList<>(); // each element [node, current price]
        queue.add(new int[]{src, 0});
        int numStops = 0;

        // BFS
        while (!queue.isEmpty() && numStops <= k) {
            List<int[]> tmp = new ArrayList<>();
            for (int[] ele : queue) {
                int node = ele[0];
                int currPrice = ele[1];
                prices[node][numStops] = Math.min(prices[node][numStops], currPrice);
                for (int[] childEle : graph.getOrDefault(node, Collections.emptyList())) {
                    int child = childEle[0];
                    int edgeCost = childEle[1];
                    tmp.add(new int[]{child, currPrice + edgeCost});
                }
            }
            numStops++;
            queue = tmp;
        }
        int res = MAX;
        for (int p : prices[dst])
            res = Math.min(res, p);
        return res == MAX ? -1 : res;
    }
}


class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        /*
         * Dijkstra.
         *
         * The key for Dijkstra is to realize that we do NOT keep track of the
         * price, because keeping to the lowest price is not the priority.
         * The priority is to arrive at the destination with at most k steps.
         * This means any time we go beyond k steps, we have to abandon the
         * current path and try something else.
         * With Dijkstra and without keeping track of the lowest price, we are
         * able to say that each node we visit has the smallest price within
         * the restraint of stops.
         *
         * However, we MUST keep track of the number of stops to reach a node.
         * If a node has been reached before with the same or smaller number of
         * stops as now, there is no need to visit it again, because earlier visits
         * always indicate lower price, and if lower number of stops doesn't
         * work, why would larger number of stops work.
         *
         * Thus, we simply run Dijkstra with k stops limit until the dst is
         * reached.
         * O(MlogN), where M is the number of edges and N is the number of nodes.
         */
        Map<Integer, List<int[]>> graph = new HashMap<>(); // the inner array is [dest, price]
        for (int[] f : flights) {
            graph.putIfAbsent(f[0], new ArrayList<>());
            graph.get(f[0]).add(new int[]{f[1], f[2]});
        }
        PriorityQueue<int[]> queue = new PriorityQueue<>(10, (a, b) -> Integer.compare(a[1], b[1]));  // each element of queue is [node, price, stops]
        int[] minStops = new int[n];
        Arrays.fill(minStops, n + 1);
        queue.add(new int[]{src, 0, 0});
        while (!queue.isEmpty()) {
            int[] ele = queue.poll();
            int node = ele[0];
            int price = ele[1];
            int stops = ele[2];
            if (node == dst)
                return price;
            if (stops >= k + 1 || stops >= minStops[node])
                continue;
            minStops[node] = stops;
            for (int[] childEle : graph.getOrDefault(node, Collections.emptyList())) {
                int child = childEle[0];
                int edgeCost = childEle[1];
                queue.add(new int[]{child, price + edgeCost, stops + 1});
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
