class Solution {
    Integer[][][] memo;
    String[] words;

    private int dp(int idx, int l, int r) {
        if (idx == words.length)
            return 0;
        // dp returns the min additional chars added to the previous str starting with l and ending with r
        if (memo[idx][l][r] != null)
            return memo[idx][l][r];
        String w = words[idx];
        int s = w.charAt(0) - 97; int e = w.charAt(w.length() - 1) - 97;
        // append words[idx][0] to r
        int pos1 = dp(idx + 1, l, e) + (s == r ? w.length() - 1 : w.length());
        // append words[idx][-1] to l
        int pos2 = dp(idx + 1, s, r) + (e == l ? w.length() - 1 : w.length());
        memo[idx][l][r] = Math.min(pos1, pos2);
        return memo[idx][l][r];
    }

    public int minimizeConcatenatedLength(String[] words) {
        /*
        Use DP, where dp(idx, left, right) represents the min additional
        letter added to the string when incorporating words[idx] with
        the previous string starting with left and ending with right.
        
        In the implementation, left and right is replaced with the index
        form of chars a to z, where char a is 0 and char z is 25.
        
        For each words[idx], there are two ways to be appended to the
        previous str, either at the front or at the end. Depending on
        whether there are matches, the additional letters added to the
        str will change.
        
        O(N*26*26), 34 ms, faster than 94.19%
        */
        memo = new Integer[words.length][26][26];
        this.words = words;
        String w = words[0];
        int s = w.charAt(0) - 97; int e = w.charAt(w.length() - 1) - 97;
        return w.length() + dp(1, s, e);
    }
}
