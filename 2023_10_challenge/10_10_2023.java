class Solution {
    public int minOperations(int[] nums) {
        /*
        LeetCode 2009 (Hint)
        
        The hint helps pointing me on the right direction. The explanation is provided in the comments below.
        
        O(NlogN), 125 ms, faster than 19.61%
         */
        // sort unique nums
        Set<Integer> numsSet = new HashSet<>();
        for (int n : nums) numsSet.add(n);
        Integer[] uniqs = numsSet.toArray(new Integer[0]);
        Arrays.sort(uniqs);
        // go through each num in uniqs and try to include as many elements larger than it in the final continuous
        // array. To do so, we must set the curretn num as the smallest in the continous array. Then we can find the
        // max needed and use binary search to count the number of unique values already existing in the nums. These
        // are the values that do not need to be changed. This also gives us the min number of values to change for
        // each unique num serving as the min of the final continous array.
        // We only have to consider the current num as min, in contrast to as max, because the purpose of considering
        // the current num as max is to include as many elements smaller than the current num in the final continous
        // array. This is equivalent to previous rounds on those smaller elements when they try to include the current
        // num in the final continous array. Thus, we don't have to do this operation for both min and max.
        int max; int maxIdx;
        int res = Integer.MAX_VALUE;
        for (int i = 0; i < uniqs.length; i++) {
            // handle the max needed when nums[i] does not change
            max = uniqs[i] + nums.length - 1;
            maxIdx = Arrays.binarySearch(uniqs, max);
            if (maxIdx < 0) maxIdx = -(maxIdx + 1) - 1;
            res = Math.min(res, nums.length - (maxIdx - i) - 1);
        }
        return res;
    }
}


class Solution {
    public int minOperations(int[] nums) {
        /*
        The second approach from the official solution where we use sliding window to find the index in uniqs that
        points to a value that is smaller or equal to the desired max.

        O(NlogN), 83 ms, faster than 28.43% 
         */
        // sort unique nums
        Set<Integer> numsSet = new HashSet<>();
        for (int n : nums) numsSet.add(n);
        Integer[] uniqs = numsSet.toArray(new Integer[0]);
        Arrays.sort(uniqs);
        // go through each num in uniqs and try to include as many elements larger than it in the final continuous
        // array. To do so, we must set the curretn num as the smallest in the continous array. Then we can find the
        // max needed and use binary search to count the number of unique values already existing in the nums. These
        // are the values that do not need to be changed. This also gives us the min number of values to change for
        // each unique num serving as the min of the final continous array.
        // We only have to consider the current num as min, in contrast to as max, because the purpose of considering
        // the current num as max is to include as many elements smaller than the current num in the final continous
        // array. This is equivalent to previous rounds on those smaller elements when they try to include the current
        // num in the final continous array. Thus, we don't have to do this operation for both min and max.
        int max; int maxIdx = 0;
        int res = Integer.MAX_VALUE;
        for (int i = 0; i < uniqs.length; i++) {
            // handle the max needed when nums[i] does not change
            max = uniqs[i] + nums.length - 1;
            while (maxIdx < uniqs.length && uniqs[maxIdx] <= max) {maxIdx++;}
            res = Math.min(res, nums.length - (maxIdx - i));
        }
        return res;
    }
}
