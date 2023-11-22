class Solution {
    private int rev(int n) {
        String strn = String.valueOf(n);
        String revStrn = new StringBuilder(strn).reverse().toString();
        return Integer.parseInt(revStrn);
    }

    public int countNicePairs(int[] nums) {
        /*
        LeetCode 1814

        If x + rev(y) = y + rev(x), then x - rev(x) = y - rev(y). We can group all the
        numbers that have the same difference between itself and its rev, and any pair
        among them is a nice pair.

        O(N), 70 ms, 13%
         */
        Map<Integer, Integer> counter = new HashMap<>();
        for (int n : nums) {
            int diff = n - rev(n);
            counter.put(diff, counter.getOrDefault(diff, 0) + 1);
        }
        long res = 0;
        int MOD = 1000000007;
        for (int c : counter.values())
            res = (res + (long)c * (c - 1) / 2) % MOD;
        return (int)res;
    }
}
