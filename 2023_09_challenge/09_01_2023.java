class Solution1 {
    private int countOccurences(String str, char c) {
        int count = 0;
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == c) {
                count++;
            }
        }
        return count;
    }

    public int[] countBits(int n) {
        int[] res = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            String bin = Integer.toBinaryString(i);
            res[i] = countOccurences(bin, '1');
        }
        return res;
    }
}


class Solution2 {
    public int[] countBits(int n) {
        /*
        Leetcode 338

        O(N), take advantage of power of 2
         */
        int[] res = new int[n + 1];
        int curPot = 1; int nextPot = 2;
        for (int i = 1; i <= n; i++) {
            if (i == nextPot) {
                curPot = nextPot;
                nextPot *= 2;
            }
            res[i] = res[i - curPot] + 1;
        }
        return res;
    }
}

class Solution3 {
    public int[] countBits(int n) {
        /*
        Leetcode 338

        Inspired by https://leetcode.com/problems/counting-bits/discuss/1808016/C%2B%2B-oror-Vectors-Only-oror-Easy-To-Understand-oror-Full-Explanation
        I think this is the right way to do it. For each value, we simply right shift to obtain the number of 1 count of
        a previous number. Then we add the last digit, either 1 or 0.

        O(N), 1 ms, faster than 99.63%
         */
        int[] res = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            res[i] = res[i >> 1] + i % 2;
        }
        return res;
    }
}
