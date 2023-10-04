class Solution {

    public int numIdenticalPairs(int[] nums) {
        /*
        LeetCode 1512
        
        No need to implement nCk, because k is always 2.
        Thus the count is n * (n - 1) // 2
        
        O(N), 1 ms, faster than 86.48%
        */
        Map<Integer, Integer> counter = new HashMap<>();
        for (int n : nums) {
            counter.put(n, counter.getOrDefault(n, 0) + 1);
        }
        int res = 0;
        for (int v : counter.values()) {
            res += v * (v - 1) / 2;
        }
        return res;
    }
}