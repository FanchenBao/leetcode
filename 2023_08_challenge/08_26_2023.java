class Solution1 {

    Integer[] memo;
    HashMap<Integer, Integer> leftRight;
    Integer[] sortedLefts;

    private int dp(int idx) {
        if (idx >= sortedLefts.length) {
            return 0;
        }
        if (memo[idx] != null) {
            return memo[idx];
        }
        memo[idx] = dp(idx + 1); // not taking sortedPairs[idx]
        int binIdx = Arrays.binarySearch(sortedLefts, leftRight.get(sortedLefts[idx]));
        if (binIdx >= 0) {
            binIdx++;
        } else {
            binIdx = -(binIdx + 1);
        }
        memo[idx] = Math.max(memo[idx], 1 + dp(binIdx));
        return memo[idx];
    }

    public int findLongestChain(int[][] pairs) {
        /*
        LeetCode 646

        First condense all the pairs with the same start to one pair whose right is the smallest. There is a bit greedy
        to play here, because for multiple pairs with the same start, only the one with the smallest right can offer the
        best chance of forming a longer chain.

        Then we sort the lefts in the remaining pairs.

        Then we use DP to find the answer, where dp(idx) returns the max chain length of lefts[idx:].

         O(NlogN), 13 ms, faster than 57.21%
         */
        memo = new Integer[pairs.length];
        leftRight = new HashMap<>();
        for (int[] tup : pairs) {
            leftRight.put(tup[0], Math.min(tup[1], leftRight.getOrDefault(tup[0], Integer.MAX_VALUE)));
        }
        sortedLefts = leftRight.keySet().toArray(new Integer[0]);
        Arrays.sort(sortedLefts);
        return dp(0);

    }
}


class Solution2 {
    public int findLongestChain(int[][] pairs) {
        /*
        This is the solution from the last time I did the problem back in March 2022. We sort on right, then greedy it
        from left to right. Since each time the right we encounter is always the smallest so far, so we are guaranteed
        to always be at the optimal position for extending the chain. Thus,the greedy works.

        O(NlogN), 10 ms, faster than 84.02%
         */
        Arrays.sort(pairs, Comparator.comparingInt(tup -> tup[1]));
        int res = 0;
        int preRight = Integer.MIN_VALUE;
        for (int[] tup: pairs) {
            if (tup[0] > preRight) {
                res++;
                preRight = tup[1];
            }
        }
        return res;
    }
}
