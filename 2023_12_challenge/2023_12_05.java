class Solution {
    public int numberOfMatches(int n) {
        /*
        LeetCode 1688
        
        bit manipulation.
        
        O(logN), 0 ms, faster than 100.00% 
        */
        int res = 0;
        while (n > 1) {
            res += (n & 1) + (n >> 1);
            n >>= 1;
        }
        return res;
    }
}


class Solution {
    public int numberOfMatches(int n) {
        /*
        Analytic solution. Each eliminated team must play
        a game and lose such game. Since eventually we have
        only one team left, there must have been n - 1
        matches for the n - 1 teams to lose.
        */
        return n - 1;
    }
}
