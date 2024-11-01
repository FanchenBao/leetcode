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
    public long minimumTotalDistance(List<Integer> robot, int[][] factory) {
        /*
         * LeetCode 2463 (Fail)
         *
         * Second time with this problem, still unable to solve. The top down
         * dp(i, j, k) solution is good, where dp(i, j, k) is the min distance
         * of fixing robot[i:] using factory[j:] with factory[j] having k
         * robots already fixed.
         *
         * This solution comes from the official solution, which flattens the
         * factory array to make the DP effort 2D, instead of 3D.
         *
         * The idea is the same with dp[i][j] = min distance of fixing robot[i:]
         * using flatFact[j:]. We need to go from right to left to ensure that
         * each DP step has previously computed values.
         *
         * O(MN), where M = len(robot) and N is the total number of capacies
         * of all factories.
         *
         *  61 ms, faster than 20.00%
         */
        int M = robot.size();
        List<Integer> flatFact = new ArrayList<>();  // flatten factories, so we don't need to use a 3D DP
        for (int[] f : factory) {
            for (int i = 0; i < f[1]; i++)
                flatFact.add(f[0]);
        }
        int N = flatFact.size();
        Collections.sort(flatFact);
        Collections.sort(robot);
        // dp[i][j] = min distance of fixing robots[i:] using flatFact[j:]
        long[][] dp = new long[M][N];
        for (int i = M - 1; i >= 0; i--) {
            for (int j = N - 1; j >= 0; j--) {
                // option 1, skip flatFact j
                long opt1Val = j == N - 1 ? Long.MAX_VALUE : dp[i][j + 1];
                // option 2, use flatFact j
                long nextVal = i == M - 1 ? 0 : (j == N - 1 ? Long.MAX_VALUE : dp[i + 1][j + 1]);
                long opt2Val = nextVal == Long.MAX_VALUE ? Long.MAX_VALUE : Math.abs(robot.get(i) - flatFact.get(j)) + nextVal;
                dp[i][j] = Math.min(opt1Val, opt2Val);
            }
        }
        return dp[0][0];
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
