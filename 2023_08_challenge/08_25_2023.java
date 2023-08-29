class Solution1 {

    Boolean[][][] memo;
    String s1;
    String s2;
    String s3;

    private boolean dp(int i, int j, int type) {
        if (memo[type][i][j] != null) {
            return memo[type][i][j];
        }
        int k = i + j; // index for s3
        memo[type][i][j] = false;
        if (type == 0) {
            // must use s1 first
            for (int ii = i; ii < s1.length(); ii++) {
                if (s1.charAt(ii) == s3.charAt(k + ii - i)) {
                    if (dp(ii + 1, j, 1)) {
                        memo[type][i][j] = true;
                        break;
                    }
                } else {
                    break;
                }
            }
        } else {
            // must use s2 first
            for (int jj = j; jj < s2.length(); jj++) {
                if (s2.charAt(jj) == s3.charAt(k + jj - j)) {
                    if (dp(i, jj + 1, 0)) {
                        memo[type][i][j] = true;
                        break;
                    }
                } else {
                    break;
                }
            }
        }
        return memo[type][i][j];
    }

    public boolean isInterleave(String s1, String s2, String s3) {
        if (s1.length() + s2.length() != s3.length()) {
            return false;
        }
        this.memo = new Boolean[2][s1.length() + 1][s2.length() + 1];
        memo[0][s1.length()][s2.length()] = true;
        memo[1][s1.length()][s2.length()] = true;
        this.s1 = s1;
        this.s2 = s2;
        this.s3 = s3;

        return dp(0,  0, 0) || dp(0, 0, 1);
    }
}

class Solution2 {

    Boolean[][][] memo;
    String s1;
    String s2;
    String s3;

    private boolean dp(int i1, int i2, int i3) {
        if (memo[i1][i2][i3] != null) {
            return memo[i1][i2][i3];
        }
        if (i1 == s1.length() && i2 == s2.length() && i3 == s3.length()) {
            return true;
        }
        memo[i1][i2][i3] = false;
        if (i1 < s1.length() && i3 < s3.length() && s1.charAt(i1) == s3.charAt(i3)) {
            memo[i1][i2][i3] |= dp(i1 + 1, i2, i3 + 1);
        }
        if (i2 < s2.length() && i3 < s3.length() && s2.charAt(i2) == s3.charAt(i3)) {
            memo[i1][i2][i3] |= dp(i1, i2 + 1, i3 + 1);
        }
        return memo[i1][i2][i3];
    }

    public boolean isInterleave(String s1, String s2, String s3) {
        /*
        Easier implementation, but not necessarily faster.

        O(MNK), 5 ms, faster than 36.59%
         */
        if (s1.length() + s2.length() != s3.length()) {
            return false;
        }
        this.memo = new Boolean[s1.length() + 1][s2.length() + 1][s3.length()];
        this.s1 = s1;
        this.s2 = s2;
        this.s3 = s3;

        return dp(0,  0, 0);
    }
}


class Solution3 {
    public boolean isInterleave(String s1, String s2, String s3) {
        /*
        Bottom up. Write out the DP table and analyze it slowly. You will get
        the 1D dp.
        
        O(s2.length()) space complexity
        O(MN) time complexity
         */
        if (s1.length() + s2.length() != s3.length()) {
            return false;
        }
        boolean[] dp = new boolean[s2.length() + 1];
        dp[s2.length()] = true;
        for (int i = s1.length(); i >= 0; i--) {
            for (int j = s2.length(); j >= 0; j--) {
                if (i < s1.length() && s1.charAt(i) != s3.charAt(i + j)) {
                    dp[j] = false;
                }
                if (j < s2.length() && s2.charAt(j) == s3.charAt(i + j)) {
                    dp[j] |= dp[j + 1];
                }
            }
        }
        return dp[0];
    }
}

class Solution4 {

    Boolean[][] memo;
    String s1;
    String s2;
    String s3;

    private boolean dp(int i1, int i2) {
        if (memo[i1][i2] != null) {
            return memo[i1][i2];
        }
        if (i1 == s1.length() && i2 == s2.length()) {
            return true;
        }
        memo[i1][i2] = false;
        if (i1 < s1.length() && s1.charAt(i1) == s3.charAt(i1 + i2)) {
            memo[i1][i2] |= dp(i1 + 1, i2);
        }
        if (i2 < s2.length() && s2.charAt(i2) == s3.charAt(i1 + i2)) {
            memo[i1][i2] |= dp(i1, i2 + 1);
        }
        return memo[i1][i2];
    }

    public boolean isInterleave(String s1, String s2, String s3) {
        /*
        O(MN), 1 ms, faster than 90.09%
        
        Interestingly, the bottom up version of this DP is much slower, with 9 ms. Perhaps recursion is faster than
        looping in Java??
         */
        if (s1.length() + s2.length() != s3.length()) {
            return false;
        }
        memo = new Boolean[s1.length() + 1][s2.length() + 1];
        this.s1 = s1;
        this.s2 = s2;
        this.s3 = s3;

        return dp(0, 0);
    }
}
