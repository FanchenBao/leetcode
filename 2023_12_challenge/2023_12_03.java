class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        /*
        LeetCode 1266
        
        The min steps to take to go from points[i] to points[i + 1]
        is the bigger absolute difference between either the x or
        y coordinates.
        
        O(N) 1 ms, faster than 95.62%
        */
        int res = 0;
        for (int i = 1; i < points.length; i++) {
            int x0 = points[i - 1][0]; int y0 = points[i - 1][1];
            int x1 = points[i][0]; int y1 = points[i][1];
            res += Math.max(Math.abs(x0 - x1), Math.abs(y0 - y1));
        }
        return res;
    }
}
