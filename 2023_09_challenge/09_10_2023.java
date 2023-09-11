class Solution {
    public int countOrders(int n) {
        /*
        LeetCode 1359

        Each order is independent of others. Thus, for each order, the possible ways to place them among the empty spots
        is nC2, where n is the number of empty spots.

        Thus, the first pair has nC2 possible ways. The second pair has (n - 2)C2 possible ways, ..., the last pair has
        2C2 possible ways.

        We cannot compute all the combinatorials directly, but we can expand them and find pattern. We take advantage
        of the pattern and perform MOD multiplication to find the answer.

        Note that the result has to be long to avoid overflow during the computation.

        O(N), 0 ms, faster than 100.00% 
         */
        long res = 1;
        int MOD = 1000000007;
        for (int i = 1; i <= n; i++) {
            res = ((res * i) % MOD * (2L * i - 1)) % MOD;
        }
        return (int)res;
    }
}
