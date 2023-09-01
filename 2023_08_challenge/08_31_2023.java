class Solution {
    public int minTaps(int n, int[] ranges) {
        /*
        LeetCode 1326

        Sort by the left interval. Then we use greedy. For each interval, we want to find the next max right before the
        left goes beyond the current max right. Thus, we set up two values: rm and next_rm where rm is the current max
        right and next_rm is the next max right.

        For each interval, if the left is larger than rm, we have gone beyond the current max right. In this case, if
        we also goes beyond the next max right, we have an unfillable gap. Return -1. Otherwise, next_rm becomes the
        current rm and we analyze the current interval.

        If the left is smaller or equal to rm, and if the right is also smaller or equal to rm, we do nothing because
        the current interval does not contribute anything. If the right is bigger than rm, there are multiple conditions.

        1. Left is smaller than 0. This means the current interval covers 0, and we simply maximize rm without touching
        next_rm or incrementing res.
        2. Otherwise, if next_rm does not exist, this means the current interval's right is the first extension to the
        right. We shall count this as a new tap. If next_rm already exists, then the tap has been counted. The final
        step is to maximize next_rm.

        O(NlogN + N), 14 ms, faster than 21.86%
         */
        int[][] intervals = new int[n + 1][2];
        for (int i = 0; i <= n; i++) {
            intervals[i][0] = i - ranges[i]; intervals[i][1] =  i + ranges[i];
        }
        Arrays.sort(intervals, Comparator.comparingInt(tup -> tup[0])); // sort by left
        int rm = intervals[0][1]; int next_rm = Integer.MIN_VALUE;
        int i = 1;
        int res = 1;
        while (i <= n && rm < n && next_rm < n) {
            if (intervals[i][0] > rm) {
                if (intervals[i][0] > next_rm) {
                    // there is a gap not fillable
                    return -1;
                }
                rm = next_rm;
                next_rm = Integer.MIN_VALUE;
            } else {
                if (intervals[i][1] > rm) {
                    if (intervals[i][0] <= 0) {
                        rm = intervals[i][1];
                    } else {
                        if (next_rm == Integer.MIN_VALUE) {
                            // new extension to the right
                            res++;
                        }
                        next_rm = Math.max(next_rm, intervals[i][1]);
                    }
                } // the else branch refers to intervals[i][1] <= rm, in which case we don't do anything
                i++;
            }
        }
        return res;
    }
}

