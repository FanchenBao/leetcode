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
    Map<Integer, List<Integer>> graph = new HashMap<>();
    
    private boolean dfs(int node, int[] nums, int k, int parent) {
        boolean shouldXOR = false;
        for (int child : graph.getOrDefault(node, Collections.emptyList())) {
            if (child != parent)
                shouldXOR ^= dfs(child, nums, k, node);
        }
        if (shouldXOR)
            nums[node] ^= k;
        if ((nums[node] ^ k) > nums[node]) {
            nums[node] ^= k;
            return true;
        }
        return false;
    }

    public long maximumValueSum(int[] nums, int k, int[][] edges) {
        /*
         * LeetCode 3068
         *
         * We go from leaf to root and try to maximize everything. At the end,
         * if there is no need for the root to XOR, we already have the max
         * sum possible.
         *
         * If the root needs to XOR in order to achieve its max, we should
         * propagate the XOR down the tree to a node whose reduction in value
         * after XOR is miminized. When XOR is propagated down from the root,
         * we can reach any node in the tree.
         *
         * O(E + V), 36 ms, faster than 7.63%
         */
        for (int[] uv : edges) {
            graph.putIfAbsent(uv[0], new ArrayList<>());
            graph.putIfAbsent(uv[1], new ArrayList<>());
            graph.get(uv[0]).add(uv[1]);
            graph.get(uv[1]).add(uv[0]);
        }
        boolean shouldRootXOR = dfs(0, nums, k, -1);
        long res = 0;
        for (int n : nums)
            res += (long)n;
        if (!shouldRootXOR)
            return res;
        int minDiff = 1000000001;
        for (int n : nums) {
            minDiff = Math.min(minDiff, n - (n ^ k));
        }
        return res - (long)minDiff;
    }
}


class Solution2 {
    public long maximumValueSum(int[] nums, int k, int[][] edges) {
        /*
         * Turns out we don't need to create the tree, because each time a
         * child XOR, it can always propagate up to the root. Thus, whether
         * there is an extra XOR to allocate depends on the parity of the total
         * number of XORs.
         *
         * O(N), 2 ms, faster than 76.34%
         */
        boolean shouldXOR = false;
        long res = 0;
        for (int n : nums) {
            if ((n ^ k) > n) {
                res += (long)(n ^ k);
                shouldXOR ^= true;
            } else {
                res += (long)n;
            }
        }
        if (!shouldXOR)
            return res;
        int minDiff = 1000000001;
        for (int n : nums)
            minDiff = Math.min(minDiff, Math.abs(n - (n ^ k)));
        return res - (long)minDiff;
    }
}


class Solution3 {
    long[][] memo;

    private long dp(int node, int shouldXOR, int[] nums, int k) {
        if (node == nums.length) {
            return shouldXOR == 1 ? Long.MIN_VALUE : (long)0;
        }
        if (memo[node][shouldXOR] >= 0)
            return memo[node][shouldXOR];
        long noXOR = nums[node] + dp(node + 1, shouldXOR, nums, k);
        long yesXOR = (nums[node] ^ k) + dp(node + 1, shouldXOR ^ 1, nums, k);
        memo[node][shouldXOR] = Math.max(noXOR, yesXOR);
        return memo[node][shouldXOR];
    }

    public long maximumValueSum(int[] nums, int k, int[][] edges) {
        /*
         * This is the DP solution from the official solution.
         * The key is to realize that any adjacent pair of XOR can be extended
         * to any other pair of nodes, regardless of whether they are adjacent.
         * Thus, the decision to XOR one node can be passed down as a state for
         * its children.
         *
         * O(N), 14 ms, faster than 20.61%
         */
        memo = new long[nums.length][2];
        for (long[] row : memo)
            Arrays.fill(row, (long)(-1));
        return dp(0, 0, nums, k);
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
