class Solution {
    private boolean satisfy(int[] nums, int minMaxTgt) {
        Set<Integer> visited = new HashSet<>();
        int i;
        for (int j = nums.length - 1; j >= 0 && visited.size() < nums.length; j--) {
            if (visited.contains(j)) continue;
            i = j - 1;
            while (i >= 0 && (visited.contains(i) || i == j || nums[i] + nums[j] > minMaxTgt)) i--;
            if (i >= 0) visited.add(i);
            else break;
            visited.add(j);
        }
        return visited.size() == nums.length;
    }

    public int minPairSum(int[] nums) {
        /*
        TLE, because the function satisfy runs in O(N^2).
        */
        Arrays.sort(nums);
        int lo = 1; int hi = 2 * nums[nums.length - 1];
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (satisfy(nums, mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}


class Solution {
    public int minPairSum(int[] nums) {
        /*
        LeetCode 1877

        Greedy, but without a good proof

        O(NlogN) 53 ms, faster than 88.09%

        UPDATE: here is the proof.
        Suppose we can find a pairing that is not the greedy manner and can yield a
        smaller min max. Then there must exist four values
        
        a0 ≤ a1 ≤ a2 ≤ a3
        
        such that max(a0 + a2, a1 + a3) < max(a0 + a3, a1 + a2) 
        
        Since a1 + a3 >= a0 + a2, we have the premise a1 + a3 < max(a0 + a3, a1 + a2)
        
        Since a1 >= a0, we have a1 + a3 >= a0 + a3
        Since a3 >= a2, we have a1 + a3 >= a1 + a2
        
        Hence a1 + a3 >= max(a0 + a3, a1 + a2). This contradicts our premise.
        
        Therefore, the greedy manner is the optimal way to find the min max pair.
         */
        Arrays.sort(nums);
        int res = 0;
        int i = 0; int j = nums.length - 1;
        while (i < j) res = Math.max(res, nums[i++] + nums[j--]);
        return res;
    }
}
