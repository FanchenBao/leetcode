class Solution {
    public int countHomogenous(String s) {
        /*
        LeetCode 1759
        
        Find the length of each substring with the same letter, and compute
        the total number of homogenous substrings within. The formula to
        compute the count given a substring (every letter in the substring
        is the same) of size k is: (k + 1) * k / 2
        
        O(N), 11 ms, faster than 41.20%
        */
        long res = 0; long cnt = 1;
        int MOD = 1000000007;
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) != s.charAt(i - 1)) {
                res = (res + cnt * (cnt + 1) / 2) % MOD;
                cnt = 1;
            } else {
                cnt++;
            }
        }
        return (int)((res + cnt * (cnt + 1) / 2) % MOD);
    }
}