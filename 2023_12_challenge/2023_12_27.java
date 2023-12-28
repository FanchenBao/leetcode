class Solution {
    public int minCost(String colors, int[] neededTime) {
        /*
        LeetCode 1578
        
        I thought it was DP, but turned out much easier. Just
        find the sum of all consecutive colors and the max time
        among them. The answer is the sum of the sum of
        consecutives minus the max.
        
        O(N), 11 ms, faster than 27.51%
         */
        int res = 0;
        int sum = neededTime[0];
        int max = neededTime[0];
        int cnt = 1;
        for (int i = 1; i < colors.length(); i++) {
            if (colors.charAt(i) != colors.charAt(i - 1)) {
                if (cnt > 1)
                    res += sum - max;
                sum = 0;
                max = 0;
                cnt = 0;
            }
            sum += neededTime[i];
            max = Math.max(max, neededTime[i]);
            cnt++;
        }
        if (cnt > 1)
            res += sum - max;
        return res;
    }
}


class Solution {
    public int minCost(String colors, int[] neededTime) {
        /*
        Inspired by an implementation of a fast algorithm.

        We do not add to res when not consecutive. Instead,
        we add when consecutive. This way, we don't need to
        use the cnt variable.

        O(N), 9 ms, faster than 61.18%
         */
        int res = 0;
        int max = neededTime[0];
        for (int i = 1; i < colors.length(); i++) {
            if (colors.charAt(i) == colors.charAt(i - 1)) {
                if (neededTime[i] >= max) {
                    res += max;
                    max = neededTime[i];
                } else {
                    res += neededTime[i];
                }
            } else {
                max = neededTime[i];
            }
        }
        return res;
    }
}

