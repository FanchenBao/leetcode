class Solution {
    public int buyChoco(int[] prices, int money) {
        /*
        LeetCode 2706
        
        Find the min and second min.
        O(N), 1 ms, faster than 100.00%
        
        */
        int min = 101;
        int secMin = 101;
        for (int p : prices) {
            if (p < min) {
                secMin = min;
                min = p;
            } else if (p < secMin) {
                secMin = p;
            }
        }
        return min + secMin <= money ? money - min - secMin : money;
    }
}
