class Solution {
    public int numDecodings(String s) {
        /*
        LeetCode 91

        Space optimized DP.

        O(N), 1 ms, faster than 84.19%
         */
        if (s.charAt(0) == '0')
            return 0;
        if (s.length() == 1)
            return 1;
        int p = 1; int pp = 1;
        for (int i = 1; i < s.length(); i++) {
            int d = s.charAt(i) - '0';
            int cur = 0;
            if (d > 0)
               cur += p;
            int dd = s.charAt(i - 1) - '0';
            if (dd > 0 && dd * 10 + d <= 26)
                cur += pp;
            pp = p;
            p = cur;
        }
        return p;
    }
}

