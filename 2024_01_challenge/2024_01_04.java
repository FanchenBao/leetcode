class Solution {
    public int minOperations(int[] nums) {
        /*
        LeetCode 2870
        
        Count the frequencies and divide by 3. If there is no
        remainder, the number of operations is the quotient.
        
        If there is 1 remainder, then n - 4 must be divisible
        by 3, and the remaining 4 can be handled by two 2s.
        
        If there is 2 remainder, then the remainder itself can
        be handled by one 2.
        
        O(N), 19 ms, faster than 73.58%
        */
        Map<Integer, Integer> counter = new HashMap<>();
        for (int n : nums) 
            counter.put(n, counter.getOrDefault(n, 0) + 1);
        int res = 0;
        for (int v : counter.values()) {
            if (v == 1)
                return -1;
            res += v / 3 + (v % 3 == 0 ? 0 : 1);
        }
        return res;
    }
}

