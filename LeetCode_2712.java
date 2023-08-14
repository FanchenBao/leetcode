class Solution1 {
    String s;

    private long solve(char tgt) {
        int j = s.length() / 2;
        int i = j - 1;
        int invertCount = 0; long res = 0;
        while (i >= 0) {
            if ((invertCount % 2 == 0 && s.charAt(i) != tgt) | (invertCount % 2 == 1 && s.charAt(i) == tgt)) {
                res += i + 1;
                invertCount += 1;
            }
            i--;
        }
        invertCount = 0;
        while (j < s.length()) {
            if ((invertCount % 2 == 0 && s.charAt(j) != tgt) | (invertCount % 2 == 1 && s.charAt(j) == tgt)) {
                res += s.length() - j;
                invertCount += 1;
            }
            j++;
        }
        return res;
    }

    public long minimumCost(String s) {
        /*
        Greedy. We can easily prove that the left and right invert operations
        should not overlap each other, because otherwise, we will conduct
        duplicated operations and always make the cost bigger.

        Thus, the solution shall be two indices starting somewhere around the
        middle of s, one going left and the other right, progressively inverting
        all the chars until they all conform to the same. A key observation is
        that after even number of inversions, the char in s remain the same as
        the original version. After odd number of inversions, the char in s is
        the opposite of what it should be. This allows us to check whether a
        round of inversion is necessary to convert the letter at the current
        position.

        We use this method to convert everything to '1' or '0' and pick the one
        with the smallest cost.

        O(2N), 16 ms, faster than 21.89% 
        */
        if (s.length() == 1) {
            return 0;
        }
        this.s = s;
        return Math.min(solve('1'), solve('0')); 
    }
}


class Solution2 {
    public long minimumCost(String s) {
        /*
        Inspired by: https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/discuss/3574435/one-pass-dp-intuition-for-check-s-i-s-i-1/

        We can simply check s[i] and s[i - 1]. If they are identical, we don't have to make any inversion.
        Otherwise, we either invert s[:i] or invert s[i:] in order to maintain that s[:i + 1] are all identical.
        We choose the smaller of the two costs.

        O(N), 7 ms, faster than 97.98%
         */
        long res = 0;
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) != s.charAt(i - 1)) {
                res += Math.min(i, s.length() - i);
            }
        }
        return res;
    }
}
