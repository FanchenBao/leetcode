class Solution {
    public int totalMoney(int n) {
        /*
        LeetCode 1716
        
        Some analysis.
        
        O(1), 0 ms, faster than 100.00%
        */
        int q = n / 7; int r = n % 7;
        return 28 * q + 7 * (q - 1) * q / 2 + r * (1 + r) / 2 + r * q;
    }
}

