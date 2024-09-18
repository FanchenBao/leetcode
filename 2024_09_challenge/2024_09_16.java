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
    private int parseTimePoints(String timePoint) {
        return Integer.parseInt(timePoint.substring(0, 2)) * 60 + Integer.parseInt(timePoint.substring(3));
    }

    public int findMinDifference(List<String> timePoints) {
        /*
         * LeetCode 539
         *
         * Convert time point into its corresponding minutes, sort them, and
         * perform pair-wise diff. Note that time can wrap around. So the
         * difference in minute can either go t0 to t1, or t1 to t0 with wrap
         * around.
         *
         * O(NlogN) 5 ms, faster than 67.04%
         */
        int N = timePoints.size();
        int[] times = new int[N];
        for (int i = 0; i < N; i++)
            times[i] = parseTimePoints(timePoints.get(i));
        Arrays.sort(times);
        int res = Integer.MAX_VALUE;
        int maxTimePoint = 24 * 60;
        int diff = 0;
        for (int i = 1; i < N; i++) {
            diff = times[i] - times[i - 1];
            res = Math.min(res, Math.min(diff, maxTimePoint - diff));
        }
        // Wrap around the last to compare with the first time
        diff = times[N - 1] - times[0];
        return Math.min(res, Math.min(diff, maxTimePoint - diff));
    }
}


class Solution2 {
    private int parseTimePoints(String timePoint) {
        return Integer.parseInt(timePoint.substring(0, 2)) * 60 + Integer.parseInt(timePoint.substring(3));
    }

    public int findMinDifference(List<String> timePoints) {
        /*
         * Same as Solution1, but we don't have to perform the wrap around
         * during the pair-wise comparison. We only need to do it when comparing
         * times[N - 1] and times[0]
         *
         * O(NlogN)
         */
        int N = timePoints.size();
        int[] times = new int[N];
        for (int i = 0; i < N; i++)
            times[i] = parseTimePoints(timePoints.get(i));
        Arrays.sort(times);
        int res = Integer.MAX_VALUE;
        for (int i = 1; i < N; i++)
            res = Math.min(res, times[i] - times[i - 1]);
        // Wrap around the last to compare with the first time
        int diff = times[N - 1] - times[0];
        int maxTimePoint = 24 * 60;
        return Math.min(res, Math.min(diff, maxTimePoint - diff));
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
