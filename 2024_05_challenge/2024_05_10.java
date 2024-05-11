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
    public int[] kthSmallestPrimeFraction(int[] arr, int k) {
        /*
         * LeetCode 786
         *
         * Brute force, O(N^2), 422 ms, faster than 45.85%
         */
        List<int[]> fracs = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++)
                fracs.add(new int[]{arr[i], arr[j]});
        }
        Collections.sort(fracs, (a, b) -> Float.compare(a[0] / (float)a[1], b[0] / (float)b[1]));
        return fracs.get(k - 1);
    }
}


class Solution2 {
    public int[] kthSmallestPrimeFraction(int[] arr, int k) {
        /*
         * This is the priority solution from the official solution. It is
         * similar to merging K sorted array. We treat all the fraction with
         * the same nominator as a sorted array (sorted in ascend). Then we
         * put the smallest value of each array in a priority queue. The first
         * one that pops out is the smallest. Then we replenish the priority
         * queue with the immediate next value of the same sorted array. Once
         * we pop out k values, we have the answer.
         *
         * O(KlogN + NlogN), 229 ms, faster than 70.31%
         */
        PriorityQueue<double[]> pq = new PriorityQueue<>((a, b) -> Double.compare(a[0], b[0]));
        int N = arr.length;
        for (int i = 0; i < N - 1; i++)
            pq.add(new double[]{1.0 * arr[i] / arr[N - 1], i, N - 1});
        double[] tmp;
        while (k > 1 && !pq.isEmpty()) {
            tmp = pq.poll();
            int ni = (int)tmp[1];
            int nj = (int)tmp[2];
            k--;
            if (nj - 1 > ni)
                pq.add(new double[]{1.0 * arr[ni] / arr[nj - 1], ni, nj - 1});
        }
        if (pq.isEmpty())
            return new int[2];
        tmp = pq.poll();
        return new int[]{tmp[1], tmp[2]};
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
