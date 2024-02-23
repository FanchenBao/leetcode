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


class Main{
    public static void main(String[] args) {
        String s = "acbbaca";
        String t = "aba";
        Solution sol = new Solution();
        System.out.println(sol.minWindow(s, t));
    }
}
