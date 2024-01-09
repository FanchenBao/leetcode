class Solution {
    public int minimumIndex(List<Integer> nums) {
        /*
        First find the dominant number and its frequency.
        
        Then go from left to right and keep the count of the dominant.
        
        For each encounter of the dominant, see if it is still dominant on
        the current left subarray, and then check if it is also dominant on
        the right subarray. We can do this check because we know the total
        count of the dominant and its count on the left. We return the first
        index that satisifies both.
        
        O(N), 34 ms, faster than 43.14% 
        */
        int N = nums.size();
        int dom = 0;
        Map<Integer, Integer> counter = new HashMap<>();
        for (int n : nums) {
            counter.put(n, counter.getOrDefault(n, 0) + 1);
            if (counter.get(n) * 2 > N) {
                dom = n;
            }
        }
        int cntDom = 0;
        for (int i = 0; i < N; i++) {
            if (nums.get(i) == dom) {
                cntDom++;
                if (cntDom * 2 > i + 1 && (counter.get(dom) - cntDom) * 2 > N - i - 1)
                    return i;
            }
        }
        return -1;
    }
}

