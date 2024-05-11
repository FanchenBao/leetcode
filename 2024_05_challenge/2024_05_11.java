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
    public double mincostToHireWorkers(int[] quality, int[] wage, int k) {
        /*
         * LeetCode 857
         *
         * Not very difficult, especially when I have been primed for the
         * solution of priority queue by the problems of yesterday. We sort
         * all the qualities based on the wage per quality. For any given wage
         * per quality, the restriction on the minimum wages determines that
         * only those workers with lower wage per quality can be included in
         * the work group. Otherwise, the worker with the higher wage per
         * quality determines the base wage per quality.
         *
         * Then, it is the question of finding the sum of the smallest k qualities,
         * which can be solved using a max heap.
         *
         * O(NlogN + NlogK), 28 ms, faster than 66.80%
         */
        int N = quality.length;
        double[][] wagePerQual = new double[quality.length][2];
        for (int i = 0; i < N; i++) {
            wagePerQual[i][0] = wage[i] / (double)quality[i];
            wagePerQual[i][1] = quality[i];
        }
        Arrays.sort(wagePerQual, (a, b) -> Double.compare(a[0], b[0]));
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> Integer.compare(-a, -b)); // max heap
        int sumQual = 0; // sum of quality of the smallest k workers so far
        double res = 1000000000.0;
        for (int i = 0; i < N; i++) {
            int q = (int)wagePerQual[i][1];
            sumQual += q;
            pq.add(q);
            if (pq.size() > k)
                sumQual -= pq.poll();
            if (pq.size() == k)
                res = Math.min(res, wagePerQual[i][0] * sumQual);
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
