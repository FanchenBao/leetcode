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
    int[][] pathsum;
    Map<Integer, List<Integer>> graph = new HashMap<>();

    private void dfs1(int node, int parent) {
        int ps = 0;
        int np = 0;
        for (int child : graph.getOrDefault(node, Collections.emptyList())) {
            if (child == parent)
                continue;
            dfs1(child, node);
            ps += pathsum[child][1] + pathsum[child][0] + 1;
            np += pathsum[child][1] + 1;
        }
        pathsum[node][0] = ps;
        pathsum[node][1] = np;
    }

    private void dfs2(int node, int parent) {
        if (parent >= 0) {
            int npOfParentNotThruNode = pathsum[parent][1] - 1 - pathsum[node][1];
            int psOfParentNotThruNode = pathsum[parent][0] - 1 - pathsum[node][1] - pathsum[node][0];
            pathsum[node][1] += npOfParentNotThruNode + 1;
            pathsum[node][0] += psOfParentNotThruNode + npOfParentNotThruNode + 1;
        }
        for (int child : graph.getOrDefault(node, Collections.emptyList())) {
            if (child == parent)
                continue;
            dfs2(child, node);
        }
    }

    public int[] sumOfDistancesInTree(int n, int[][] edges) {
        /*
         * LeetCode 834
         *
         * Two rounds of DFS. The first round computes the path sum and the
         * number of paths starting from each node as root of its subtree. It
         * does not matter which node is set as the root of the whole tree.
         * Thus, we use 0 as the root.
         *
         * Then we do DFS for the second time. For each node, we look into
         * the parent to find the number of paths and path sum that starts
         * from the parent but do not go through the current node. Using that
         * info, we can find the total path sum and number of paths starting
         * at the current node as the root.
         *
         * O(E + V), 67 ms, faster than 37.07%
         */
        for (int [] tup : edges) {
            int a = tup[0];
            int b = tup[1];
            graph.putIfAbsent(a, new ArrayList<>());
            graph.putIfAbsent(b, new ArrayList<>());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }
        pathsum = new int[n][2]; // pathsum[i] = [total path sum with i as root, total number of paths with i as root]
        dfs1(0, -1);
        dfs2(0, -1);
        int[] res = new int[n];
        for (int i = 0; i < n; i++)
            res[i] = pathsum[i][0];
        return res;
    }
}


class Solution2 {
    int[] subtreeSize;
    int[] pathSums;
    Map<Integer, List<Integer>> graph = new HashMap<>();
    int N;

    private void dfs1(int node, int parent) {
        for (int child : graph.getOrDefault(node, Collections.emptyList())) {
            if (child == parent)
                continue;
            dfs1(child, node);
            subtreeSize[node] += subtreeSize[child];
            pathSums[node] += subtreeSize[child] + pathSums[child];
        }
    }

    private void dfs2(int node, int parent) {
        if (parent >= 0) {
            // pathSums[parent] - subtreeSize[node] removes the paths from
            // parent to all the paths starting from node. This provides a
            // basis for the pathSums starting from node.
            // Then we add additional paths starting from the node and going
            // through the parent, which it the number of nodes not in the
            // subtree rooted at node
            pathSums[node] = pathSums[parent] - subtreeSize[node] + N - subtreeSize[node];
        }
        for (int child : graph.getOrDefault(node, Collections.emptyList())) {
            if (child == parent)
                continue;
            dfs2(child, node);
        }
    }

    public int[] sumOfDistancesInTree(int n, int[][] edges) {
        /*
         * This is the official solution.
         *
         * The number of paths is equal to the number of nodes in a node's
         * subtree (including the node itself).
         */
        for (int [] tup : edges) {
            int a = tup[0];
            int b = tup[1];
            graph.putIfAbsent(a, new ArrayList<>());
            graph.putIfAbsent(b, new ArrayList<>());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }
        N = n;
        subtreeSize = new int[n];
        Arrays.fill(subtreeSize, 1);
        pathSums = new int[n];
        dfs1(0, -1);
        dfs2(0, -1);
        return pathSums;
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
