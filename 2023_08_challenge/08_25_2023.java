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
