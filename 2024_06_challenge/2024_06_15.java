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
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        /*
         * LeetCode 502
         *
         * I used a bit of hint by checking what data structure to use for this
         * problem. The hint says sorting and priority queue, and the solution
         * is very straightforward.
         *
         * We sort capital along with its profits. Then we put all the profits
         * in a priority queue if its capital is smaller or equal to w at the
         * moment. Then we choose the largest profit in the queue for the
         * current w. The profit then gets added to w, and we will search
         * capital again to put more profits into the queue, if possible.
         *
         * We keep doing this until k projects have been selected or no profit
         * can be extracted from the queue.
         *
         * O(NlogN), 82 ms, faster than 72.14%
         */
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int N = profits.length;
        int[][] capprof = new int[N][2];
        for (int i = 0; i < N; i++) {
            capprof[i][0] = capital[i];
            capprof[i][1] = profits[i];
        }
        Arrays.sort(capprof, (a, b) -> Integer.compare(a[0], b[0]));
        int i = 0;
        while (k > 0) {
            if (i < N && capprof[i][0] <= w) {
                pq.add(-capprof[i][1]);
                i++;
            } else {
                if (pq.isEmpty())
                    break;
                w += -pq.poll();
                k--;
            }
        }
        return w;
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
