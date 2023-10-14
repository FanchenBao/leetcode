class Solution {
    public int minCostClimbingStairs(int[] cost) {
        /*
        LeetCode 746
        
        DP
        
        O(N), 0 ms, faster than 100.00%
        */
        int second = cost[cost.length - 1]; int first = cost[cost.length - 2]; int tmp;
        for (int i = cost.length - 3; i >= 0; i--) {
            tmp = Math.min(first, second) + cost[i];
            second = first; first = tmp;
        }
        return Math.min(first, second);
    }
}
