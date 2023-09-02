class Solution1 {
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



class Solution2 {
    public int minTaps(int n, int[] ranges) {
        /*
        DP solution from the official solution.

        First, create all the ranges, but the left should not go below 0 and the right should not go beyond n.

        Then define dp[i] as the min number of taps to cover [0, i]. For each position j in a range (start, end),
        dp[end] = min(dp[end], dp[j] + 1)

        The answer is dp[n] if it has been computed. Otherwise, -1.
        
        O(MN) where M is the average value in ranges.
         */
        int[] dp = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            // initialization. Note that dp[0] = 0, because no tap is needed to
            // water [0, 0] (the stretch of garden has 0 length)
            // Other positions are initialized with an impossible large value.
            dp[i] = n + 1;
        }
        for (int i = 0; i <= n; i++) {
            int left = Math.max(0, i - ranges[i]); int right = Math.min(n, i + ranges[i]);
            for (int j = left; j <= right; j++) {
                dp[right] = Math.min(dp[right], dp[j] + 1);
            }
        }
        return dp[n] < n + 1 ? dp[n] : -1;
    }
}


class Solution3 {
    public int minTaps(int n, int[] ranges) {
        /*
        Use a maxReach array to record the max right reachable from each start. In other words, maxReach[i] is the max
        right reachable starting from i.

        Then the problem is converted to starting from 0 with the maxReach serving as the max jump possible from each
        position, what is the min number of jumps to reach n.

        Given a start and currReach, we go through them to find the max next reach. Then we repeat the same process
        until the max next reach goes to n or beyond.

        O(N), 4 ms, faster than 83.50% 
         */
        int[] maxReach = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            int left = Math.max(0, i - ranges[i]); int right = Math.min(n, i + ranges[i]);
            maxReach[left] = Math.max(maxReach[left], right);
        }
        int curLeft = 0; int curRight = maxReach[0];
        int res = 1;
        while (curRight < n) {
            int nextRight = 0;
            for (int i = curLeft; i <= curRight; i++) {
                nextRight = Math.max(nextRight, maxReach[i]);
            }
            if (nextRight <= curRight) {
                return -1;
            }
            res++;
            curLeft = curRight;
            curRight = nextRight;
        }
        return res;
    }
}

class Solution4 {
    public int minTaps(int n, int[] ranges) {
        /*
        Same as Solution3, but with another looping structure from the official
        solution.

        O(N)
         */
        int[] maxReach = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            int left = Math.max(0, i - ranges[i]); int right = Math.min(n, i + ranges[i]);
            maxReach[left] = Math.max(maxReach[left], right);
        }
        int res = 0;
        int curRight = 0; int nextRight = 0;
        for (int i = 0; i <= n; i++) {
            if (i > nextRight) {
                // the current position i cannot be covered by the next max reach. Impossible to cover the garden ending
                // at i.
                return -1;
            }
            if (i > curRight) {
                res++;
                curRight = nextRight;
            }
            nextRight = Math.max(nextRight, maxReach[i]);
        }
        return res;
    }
}

