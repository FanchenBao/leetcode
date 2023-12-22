class Solution {
    public int maxWidthOfVerticalArea(int[][] points) {
        /*
        LeetCode 1637
        
        Sort based on x coord and then find the max gap among pairs of
        x coords.
        
        O(NlogN), 44 ms, faster than 9.23%
        */
        Arrays.sort(points, Comparator.comparingInt(t -> t[0]));
        int res = 0;
        for (int i = 0; i < points.length - 1; i++) {
            res = Math.max(res, points[i + 1][0] - points[i][0]);
        }
        return res;
    }
}

