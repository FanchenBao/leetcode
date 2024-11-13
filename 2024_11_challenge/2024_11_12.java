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
    public int[] maximumBeauty(int[][] items, int[] queries) {
        /*
         * LeetCode 2070
         *
         * Sort item by prices. Then produce a prefix max array on beauties.
         * Finally for each query, binary search item by price and use the
         * prefix max beauty as the result.
         *
         * We can make the prefix max beauty one element more than items. This
         * way when a query cannot find any item, i.e., the query value is
         * smaller than the smallest price of items, we automatically return
         * 0 for that query.
         *
         * O(NlogN), 40 ms, faster than 98.55%
         */
        double[] prices = new double[items.length];
        int[] beauties = new int[items.length + 1];
        Arrays.sort(items, (a, b) -> Integer.compare(a[0], b[0]));
        for (int i = 0; i < items.length; i++) {
            prices[i] = (double)items[i][0];
            beauties[i + 1] = Math.max(beauties[i], items[i][1]);
        }
        int[] res = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int idx = Arrays.binarySearch(prices, queries[i] + 0.1);
            res[i] = beauties[-(idx + 1)];
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
