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
    public int minimizedMaximum(int n, int[] quantities) {
        /*
         * LeetCode 2064
         *
         * Since this is min-max problem, binary search is the first to come
         * to mind.
         *
         * O(MlogK), where M = len(quantities), K = max of quantities
         */
        int total = 0;
        int hi = 0;
        for (int q : quantities) {
            total += q;
            hi = Math.max(q, hi);
        }
        int lo = total / n;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            int stores = 0;
            for (int q : quantities)
                stores += q / mid + (q % mid == 0 ? 0 : 1);
            if (stores <= n)
                hi = mid;
            else
                lo = mid + 1;
        }
        return lo;
    }
}


class Solution {
    private int ceilDiv(int a, int b) {
        return a / b + (a % b == 0 ? 0 : 1);
    }

    public int minimizedMaximum(int n, int[] quantities) {
        /*
         * This is the greedy solution from the official solution. It is very
         * smart. We first assign each quantity to a store. Then we always
         * select the quantity with the highest quantity-to-store ratio, and
         * break it evenly with the next available store. We keep doing this
         * until there is no available store left.
         *
         * Then the highest ratio at that moment is the answer.
         *
         * O(MlogM + (N - M)logM) = O(NlogM)
         */
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Long.compare((long) b[0] * a[1], (long) a[0] * b[1]));
        for (int q : quantities)
            pq.add(new int[]{q, 1});
        n -= quantities.length;
        while (n > 0 && !pq.isEmpty() && pq.peek()[0] > pq.peek()[1]) {
            int[] ele = pq.poll();
            ele[1]++;
            pq.add(ele);
            n--;
        }
        return ceilDiv(pq.peek()[0], pq.peek()[1]);
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
