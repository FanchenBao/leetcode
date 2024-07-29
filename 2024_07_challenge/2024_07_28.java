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
    public int secondMinimum(int n, int[][] edges, int time, int change) {
        /*
         * LeetCode 2045
         *
         * Use a BFS that allows the visit of a node if it is the first time
         * which means we are finding the min path to reach it, or if the
         * path to reach it is just ONE more than the min path. This guarantees
         * that when N is reached, it is either reached with the min path or
         * the min + 1 path.
         *
         * If min + 1 path is possible from 1 to N, then that is the second
         * minimum. If not, we need to do a back and forth such that the second
         * minimum is min + 2.
         *
         * Then based on the second minimum step, we can compute the time with
         * the help of the given time of each edge and the change frequency
         * of traffic light.
         *
         * O(??), 217 ms, faster than 9.33%
         */
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] e : edges) {
            graph.putIfAbsent(e[0], new ArrayList<>());
            graph.putIfAbsent(e[1], new ArrayList<>());
            graph.get(e[0]).add(e[1]);
            graph.get(e[1]).add(e[0]);
        }
        // BFS for min and min + 1 steps from 1 -> n
        int[] minSteps = new int[n + 1];
        Arrays.fill(minSteps, Integer.MAX_VALUE);
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{1, 0});
        boolean reachedWithSecMin = false;
        while (!queue.isEmpty()) {
            int[] ele = queue.poll();
            if (ele[0] == n && ele[1] == minSteps[n] + 1) {
                reachedWithSecMin = true;
                    break;
            }
            int nextStep = ele[1] + 1;
            for (int child : graph.get(ele[0])) {
                if (nextStep <= minSteps[child] || nextStep == minSteps[child] + 1) {
                    minSteps[child] = Math.min(minSteps[child], nextStep);
                    queue.add(new int[]{child, nextStep});
                }
            }
        }
        // If we can reach N multiple times using the BFS scheme
        // above, that means the second min step to reach it is
        // min step + 1 steps.
        // Otherwise, the second min steps to reach N is to perform
        // a back and forth, which means we will reach it in min step
        // + 2.
        int secMinStep = reachedWithSecMin ? minSteps[n] + 1 : minSteps[n] + 2;
        int res = 0;
        for (int i = 0; i < secMinStep - 1; i++) {
            res += time;
            int tmp = res / change;
            if (tmp % 2 == 1)
                res = (tmp + 1) * change;
        }
        return res + time;
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
