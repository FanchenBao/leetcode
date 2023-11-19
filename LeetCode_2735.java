class Solution {
    public long minCost(int[] nums, int x) {
        /*
        Find the min cost of collecting all the chocolates after each shift. If a chocolate
        can be collected with a smaller cost previously, continue to use that previous cost.

        O(N^2), 35 ms, faster than 84.82% 
         */
        int N = nums.length;
        int[] minC = new int[N]; // min cost of collecting the ith chocolate after all the shifts
        long cur = 0; // the total cost of collecting all the chocolate at their shifted positions
        for (int i = 0; i < N; i++) {
            minC[i] = nums[i];
            cur += nums[i];
        }
        long res = cur;
        int j;
        for (int s = 1; s < N; s++) {
            for (int i = 0; i < N; i++) {
                j = (i - s + N) % N;
                if (minC[i] > nums[j]) {
                    // update the min cost of collecting the ith chocolate after a shift
                    cur += nums[j] - minC[i];
                    minC[i] = nums[j];
                }
            }
            res = Math.min(res, (long)s * x + cur);
        }
        return res;
    }
}
