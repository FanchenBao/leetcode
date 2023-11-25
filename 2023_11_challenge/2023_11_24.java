class Solution {
    public int maxCoins(int[] piles) {
        /*
        LeetCode 1561
        
        Greedy works. Always pick the second largest for myself at each step.
        
        O(NlogN), 27 ms, faster than 98.94%
         */
        Arrays.sort(piles);
        int i = 0; int j = piles.length - 1;
        int res = 0;
        while (i < j) {
            res += piles[j - 1];
            i++; j -= 2;
        }
        return res;
    }
}
