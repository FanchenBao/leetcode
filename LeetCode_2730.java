class Solution {
    public int longestSemiRepetitiveSubstring(String s) {
        /*
        O(1) extra space.
        
        5 ms, faster than 100.00% 
        */
        int pp = 0; int p = 0; int res = 0;
        for (int i = 0; i < s.length() - 1; i++) {
            if (s.charAt(i + 1) == s.charAt(i)) {
                res = Math.max(res, i - pp + 1);
                pp = p; p = i + 1;
            }
        }
        res = Math.max(res, s.length() - 1 - pp + 1);
        return res;
    }
}
