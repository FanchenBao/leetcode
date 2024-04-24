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
    Map<Integer, List<Integer>> graph = new HashMap<>();
    Map<Integer, List<int[]>> heights = new HashMap<>();
    Map<Integer, List<Integer>> maxHeightNodes = new HashMap<>();
    int minHeight = 1000000000;

    private int dfs1(int node, int parent) {
        // First pass DFS to get the heights from a given root
        int maxH = 0;
        heights.putIfAbsent(node, new ArrayList<>());
        for (int nex : graph.getOrDefault(node, Collections.emptyList())) {
            if (nex != parent) {
                int nexH = dfs1(nex, node) + 1;
                heights.get(node).add(new int[]{nexH, nex});
                maxH = Math.max(maxH, nexH);
            }
        }
        return maxH;
    }

    private void dfs2(int node, int parent) {
        if (parent >= 0) {
            int[] parentH = new int[]{1, parent};
            for (int[] heightVia : heights.getOrDefault(parent, Collections.emptyList())) {
                if (heightVia[1] != node) {
                    parentH[0] = Math.max(parentH[0], heightVia[0] + 1);
                    break;
                }
            }
            heights.get(node).add(parentH);    
        }
        heights.get(node).sort(Comparator.comparing(tup -> -tup[0]));
        int maxH = 0;
        if (!heights.get(node).isEmpty())
            maxH = heights.get(node).get(0)[0];
        maxHeightNodes.putIfAbsent(maxH, new ArrayList<>());
        maxHeightNodes.get(maxH).add(node);
        minHeight = Math.min(minHeight, maxH);
        for (int nex: graph.getOrDefault(node, Collections.emptyList())) {
            if (nex != parent)
                dfs2(nex, node);
        }
    }

    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        /*
         * LeetCode 310
         *
         * Two rounds of DFS. First round to get the height of each node when
         * taking 0 as the root.
         *
         * The second round adds one more max path for each node from the
         * parent. The only requirement is that the max path through the parent
         * does not go through the current node already.
         *
         * O(V + E), 78 ms, faster than 5.14%
         */
        for (int[] e : edges) {
            graph.putIfAbsent(e[0], new ArrayList<>());
            graph.putIfAbsent(e[1], new ArrayList<>());
            graph.get(e[0]).add(e[1]);
            graph.get(e[1]).add(e[0]);
        }
        dfs1(0, -1);
        dfs2(0, -1);
        return maxHeightNodes.get(minHeight);
    }
}


class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        /*
         * Smarter solution: topological sort.
         *
         * Prune the nodes with only one edge, until only one or two nodes
         * are left. They are the roots of the MHTs.
         *
         * O(V + E), 50 ms, faster than 13.47%
         */
        if (n <= 2) {
            List<Integer> res = new ArrayList<>();
            for (int i = 0; i < n; i++)
                res.add(i);
            return res;
        }
        Map<Integer, Set<Integer>> graph = new HashMap<>();
        for (int[] e : edges) {
            graph.putIfAbsent(e[0], new HashSet<>());
            graph.putIfAbsent(e[1], new HashSet<>());
            graph.get(e[0]).add(e[1]);
            graph.get(e[1]).add(e[0]);
        }
        List<Integer> queue = new ArrayList<>();
        for (int node : graph.keySet()) {
            if (graph.get(node).size() == 1)
                queue.add(node);
        }
        while (!queue.isEmpty()) {
            List<Integer> tmp = new ArrayList();
            for (int node : queue) {
                for (int neigh : graph.get(node)) {
                    graph.get(neigh).remove(node);
                    if (graph.get(neigh).size() == 1)
                        tmp.add(neigh);
                }
                n -= 1;
            }
            queue = tmp;
            if (queue.size() == 1 || (queue.size() == 2 && n == 2))
                break;
        }
        return queue;
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
