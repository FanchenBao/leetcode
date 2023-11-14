class Solution {
    public int findNonMinOrMax(int[] nums) {
        /*
        Took me quite a while to get the second max search correctly.

        O(N), 4 ms, faster than 99.59%
        */
        int min = 100; int max = -1; int secondMax = -1;
        for (int n : nums) {
            if (n < min)
                min = n;
            if (n > max) {
                secondMax = max;
                max = n;
            }
            if (n > secondMax && n < max) secondMax = n;
        }
        if (secondMax == max || secondMax == min)
            return -1;
        return secondMax;
    }
}
