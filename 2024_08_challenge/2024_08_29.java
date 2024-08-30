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
    private int dfs(int node, Map<Integer, List<Integer>> graph, boolean[] seen) {
        int cnt = 1;
        for (int child : graph.getOrDefault(node, Collections.emptyList())) {
            if (!seen[child]) {
                seen[child] = true;
                cnt += dfs(child, graph, seen);
            }
        }
        return cnt;
    }

    public int removeStones(int[][] stones) {
        /*
         * LeetCode 947
         *
         * Consider the stones as nodes of a graph where two stones have an
         * edge if they share either the row or col index. Then the problem
         * becomes finding all the connected clique and count the number of
         * nodes in the clique. The answer is the sum of the count minus one
         * of each clique.
         *
         * O(N^2)
         */
        int N = stones.length;
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                if (stones[i][0] == stones[j][0] || stones[i][1] == stones[j][1]) {
                    graph.putIfAbsent(i, new ArrayList<>());
                    graph.putIfAbsent(j, new ArrayList<>());
                    graph.get(i).add(j);
                    graph.get(j).add(i);
                }
            }
        }
        boolean[] seen = new boolean[N];
        int res = 0;
        for (int i = 0; i < N; i++) {
            if (!seen[i]) {
                seen[i] = true;
                res += dfs(i, graph, seen) - 1;
            }
        }
        return res;
    }
}



class Solution2 {
    private void dfs(int node, Map<Integer, List<Integer>> graph, boolean[] seen) {
        for (int child : graph.getOrDefault(node, Collections.emptyList())) {
            if (!seen[child]) {
                seen[child] = true;
                dfs(child, graph, seen);
            }
        }
    }

    public int removeStones(int[][] stones) {
        /*
         * We don't even need to count the number of nodes. We just need to
         * count the number of cliques as that represents the number of stones
         * remaining. Thus the answer is the total number of stones minus the
         * count of the cliques.
         *
         * O(N^2)
         */
        int N = stones.length;
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                if (stones[i][0] == stones[j][0] || stones[i][1] == stones[j][1]) {
                    graph.putIfAbsent(i, new ArrayList<>());
                    graph.putIfAbsent(j, new ArrayList<>());
                    graph.get(i).add(j);
                    graph.get(j).add(i);
                }
            }
        }
        boolean[] seen = new boolean[N];
        int cliqueCnt = 0;
        for (int i = 0; i < N; i++) {
            if (!seen[i]) {
                seen[i] = true;
                dfs(i, graph, seen);
                cliqueCnt++;
            }
        }
        return N - cliqueCnt;
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
