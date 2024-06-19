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
    public int maxProfitAssignment(int[] difficulty, int[] profit, int[] worker) {
        /*
         * LeetCode 826
         *
         * Sort worker, sort difficulty and profit. Use priority queue to keep
         * the profits of all jobs whose difficulty is smaller or equal to the
         * current worker. Then we pick the largest profit for that worker.
         * Then we move on to the next worker and repeat the previous process.
         *
         * Note that since the job can be duplicated, we do not pop the profit
         * from the priority queue.
         *
         * O(NlogN + MlogM + MlogN), 31 ms, faster than 31.08%
         */
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int N = difficulty.length;
        int[][] difprof = new int[N][2];
        for (int i = 0; i < N; i++) {
            difprof[i][0] = difficulty[i];
            difprof[i][1] = profit[i];
        }
        Arrays.sort(difprof, (a, b) -> Integer.compare(a[0], b[0]));
        Arrays.sort(worker);
        int res = 0;
        int i = 0;
        for (int w : worker) {
            while (i < N && w >= difprof[i][0]) {
                pq.add(-difprof[i][1]);
                i++;
            }
            if (!pq.isEmpty())
                res += -pq.peek();
        }
        return res;
    }
}


class Solution2 {
    public int maxProfitAssignment(int[] difficulty, int[] profit, int[] worker) {
        /*
         * Similar idea from the official solution but without using priority
         * queue. This is because we can keep track of the max profit for each
         * worker, similar to a prefix max.
         *
         * O(NlogN + MlogM), 19 ms, faster than 70.64% 
         */
        int N = difficulty.length;
        int[][] difprof = new int[N][2];
        for (int i = 0; i < N; i++) {
            difprof[i][0] = difficulty[i];
            difprof[i][1] = profit[i];
        }
        Arrays.sort(difprof, (a, b) -> Integer.compare(a[0], b[0]));
        Arrays.sort(worker);
        int res = 0;
        int i = 0;
        int maxProf = 0;
        for (int w : worker) {
            while (i < N && w >= difprof[i][0]) {
                maxProf = Math.max(maxProf, difprof[i][1]);
                i++;
            }
            if (maxProf > 0)
                res += maxProf;
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
