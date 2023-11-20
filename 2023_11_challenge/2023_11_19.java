class Solution {
    public int reductionOperations(int[] nums) {
        /*
        LeetCode 1887

        Count the numbers, sort the uniques. For each unique, the number of operations to
        bring all the values down to the min value is counter[unique] * idx, where the
        idx is the unique's position in the sorted uniques.

        O(N + NlogN), 66 ms, faster than 34.21%
         */
        Map<Integer, Integer> counter = new HashMap<>();
        for (int n : nums)
            counter.put(n, counter.getOrDefault(n, 0) + 1);
        List<Integer> sortedUniqs = new ArrayList<>(counter.keySet());
        Collections.sort(sortedUniqs);
        int res = 0;
        for (int i = sortedUniqs.size() - 1; i >= 0; i--)
            res += counter.get(sortedUniqs.get(i)) * i;
        return res;
    }
}


class Solution {
    public int reductionOperations(int[] nums) {
        /*
        This is the official solution which does not require a counter.

        We sort nums first. Then We use a separate variable to record the
        number of uniques encountered so far. Then for each number, the
        number of operations to bring the number down to the min would
        be the count of the current uniques.

        O(NlogN + N), 34 ms, faster than 81.58%
         */
        Arrays.sort(nums);
        int uniqCount = 0; int res = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1])
                uniqCount++;
            res += uniqCount;
        }
        return res;
    }
}
